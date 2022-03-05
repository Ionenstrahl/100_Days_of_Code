from data import QuestionData
from question_model import Question
from quiz_brain import QuizBrain
from tkinter import *


GREY = "#474b4e"
GREEN = "#DFF5CE"
RED = "#ff94b6"
WHITE = "#ffffff"
FONT_NAME = "Courier"

# ---------------------------- Functions ------------------------------- #


def show_categories():
    games_btn.grid(row=1, column=0, sticky="w", padx=10, pady=10)
    music_btn.grid(row=1, column=1, sticky="e", padx=10, pady=10)
    science_btn.grid(row=2, column=0, sticky="w", padx=10, pady=10)
    computer_btn.grid(row=2, column=1, sticky="e", padx=10, pady=10)


def hide_categories():
    games_btn.grid_forget()
    music_btn.grid_forget()
    science_btn.grid_forget()
    computer_btn.grid_forget()


def show_quiz():
    q_text.grid(row=1, column=0, columnspan=2, pady=(10, 20))
    red_btn.grid(row=2, column=0, sticky="w")
    green_btn.grid(row=2, column=1, sticky="e")


def hide_quiz():
    red_btn.grid_forget()
    green_btn.grid_forget()
    q_text.grid_forget()


def initiate_quiz(category):
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

    hide_categories()
    show_quiz()
    load_question()
    in_game = True


def load_question():
    q_text.config(state=NORMAL)
    q_text.replace("1.0", END, quiz.get_current_question())
    q_text.config(state=DISABLED)


def press_green():
    if in_game:
        if quiz.check_answer("True"):
            q_text.config(bg=GREEN)
        else:
            q_text.config(bg=RED)
        q_text.after(500, lambda: q_text.config(bg=WHITE))
        q_text.after(500, proceed_after_question)
    if not in_game:
        hide_quiz()
        show_categories()
        reset_labels()


def press_red():
    if in_game:
        if quiz.check_answer("False"):
            q_text.config(bg=GREEN)
        else:
            q_text.config(bg=RED)
        q_text.after(500, lambda: q_text.config(bg=WHITE))
        q_text.after(500, proceed_after_question)
    if not in_game:
        exit()


def proceed_after_question():
    global in_game
    if quiz.still_has_question():
        quiz.next_question()
        load_question()
    else:
        q_text.config(state=NORMAL)
        q_text.replace("1.0", END, f"\n  Finished with {quiz.score} Points\n\n   Exit         Try Again\n    |               |\n    V               V")
        q_text.config(state=DISABLED)
        in_game = False
    update_labels()


def update_labels():
    no_txt.config(text=f"{quiz.question_number + 1}/10")
    score_txt.config(text=f"Score: {quiz.score}")


def reset_labels():
    no_txt.config(text=f"1/10")
    score_txt.config(text=f"Score: 0")


# ---------------------------- UI SETUP ------------------------------- #

# WINDOW
window = Tk()
window.title("Quiz Game")
window.config(padx=50, pady=30, bg=GREY)

# SCORE + QUESTION
no_txt = Label(text="1/10 ", font=(FONT_NAME, 15, "bold"), bg=GREY)
no_txt.grid(row=0, column=0, sticky="w")
score_txt = Label(text="Score: 0", font=(FONT_NAME, 15, "bold"), bg=GREY)
score_txt.grid(row=0, column=1, sticky="e")

# QUIZ TEXT
q_text = Text(window, width=26, height=6)
q_text.config(font=(FONT_NAME, 13, "bold"), state=DISABLED)

# BUTTON 1
false_img = PhotoImage(file="images/false.png")
red_btn = Button(text="Start", image=false_img, font=(FONT_NAME, 12, "bold"), bg=GREY, command=press_red)

# BUTTON 2
true_img = PhotoImage(file="images/true.png")
green_btn = Button(text="Reset", image=true_img, font=(FONT_NAME, 12, "bold"), bg=GREY, command=press_green)

# CATEGORIES
WIDTH = 8
HEIGHT = 3
games_btn = Button(width=WIDTH, height=HEIGHT, text="Video\nGames", font=(FONT_NAME, 16, "bold"), bg=WHITE,
                   command=lambda: initiate_quiz("video_games"))
music_btn = Button(width=WIDTH, height=HEIGHT, text="Music", font=(FONT_NAME, 16, "bold"), bg=WHITE,
                   command=lambda: initiate_quiz("music"))
science_btn = Button(width=WIDTH, height=HEIGHT, text="Science\n&\nNature", font=(FONT_NAME, 16, "bold"), bg=WHITE,
                     command=lambda: initiate_quiz("science_nature"))
computer_btn = Button(width=WIDTH, height=HEIGHT, text="Computer\nScience", font=(FONT_NAME, 16, "bold"), bg=WHITE,
                      command=lambda: initiate_quiz("computer_science"))


show_categories()
window.mainloop()
