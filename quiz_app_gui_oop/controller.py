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

    def hasQuestion(self):
        return self.question_number < len(self.question_list)