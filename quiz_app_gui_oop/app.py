from question import Question
from data import question_data

all_question = []
"""
question = Question("1 + 1 = 10 ?", "False")
print(question.text)
print(question.answer)
"""
for item in question_data:
    text = item["text"]
    answer = item["answer"]
    question = Question(text, answer)
    all_question.append(question)


print(all_question[0].text)
print(all_question[1].text)
print(all_question[2].text)
