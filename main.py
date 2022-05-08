import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw

def Spin():  # редактор перехода
    spn_win = Tk()
    spn_win.title("Factor choosing")
    spn_win.geometry('260x50')
    spn_win.resizable(height=None, width=None)
    spn_win.iconbitmap('YON.ico')
    spin = Spinbox(spn_win, from_=-100, to=100)
    apply_btn = Button(spn_win, text='Применить', command=lambda: window.Equal_f(spn_win, spin.get()))
    spin.pack(anchor=CENTER)
    apply_btn.pack(anchor=CENTER)
    spn_win.mainloop()

def Compression():
    cmp_win = Tk()
    cmp_win.title("Степень сжатия")
    cmp_win.geometry('260x50')
    cmp_win.resizable(height=None, width=None)
    cmp_win.iconbitmap('YON.ico')
    spin = Spinbox(cmp_win, from_=2, to=1000)
    apply_btn = Button(cmp_win, text='Применить', command=lambda: window.Equal_c(cmp_win, spin.get()))
    spin.pack(anchor=CENTER)
    apply_btn.pack(anchor=CENTER)
    cmp_win.mainloop()

class Root_win(Tk):
    invert_btn_value = False
    factor = 50
    cmp = 1
    def __init__(self):
        super().__init__()

    def Inverting(self):
        self.invert_btn_value = not self.invert_btn_value

    def Error_upload(self):  #ошибка загрузки
        answer = messagebox.showerror(
            "Ошибка!",
            "Не удалось открыть файл. Попробуйте снова.")

    def Error_cmp(self):
        answer = messagebox.showerror(
            "Ошибка!",
            "Шаг сжатия больше размеров изображения. Уменьшите сжатие и попробуйте снова.")

    def Equal_c(self, win, x):  # установка степени сжатия
        self.cmp = int(x)
        win.destroy()

    def Equal_f(self, win, num):  # установка перехода
        self.factor = int(num)
        win.destroy()

    def upl_clicked(self):  # загрузка картинки
        file = filedialog.askopenfilename(filetypes=[("Image files",
                                                      "*.jpg; *.jpeg; *.png; *.bmp; *.raw; *.gif; *.tiff")])
        try:
            if not self.invert_btn_value:
                white, black = 255, 0
            else:
                white, black = 0, 255
            image = Image.open(file)
            draw = ImageDraw.Draw(image)
            width = image.size[0]  # Определяем ширину.
            height = image.size[1]  # Определяем высоту.
            if self.cmp > min(width, height):
                self.Error_cmp()
            pix = image.load()  # массив пикселей
            for i in range(width):
                for j in range(height):
                    a = pix[i, j][0]
                    b = pix[i, j][1]
                    c = pix[i, j][2]
                    S = a + b + c
                    if S > ((255 + self.factor) // 2) * 3:  # распределение пикселей на черные и белые
                        a, b, c = white, white, white
                    else:
                        a, b, c = black, black, black
                    draw.point((i, j), (a, b, c))
            image.show()
        except AttributeError:
            self.Error_upload()

if __name__ == '__main__':
    window = Root_win()
    window.title("Your Own Nonogram")  # название окна
    window.geometry('458x458')  # размеры окна
    window.iconbitmap('YON.ico')  # иконка для окна

    mainmenu = Menu(window)
    window.config(menu=mainmenu)

    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Загрузить картинку",
                         command=window.upl_clicked)
    filemenu.add_checkbutton(label='Инвертировать картинку',
                             command=window.Inverting)
    filemenu.add_separator()
    filemenu.add_command(label="Выход",
                         command=window.destroy)

    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="Помощь")
    helpmenu.add_command(label="О программе")

    mainmenu.add_cascade(label="Файл",
                         menu=filemenu)
    mainmenu.add_command(label="Переход", command=Spin)
    mainmenu.add_command(label='Сжатие', command=Compression)
    mainmenu.add_cascade(label="Справка",
                         menu=helpmenu)
    #image = Image.open("Plug_image.jpg")
    #canvas = tkinter.Canvas(window, height=image.height, width=image.width)
    #photo = ImageTk.PhotoImage(image)
    #canvas.create_image(0, 0, anchor='nw', image=photo)
    #canvas.pack(anchor=CENTER)
    window.mainloop()
