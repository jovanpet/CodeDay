from tkinter import *
from PIL import Image, ImageTk

def onClick():
    ar = IntVar()

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()

    t = Checkbutton(app, text="Party", variable = var)

    t.grid(row = 100, column = 5)

    t1 = Checkbutton(app, text="Hungover", variable = var1)

    t1.grid(row = 100, column = 6)

    t2 = Checkbutton(app, text="Family", variable = var2)

    t2.grid(row = 100, column = 7)

    t3 = Checkbutton(app, text="Football", variable = var3)

    t3.grid(row = 100, column = 8)

    t4 = Checkbutton(app, text="Breakfast", variable = var4)

    t4.grid(row = 100, column = 9)

    t5 = Checkbutton(app, text="Date", variable = var5)

    t5.grid(row = 100, column = 10)

    t6 = Checkbutton(app, text="Binge", variable = var6)

    t6.grid(row = 100, column = 11)

    t7 = Checkbutton(app, text="Home-Alone", variable = var7)

    t7.grid(row = 100, column = 12)

    a1=Button(app, text = "Apply", command = onClick)

    a1.grid(row = 150, column = 13)


