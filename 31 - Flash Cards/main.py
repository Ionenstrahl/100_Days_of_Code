import tkinter
import random
import csv

BACKGROUND_COLOR = "#B1DDC6"
VOCABLE_SOURCE = "data/french_words.csv"
LEARN_SOURCE = "data/french_to_learn.csv"
FLIP_DELAY = 3000  # ms

try:
    with open(LEARN_SOURCE, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    with open(VOCABLE_SOURCE, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
current_voc = None

# ---------------------------- FUNCTIONS ------------------------------- #


def remove():
    """remove Card from Repeat list"""
    global data, current_voc
    data.remove(current_voc)
    with open(LEARN_SOURCE, "w", newline='') as new_f:
        writer = csv.writer(new_f)
        writer.writerows(data)
    fetch()


def fetch():
    """fetch new Card"""
    global current_voc, flip_timer, data
    screen.after_cancel(flip_timer)
    current_voc = data[random.randint(1, len(data)-1)]
    canvas.itemconfig(card_img, image=front_card_img)
    canvas.itemconfig(lng_txt, text=data[0][0], fill="black")         # e.g. spanish
    canvas.itemconfig(voc_txt, text=current_voc[0], fill="black")     # e.g. hola
    flip_timer = screen.after(FLIP_DELAY, flip)


def flip():
    """flip the card, so you see the solution"""
    canvas.itemconfig(card_img, image=back_card_img)
    canvas.itemconfig(lng_txt, text=data[0][1], fill="white")
    canvas.itemconfig(voc_txt, text=current_voc[1], fill="white")


# ---------------------------- UI SETUP ------------------------------- #

# Screen
screen = tkinter.Tk()
screen.title("Flash Cards")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = screen.after(FLIP_DELAY, flip)

# Canvas
canvas = tkinter.Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Card Image
front_card_img = tkinter.PhotoImage(file="images/card_front.png")
back_card_img = tkinter.PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_card_img)

# Card Text
lng_txt = canvas.create_text(400, 150, text="",  font=("Arial", 40, "italic"))
voc_txt = canvas.create_text(400, 263, text="",  font=("Arial", 60, "bold"))

# Red Button
red_img = tkinter.PhotoImage(file="images/wrong.png")
red_btn = tkinter.Button(image=red_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=fetch)
red_btn.grid(row=1, column=0)

# Green Button
green_img = tkinter.PhotoImage(file="images/right.png")
green_btn = tkinter.Button(image=green_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove)
green_btn.grid(row=1, column=1)


fetch()
screen.mainloop()
