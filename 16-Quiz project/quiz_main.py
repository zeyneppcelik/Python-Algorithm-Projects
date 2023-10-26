from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain
from random import choice

question_bank=[]
questions=[Question(question_text=q["question"], question_answer=q["correct_answer"]) for q in question_data]
for i in range(0,10):
    question_bank.append(choice(questions))

new_quiz=QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()
    print(" ")

print("Congratulations! You have completed the quiz.")
print(f"Your score: {new_quiz.score}/10")