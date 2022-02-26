import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def clicked():
    file = filedialog.askopenfile()
    if file is not None:
        content = file.read()
window = Tk()
window.title("Тестовое окно на Python")
window.geometry('400x250')
btn = Button(window, text="Загрузить картинку", bg="lightgrey", fg="black", command=clicked)
btn.pack(side=LEFT)
spin = Spinbox(window, from_=0, to=100)
spin.pack()
frame = tkinter.Frame(window)
frame.pack()
image = Image.open("C:\Program Files\JetBrains\IMG_20220123_232540.jpg")
canvas = tkinter.Canvas(frame, height=1076, width=1435)
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.grid(row=1, column=3)
window.mainloop()
