class QuizBrain:
    """docstring"""
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """ doc """
        #print(f"Question {self.question_number} of {len(self.question_list)} total questions.")
        return self.question_number < len(self.question_list)

    def next_question(self):
        """ doc """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q{self.question_number}: {current_question.text} (True/False): "
        )
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_a, correct_a):
        """ doc """
        if user_a.lower() == correct_a.lower():
            print("Yay, this is correct.")
            self.score += 1
        else:
            print("Sorry, wrong. Think again..")
        print(f"The correct answer was {correct_a}.")
    