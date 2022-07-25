class Controller:
    def __init__(self,data):
        self.question_list = data
        self.question_number = 0
        self.score = 0

    # ไปยังคำถามข้อถัดไป
    def nextQuestion(self):
        current = self.question_list[self.question_number]
        self.question_number+=1
        print(self.question_number,")",current.text," = ? (True/False)")
        user_answer = input("ป้อนคำตอบ ")
        self.checkAnswer(user_answer, current.answer)


    def hasQuestion(self):
        return self.question_number < len(self.question_list)

    def checkAnswer(self,userInput,correct_answer):
        if userInput.lower() == correct_answer.lower():
            #ได้รับคะเเนน
            self.score+=1
            print("คะแนน = ",self.score)
        else:
            print("ตอบผิด")
            print("เฉลย = ",correct_answer)
