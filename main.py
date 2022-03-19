import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import Start_Window

class Root_win:
    def __init__(self):
        self.window = Tk()
        self.window.title("Your Own Nonogram")   #название окна
        self.window.geometry('400x250')    #размеры окна
        self.window.iconbitmap('YON.ico')    #ставим иконку для окна

        mainmenu = Menu(self.window)
        self.window.config(menu=mainmenu)

        invert_btn = IntVar()
        filemenu = Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Загрузить картинку", command=self.upl_clicked)
        filemenu.add_checkbutton(label='Инвертировать картинку', variable=invert_btn, onvalue=1, offvalue=0)
        filemenu.add_separator()
        filemenu.add_command(label="Выход", command=self.window.destroy)

        helpmenu = Menu(mainmenu, tearoff=0)
        helpmenu.add_command(label="Помощь")
        helpmenu.add_command(label="О программе")

        mainmenu.add_cascade(label="Файл",
                             menu=filemenu)
        mainmenu.add_cascade(label="Справка",
                             menu=helpmenu)

        self.invert_btn_value = invert_btn.get

        spin = Spinbox(self.window, from_=-100, to=100)
        spin.grid(row=2, column=1)

        self.window.mainloop()

    def Error_win(self):  #ошибка загрузки
        answer = messagebox.showerror(
            "Ошибка!",
            "Не удалось открыть файл. Попробуйте снова.")

    def upl_clicked(self):
        file = filedialog.askopenfilename()
        if file is not None:
            #if not self.invert_btn_value:
            white, black = 255, 0
            #else:
            #    white, black = 0, 255
            image = Image.open(file)
            draw = ImageDraw.Draw(image)
            width = image.size[0]  # Определяем ширину.
            height = image.size[1]  # Определяем высоту.
            pix = image.load()  #массив пикселей
            factor = 50  #регулировка перехода
            for i in range(width):
                for j in range(height):
                    a = pix[i, j][0]
                    b = pix[i, j][1]
                    c = pix[i, j][2]
                    S = a + b + c
                    if (S > (((255 + factor) // 2) * 3)):  #распределение пикселей на черные и белые
                        a, b, c = white, white, white
                    else:
                        a, b, c = black, black, black
                    draw.point((i, j), (a, b, c))

            panel = Label(self.window, image=ImageTk.PhotoImage(image))  #вывод изображения
            panel.grid(row=3, column=2)
            image.show()
        else:
            self.Error_win()

app = Root_win()
