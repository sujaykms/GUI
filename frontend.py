import tkinter
from tkinter import END
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import Listbox
from tkinter import Scrollbar
from tkinter import Button
from tkinter import messagebox
import backend

def get_selected_row(event):
    global selected_tuple
    try:
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[0])
    except:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    
    for row in backend.search(Id_text.get(),name_text.get(),ccode_text.get(),district_text.get(),population_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(Id_text.get(),name_text.get(),ccode_text.get(),district_text.get(),population_text.get())
    list1.delete(0,END)
    list1.insert(END,(Id_text.get(),name_text.get(),ccode_text.get(),district_text.get(),population_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],Id_text.get(),name_text.get(),ccode_text.get(),district_text.get(),population_text.get())

def goodbye():
    if messagebox.askyesno("Exit", "Wanna leave?"):
        window.destroy()

window=tkinter.Tk()


window.wm_title("GEO - INFO")

l1=Label(window,text="Name")
l1.grid(row=0,column=0)

l2=Label(window,text="C-code")
l2.grid(row=0,column=2)

l6 = Label(text="Capital letters only!")

l3=Label(window,text="District")
l3.grid(row=1,column=0)

l4=Label(window,text="Population")
l4.grid(row=1,column=2)

l5=Label(window,text="Id")
l5.grid(row=0,column=4)

name_text=StringVar()
e1=Entry(window,textvariable=name_text)
e1.grid(row=0,column=1)

Id_text=StringVar()
e5=Entry(window,textvariable=Id_text)
e5.grid(row=0,column=5)

ccode_text=StringVar()
e2=Entry(window,textvariable=ccode_text)
e2.grid(row=0,column=3)

district_text=StringVar()
e3=Entry(window,textvariable=district_text)
e3.grid(row=1,column=1)

population_text=StringVar()
e4=Entry(window,textvariable=population_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=40)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=15,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=15,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=15,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=15,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=15,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=15,command=goodbye)
b6.grid(row=7,column=3)

window.protocol("WM_DELETE_WINDOW", goodbye)

window.mainloop()
