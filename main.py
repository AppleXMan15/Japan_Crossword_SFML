import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import Start_Window

class Root_win:
    def __init__(self):
        self.window = Tk()
        self.window.title("Тестовое окно на Python")
        self.window.geometry('400x250')

        btn = Button(self.window, text="Загрузить картинку", bg="lightgrey", fg="black", command=self.upl_clicked)
        btn.grid(row=1, column=1)

        spin = Spinbox(self.window, from_=0, to=100)
        spin.grid(row=2, column=1)

        frame = tkinter.Frame(self.window)
        frame.grid(row=1, column=2)

        self.window.mainloop()

    def Error_win(self):
        Er_win = Tk()
        Er_win.title("Ошибка загрузки")
        Er_win.geometry('250x75')
        Er_win.resizable(width=False, height=False)
        lbl = Label(Er_win, text="\nЗагрузка файла не удалась.\nПопробуйте снова.")
        lbl.pack()
        Er_win.mainloop()

    def upl_clicked(self):
        file = filedialog.askopenfile()
        if file is not None:
            content = file.read()
            canvas = tkinter.Canvas(self.frame, height=107, width=146)
            photo = ImageTk.PhotoImage(content)
            image = canvas.create_image(0, 0, anchor='nw', image=photo)
            canvas.pack()
        else:
            self.Error_win()


app = Root_win()
