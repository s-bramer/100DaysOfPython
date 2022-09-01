from data import question_data
from question_model import MyQuestion
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = MyQuestion(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    print(f"Your score is {quiz.score}/{quiz.question_number}")
    print()
print("You finished the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
