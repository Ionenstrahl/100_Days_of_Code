from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    top_txt.config(text="Timer", fg=GREEN)

    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")

    global reps
    reps = 0
    checkmark_txt.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count = work_sec
        top_txt.config(text="Work", fg=GREEN)
    elif reps % 8 == 7:
        count = long_break_sec
        top_txt.config(text="Break", fg=RED)
    else:
        count = short_break_sec
        top_txt.config(text="Break", fg=PINK)
    reps += 1

    count_down(count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def clock_format(count):
    if count < 10:
        count = f"0{count}"
    return count


def count_down(count):
    count_min = clock_format(count // 60)
    count_sec = clock_format(count % 60)
    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ""
        work_sessions = (reps + 1) // 2
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_txt.config(text=marks)
        start_timer()


    # ---------------------------- UI SETUP ------------------------------- #

# WINDOW
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

# TIMER
top_txt = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
top_txt.grid(row=0, column=1)

# CANVAS = IMAGE + TEXT
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# BUTTON 1
start_btn = Button(text="Start", font=(FONT_NAME, 12, "bold"), bg=GREEN, fg=RED, command=start_timer)
start_btn.grid(row=2, column=0)

# BUTTON 2
start_btn = Button(text="Reset", font=(FONT_NAME, 12, "bold"), bg=GREEN, fg=RED, command=reset_timer)
start_btn.grid(row=2, column=2)

# CHECKMARK
checkmark_txt = Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
checkmark_txt.grid(row=3, column=1)


window.mainloop()
