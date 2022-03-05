class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    def next_question(self):
        self.question_number += 1

    def still_has_question(self):
        return self.question_number + 1 < len(self.questions_list)

    def check_answer(self, user_answer):
        current_question = self.questions_list[self.question_number]
        if user_answer == current_question.answer:
            self.increase_score()
            return True

    def increase_score(self):
        current_question = self.questions_list[self.question_number]
        if current_question.difficulty == "easy":
            self.score += 1
        if current_question.difficulty == "medium":
            self.score += 2
        if current_question.difficulty == "hard":
            self.score += 3

    def get_current_question(self):
        print(f"question number: {self.question_number}")
        print(f"len(self.questions_list):  {len(self.questions_list)}")
        current_question = self.questions_list[self.question_number]
        q = f"""Q.{self.question_number + 1} - {current_question.difficulty}:\n{current_question.text}"""
        q = q.replace("&#039;", "'")
        q = q.replace('&quot;', '"')
        return q


