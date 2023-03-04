from tkinter import *
from tkinter import ttk

import googletrans
from googletrans import Translator

root = Tk()
root.title("google translator")
root.geometry("1200x600")
root.resizable(False,False)
# root.configure(background = "white")

def label_change():
    c = drop1.get()
    c1 = drop2.get()
    label1.configure(text = c)
    label2.configure(text = c1)
    root.after(1000,label_change)

def trans():
    txt = text1.get(1.0,END)
    t1 = Translator()
    trans_txt = t1.translate(txt,src=drop1.get(),dest=drop2.get())
    trans_txt = trans_txt.text
    
    text2.delete(1.0,END)
    text2.insert(END,trans_txt)

# image_icon = PhotoImage(file = "google.png")
# root.iconphoto(False,image_ico)
icon_img = PhotoImage(file = "arrow.png")
image_label = Label(root,image = icon_img,width=150)
image_label.place(x=460,y=50)
language = googletrans.LANGUAGES
languageV =list(language.values())
lang1 = language.keys()

drop1 =ttk.Combobox(root,values = languageV,font = "ROBOT 14",state = "r" )
drop1.place(x=110,y=20)
drop1.set("ENGLISH")
label1 = Label(root,text = "ENGLISH",font = "segoe 30 bold",bg = "white", width=18,bd =5,relief=GROOVE)
label1.place(x=10,y=50)

drop2 =ttk.Combobox(root,values = languageV,font = "ROBOT 14",state = "r" )
drop2.place(x=730,y=20)
drop2.set("CHOOSE LANGUAGE")
label2 = Label(root,text = "ENGLISH",font = "segoe 30 bold",bg = "white", width=18,bd =5,relief=GROOVE)
label2.place(x=620,y=50)

#first frame
f= Frame(root,bg = "Black",bd = 5)
f.place(x=10,y=118,width=440,height=210)

text1 = Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap = WORD)
text1.place(x=0,y=0,width=430,height=200)

sb1 = Scrollbar(f)
sb1.pack(side = "right",fill = 'y')

sb1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar)

#second frame

f1 = Frame(root,bg = "Black",bd = 5)
f1.place(x=620,y=118,width=440,height=210)

text2 = Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap = WORD)
text2.place(x=0,y=0,width=430,height=200)

sb2 = Scrollbar(f1)
sb2.pack(side = "right",fill = 'y')

sb2.configure(command=text2.yview)
text2.configure(yscrollcommand=Scrollbar)

#translate button
translate = Button(root,text="Translate",font=("Roboto",15),activebackground="white",cursor="hand2",
                   bd =1,width=10,height=2,bg="black",fg="white",command=trans)
translate.place(x=476,y=250)

label_change()



root.mainloop()



