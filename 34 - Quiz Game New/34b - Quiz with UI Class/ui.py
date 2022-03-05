from data import QuestionData
from question_model import Question
from quiz_brain import QuizBrain
from tkinter import *


GREY = "#474b4e"
GREEN = "#DFF5CE"
RED = "#ff94b6"
WHITE = "#ffffff"
FONT_NAME = "Courier"


class QuizInterface():

    def __init__(self):

        # ---------------------------- UI SETUP ------------------------------- #

        # WINDOW
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=50, pady=30, bg=GREY)

        # SCORE + QUESTION
        self.no_txt = Label(text="1/10 ", font=(FONT_NAME, 15, "bold"), bg=GREY)
        self.no_txt.grid(row=0, column=0, sticky="w")
        self.score_txt = Label(text="Score: 0", font=(FONT_NAME, 15, "bold"), bg=GREY)
        self.score_txt.grid(row=0, column=1, sticky="e")

        # QUIZ TEXT
        self.canvas = Canvas(width=260, height=200, bg="white")
        self.question_text = self.canvas.create_text(
            130,
            100,
            width=250,
            text="Some Question Text",
            font=(FONT_NAME, 15, "bold")
        )

        # BUTTON 1
        self.false_img = PhotoImage(file="images/false.png")
        self.red_btn = Button(text="Start", image=self.false_img, font=(FONT_NAME, 12, "bold"), bg=GREY, command=self.press_red)

        # BUTTON 2
        self.true_img = PhotoImage(file="images/true.png")
        self.green_btn = Button(text="Reset", image=self.true_img, font=(FONT_NAME, 12, "bold"), bg=GREY, command=self.press_green)

        # CATEGORIES
        WIDTH = 8
        HEIGHT = 3
        self.games_btn = Button(width=WIDTH,
                                height=HEIGHT,
                                text="Video\nGames",
                                font=(FONT_NAME, 16, "bold"),
                                bg=WHITE,
                                command=lambda: self.initiate_quiz("video_games"))
        self.music_btn = Button(width=WIDTH,
                                height=HEIGHT,
                                text="Music",
                                font=(FONT_NAME, 16, "bold"),
                                bg=WHITE,
                                command=lambda: self.initiate_quiz("music"))
        self.science_btn = Button(width=WIDTH,
                                  height=HEIGHT,
                                  text="Science\n&\nNature",
                                  font=(FONT_NAME, 16, "bold"),
                                  bg=WHITE,
                                  command=lambda: self.initiate_quiz("science_nature"))
        self.computer_btn = Button(width=WIDTH,
                                   height=HEIGHT,
                                   text="Computer\nScience",
                                   font=(FONT_NAME, 16, "bold"),
                                   bg=WHITE,
                                   command=lambda: self.initiate_quiz("computer_science"))

        self.show_categories()
        self.window.mainloop()

    # ---------------------------- Functions ------------------------------- #

    def show_categories(self):
        self.games_btn.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.music_btn.grid(row=1, column=1, sticky="e", padx=10, pady=10)
        self.science_btn.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.computer_btn.grid(row=2, column=1, sticky="e", padx=10, pady=10)

    def hide_categories(self):
        self.games_btn.grid_forget()
        self.music_btn.grid_forget()
        self.science_btn.grid_forget()
        self.computer_btn.grid_forget()

    def show_quiz(self):
        # self.q_text.grid(row=1, column=0, columnspan=2, pady=(10, 20))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(10, 20))
        self.red_btn.grid(row=2, column=0, sticky="w")
        self.green_btn.grid(row=2, column=1, sticky="e")

    def hide_quiz(self):
        self.canvas.grid_forget
        self.red_btn.grid_forget()
        self.green_btn.grid_forget()

    def initiate_quiz(self, category):
        global quiz, in_game
        question_bank = []
        question_data = QuestionData()

        if category == "video_games":
            question_data.video_games()
        elif category == "music":
            question_data.music()
        elif category == "science_nature":
            question_data.science_nature()
        elif category == "computer_science":
            question_data.computer_science()

        for question in question_data.data['results']:
            question_bank.append(Question(question["question"], question["correct_answer"], question["difficulty"]))
        quiz = QuizBrain(question_bank)

        self.hide_categories()
        self.show_quiz()
        self.load_question()
        in_game = True

    def load_question(self):
        self.canvas.itemconfig(self.question_text, text=quiz.get_current_question())

    def press_green(self):
        if in_game:
            if quiz.check_answer("True"):
                self.canvas.config(bg=GREEN)
            else:
                self.canvas.config(bg=RED)
            self.canvas.after(500, lambda: self.canvas.config(bg=WHITE))
            self.canvas.after(500, self.proceed_after_question)
        if not in_game:
            self.hide_quiz()
            self.show_categories()

    def press_red(self):
        if in_game:
            if quiz.check_answer("False"):
                self.canvas.config(bg=GREEN)
            else:
                self.canvas.config(bg=RED)
            self.canvas.after(500, lambda: self.canvas.config(bg=WHITE))
            self.canvas.after(500, self.proceed_after_question)
        if not in_game:
            exit()

    def proceed_after_question(self):
        print("proceed_after_question")
        global in_game
        if quiz.still_has_question():
            quiz.next_question()
            self.load_question()
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"              ^\n"
                                        f"              |\n"
                                        f"            Score\n"
                                        f"\n"
                                        f"     Finished \n"
                                        f"\n"
                                        f"  Exit      Again\n"
                                        f"   |          |\n"
                                        f"   v          v")
            in_game = False
        self.update_labels()

    def update_labels(self):
        self.no_txt.config(text=f"{quiz.question_number + 1}/10")
        self.score_txt.config(text=f"Score: {quiz.score}")
