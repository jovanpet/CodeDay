from tkinter import *
from PIL import Image, ImageTk
from Collage_lunch import *

dict_fridge={} #globalna za frizider

dict_recepies=first()

theam=[]

dict_type={}

final_theme_list = []

final_Emotion_list = []

def be_done():
    pair_item_quan.append(('done',0))
    ingridiatns=open("Ingredients.txt", "r")
    if ingridiatns.mode=="r":
        contents_ingridiatns = ingridiatns.read()

    dict_fridge=fridge(my_split(contents_ingridiatns), pair_item_quan)
    #Fridge
    #---------------------------------------------------
    var_fridge=StringVar()

    var_start_fridge.set("")
    
    fridge_box= Message( app, textvariable=var_fridge, relief=SUNKEN , width=300 ).grid(row=11, column= 1)

    help=""
    for i,j in dict_fridge.items():
        help+= i+ " : "+ str(j)  + "\n"
    var_fridge.set(help)
    #-----------------------------------------------------




def applyFunction():
    string_item = Item_Enter.get()
    int_quan = Quantity_Enter.get()
    pair_item_quan.append((str(string_item), int(int_quan)))
    Item_Enter.delete(0, END)
    Quantity_Enter.delete(0, END)
    return pair_item_quan 

def check_emo_list():
    Emotions_list = [
                (int(var.get()), 'Sad'), (int(var1.get()), 'Happy'), 
                (int(var2.get()), 'Romance'), (int(var3.get()), 'Hungry'), 
                (int(var4.get()), 'Angry'), (int(var5.get()), 'Stressful')
                ]
    for i in Emotions_list:
        if i[0] == 1:
            final_Emotion_list.append(i[1]) #final emotion list
    

def check_theme_list():
    Theme_list = [
            (int(var6.get()), 'Party'),(int(var7.get()), 'Hungover'),
            (int(var8.get()), 'Family'),(int(var9.get()), 'Football'),(int(var10.get()), 'Breakfast'),
            (int(var11.get()), 'Date'),(int(var12.get()), 'Binge'),(int(var13.get()), 'Home-Alone')
             ]
    for i in Theme_list:
        if i[0] == 1:
            final_theme_list.append(i[1]) #final global list

def check_lists():
    ingridiatns=open("Ingredients.txt", "r")
    if ingridiatns.mode=="r":
        contents_ingridiatns = ingridiatns.read()

    dict_fridge=fridge(my_split(contents_ingridiatns), pair_item_quan)

    type=open('Recepies_type.txt', 'r') #Jovan test file
    if type.mode=='r':
        content_type=type.read()
    dict_type=make_dict(content_type)

    check_emo_list()
    check_theme_list()
    theam= final_theme_list + final_Emotion_list #lista checked stuff in code
    final_Emotion_list.clear()
    final_theme_list.clear()
    print(devide_into_can_cant(search_similar_fridge(dict_fridge,dict_recepies), search_similar_type(theam, dict_type)))

    #send to API

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
Label(app, text="Mood:").grid(row = 0, column=5)
Label(app, text="Theme:").grid(row = 2, column=5)
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
apply = Button(app, text="Apply", command=applyFunction).grid(column=1)
done= Button( app, text='Done', command=be_done).grid(column= 1)

#FRIDGE
#This will show what is inside the firdge
#------------------------------
var_start_fridge=StringVar()

fridge_start= Message( app, textvariable=var_start_fridge, relief=SUNKEN, width=124  ).grid(row=11, column= 1)

var_start_fridge.set("Here will be your items when you type them in:")
#----------------------------
Unit_choice = StringVar(app)
Unit_choice.set(unit_list[0])
Units = OptionMenu(app, Unit_choice, *unit_list).grid(row = 1, column = 4)


#path = "fridgeIMG.jpg"
#img = ImageTk.PhotoImage(Image.open(path))
#panel = Label(app, image = img).grid(row = 0) 

var = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()

c = Checkbutton(app, text="Sad", variable = var)
c.grid(row = 1, column = 5)

c1 = Checkbutton(app, text="Happy", variable = var1)
c1.grid(row = 1, column = 6)

c2 = Checkbutton(app, text="Romance", variable = var2)
c2.grid(row = 1, column = 7)

c3 = Checkbutton(app, text="Hungry", variable = var3)
c3.grid(row = 1, column = 8)

c4 = Checkbutton(app, text="Angry", variable = var4)
c4.grid(row = 1, column = 9)

c5 = Checkbutton(app, text="Stressful", variable = var5)
c5.grid(row = 1, column = 10)


c6 = Checkbutton(app, text="Party", variable = var6)
c6.grid(row = 3, column = 5)

c7 = Checkbutton(app, text="Hungover", variable = var7)
c7.grid(row = 3, column = 6)

c8 = Checkbutton(app, text="Family", variable = var8)
c8.grid(row = 3, column = 7)

c9 = Checkbutton(app, text="Football", variable = var9)
c9.grid(row = 3, column = 8)

c10 = Checkbutton(app, text="Breakfast", variable = var10)
c10.grid(row = 3, column = 9)

c11 = Checkbutton(app, text="Date", variable = var11)
c11.grid(row = 3, column = 10)

c12 = Checkbutton(app, text="Binge", variable = var12)
c12.grid(row = 3, column = 11)

c13 = Checkbutton(app, text="Home-Alone", variable = var13)
c13.grid(row = 3, column = 12)

a1=Button(app, text = "Apply", command=check_lists)
a1.grid(row = 6, column = 15)

app.mainloop()