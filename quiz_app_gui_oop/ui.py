from tkinter import *
THEME_APP = '#375362'

class UserInterface:
    def __init__(self):
        #หน้าต่างโปรแกรม
        self.window = Tk()
        self.window.title("โปรแกรมทำข้อสอบ")
        self.window.config(padx=20,pady=20,bg=THEME_APP)
        #พื้นที่แสดงคะแนนสอบ
        self.scoreLabel = Label(text="คะเเนน : 0",fg="white",bg=THEME_APP)
        self.scoreLabel.grid(row=0,column=2)

        #พื้นที่แสดงโจทย์ปัญหา
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,width=280,text="Pinzaa",font=('Arial',18,'bold'),fill=THEME_APP)

        self.canvas.grid(row=1,column=1,columnspan=2,pady=50)

        #ปุ่มตัวเลือกตอบคำถาม
        true_image = PhotoImage(file="images/check.png")
        self.true_button=Button(image=true_image)
        self.true_button.grid(row=2,column=1)

        false_image = PhotoImage(file="images/remove.png")
        self.false_button=Button(image=false_image)
        self.false_button.grid(row=2,column=2)



        self.window.mainloop()

