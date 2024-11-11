import os
from tkinter import *

root = Tk()
root.title("Sign Language Detection App")

# Adjust size
root.geometry("604x470")

def run():
    os.system('python opencam.py')

# Assuming bg.png is in a folder named "images" in the current working directory
bg_path = os.path.join(os.getcwd(), "images", "bg.png")
bg = PhotoImage(file=bg_path)

label1 = Label(root, image=bg)
label1.place(x=0, y=0)

btn = Button(root, text=' Detect Sign Language ', bd='5', command=run)
btn.place(x=230, y=350)

btn_close = Button(root, text=' Close App ', bd='5', command=root.destroy)
btn_close.place(x=520, y=430)

root.mainloop()
