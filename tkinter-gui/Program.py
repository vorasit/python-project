from tkinter import *
import tkinter.messagebox
root = Tk()
root.title("My GUI")

# สร้างเมนู
myMenu = Menu()
root.config(menu=myMenu)

#สร้างหน้าต่างใหม่
def showWindow():
    Window = Tk()
    Window.title("หน้าต่างใหม่")
    Window.geometry("500x300")
    Window.mainloop()

def aboutProgram():
    tkinter.messagebox.showinfo("รายละเอียด","Pinzaa deverloper")

def exitProgram():
    confrim = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการปิดโปรแกรมหรือไม่ ?")
    if confrim == "yes":
        root.destroy()

# เพิ่มเมนูย่อย
menuitem = Menu()
menuitem.add_command(label="New window",command = showWindow)
menuitem.add_command(label="Open File")
menuitem.add_command(label="Save File")
menuitem.add_command(label="About File",command=aboutProgram)
menuitem.add_command(label="Exit File",command=exitProgram)

# เพิ่มเมนูหลัก
myMenu.add_cascade(label="File",menu=menuitem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")


#ใส่ข้อความในหน้าจอ
#myLabel1 = Label(root,text="Hello World",fg="blue",font=20,bg="yellow").place(x=100,y=300)
myLabel1 = Label(root,text="Hello World",fg="blue",font=20,bg="yellow").pack()
myLabel2 = Label(root,text="Pinzaa",fg="blue",font=20,bg="yellow").pack()

# กล่องข้อความ
txt = StringVar()
myText = Entry(root,textvariable=txt).pack()

# myLabel3 = Label(root,text="Pinzaa",fg="blue",font=20,bg="red").grid(row=2,column=0)
#myLabel2 = Label(root,text="Pinzaa").pack()

def showMessage():
    message = txt.get()
    print(message)
    Label(root,text=message,fg="blue",font=20,bg="yellow").pack()

def openWindow():
    #หน้าจอที่ 2
    myWindow = Tk()
    myWindow.title("รายงานผลการทำงาน")
    myWindow.geometry("500x300")
    
#การใส่ปุ่ม
btn1 = Button(root,text="บันทึก",fg="white",bg="red",command=showMessage).pack()
btn2 = Button(root,text="เปิดรายงาน",fg="white",bg="green",command=openWindow).pack()



#กำหนดขนาดหน้าจอและตำเเหน่งหน้าจอ
root.geometry("600x500+100+400")# w*h+x+y



root.mainloop()


