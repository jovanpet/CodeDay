from tkinter import *
from PIL import Image, ImageTk
from Fridge_Functions import *

def applyFunction():
    string_item = Item_Enter.get()
    int_quan = Quantity_Enter.get()
    pair_item_quan.append((str(string_item), int(int_quan)))
    Item_Enter.delete(0, END)
    Quantity_Enter.delete(0, END)
    print(pair_item_quan)
    

app = Tk()
canvas = app.geometry("1980x1080") 

unit_list = (
    'Single Item(s)',
    'Grams',
     'Kilograms',
     'Pounds',      
     'Liter',
     'Ounces',
     'Oz',
      )

Item = Label(app, text="Items").grid(row = 0, sticky = W)
Quantity = Label(app, text="Quantity").grid(row = 0, column = 2, sticky = W)
Unit = Label(app, text="Unit").grid(row = 0, column = 4)

pair_item_quan = []
Entry_Items  = StringVar()
Item_Enter = Entry(app, textvariable=Entry_Items)
Item_Enter.grid(row = 1, column = 1)



Entry_quantity = IntVar()
Quantity_Enter = Entry(app, textvariable=Entry_quantity)
Quantity_Enter.grid(row = 1, column = 3)


apply = Button(app, text="Apply", command=applyFunction).grid(row = 3)


Unit_choice = StringVar(app)
Unit_choice.set(unit_list[0])
Units = OptionMenu(app, Unit_choice, *unit_list).grid(row = 1, column = 4)


#path = "fridgeIMG.jpg"
#img = ImageTk.PhotoImage(Image.open(path))
#panel = Label(app, image = img).grid(row = 0) 

 
scrollbar = Scrollbar()

var = IntVar()

var1 = IntVar()

var2 = IntVar()

var3 = IntVar()

var4 = IntVar()

var5 = IntVar()

c = Checkbutton(app, text="Sad", variable = var)

c.grid(row = 0, column = 5)

c1 = Checkbutton(app, text="Happy", variable = var1)

c1.grid(row = 0, column = 6)

c2 = Checkbutton(app, text="Romance", variable = var2)

c2.grid(row = 0, column = 7)

c3 = Checkbutton(app, text="Hungry", variable = var3)

c3.grid(row = 0, column = 8)

c4 = Checkbutton(app, text="Angry", variable = var4)

c4.grid(row = 0, column = 9)

c5 = Checkbutton(app, text="Stressful", variable = var5)

c5.grid(row = 0, column = 10)

a=Button(app, text = "Apply", command = onClick)

a.grid(row = 2, column = 11)

bottomframe = Frame(app)
scroll = Scrollbar(app)
app.mainloop()