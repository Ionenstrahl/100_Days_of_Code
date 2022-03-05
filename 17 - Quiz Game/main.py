from data import QuestionData
from question_model import Question
from quiz_brain import QuizBrain


difficulty = input('Choose difficulty between "easy", "medium" and "hard" ')

question_bank = []
question_data = QuestionData(difficulty)
for question in question_data.data['results']:
    question_bank.append(Question(question["question"], question["correct_answer"], question["difficulty"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
