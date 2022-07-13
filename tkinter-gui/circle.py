from tkinter import *
root = Tk()
root.title("โปรแกรมคำนวณพื้นที่วงกลม")


Label(text="รัศมี",font=20).grid(row=0,sticky=W)
radius = IntVar()
et1 = Entry(width=30,textvariable=radius,font=20)
et1.grid(row=0,column=1)

Label(text="พื้นที่",font=20).grid(row=1,sticky=W)
et2 = Entry(width=30,font=20)
et2.grid(row=1,column=1)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)

def calculate():
    et2.delete(0,END)
    r = radius.get()
    area = 3.14*r*r
    et2.insert(0, area)

btn1 = Button(text="คำนวณ",command=calculate).grid(row=2,column=1,sticky=W)
btn2 = Button(text="ล้าง",command=deleteText).grid(row=2,column=1,sticky=E)
root.mainloop()