from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Combo Box")

Label(text="address",font=20).grid(row=0,column=0)
choice = StringVar(value="please select provices")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("bangkok","chai mai","kabi","puket","chon buri")
combo.grid(row=0,column=1)

def selectCity():
    Label(text="your select = "+choice.get()).grid(row=2,column=0)

btn = Button(text="send",command=selectCity)
btn.grid(row=1,column=1)

root.mainloop()