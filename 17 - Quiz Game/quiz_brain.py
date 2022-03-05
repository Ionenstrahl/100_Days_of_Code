import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1

        q_text = html.unescape(current_question.text)

        user_answer = input(f"""Q.{self.question_number} - {current_question.difficulty}: {q_text} (True/False): """)
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"Score: {self.score}/{self.question_number}")
        print("\n")

