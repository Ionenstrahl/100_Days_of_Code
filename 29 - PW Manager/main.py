import pyperclip
from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_pw():
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    pw_entry.delete(0, END)
    pw_entry.insert(0, f"{password}")

    pyperclip.copy(password)
    status_label.config(text=f"Strg + V = Password", fg="blue")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pw():
    website = website_entry.get()
    user = user_entry.get()
    pw = pw_entry.get()

    if website == "":
        status_label.config(text="Error: Website missing", fg="red")
    elif user == "":
        status_label.config(text="Error: User missing", fg="red")
    elif pw == "":
        status_label.config(text="Error: PW missing", fg="red")

    else:
        # messagebox.showinfo(title="Title", message="Message")
        is_ok = messagebox.askokcancel(title=website, message=f"User: {user}\nPW: {pw}\nis correct?")
        if is_ok:
            new_data = {
                website: {
                    "user": user,
                    "pw": pw,
                }
            }
            overwritten = False
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)
                    if list(new_data.keys())[0] in data:
                        overwritten = True
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump("", f)
                    data = new_data
            except AttributeError: # catched of data.json exists, but does not contain json data
                data = new_data
            finally:
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
                if overwritten:
                    status_label.config(text=f"Success: PW for {website} overwritten", fg="green")
                else:
                    status_label.config(text=f"Success: PW for {website} saved", fg="green")
                website_entry.delete(0, END)
                pw_entry.delete(0, END)

        else:
            status_label.config(text="Then try again", fg="blue")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_pw():
    website = website_entry.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            user = data[website]["user"]
            pw = data[website]["pw"]
    except FileNotFoundError:
        status_label.config(text="FileNotFoundError: data.json", fg="red")
    # bad habit, as if else is preferred. e.g. if website in data
    except KeyError as msg:
        status_label.config(text=f"KeyError: {msg} not found", fg="red")
    else:
        user_entry.delete(0, END)
        user_entry.insert(0, user)
        pw_entry.delete(0, END)
        pw_entry.insert(0, pw)
        status_label.config(text=f"Success: {website}-Credentials loaded", fg="green")

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
canvas = Canvas(height=200, width=200)
filename = PhotoImage(file="logo.png")
logo_image = canvas.create_image(100, 100, image=filename)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=34)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=10, command=search_pw)
search_button.grid(row=1, column=2)

# User
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
user_entry = Entry(width=48)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "MaxMustermann@gmail.com")

# Password
pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)
pw_entry = Entry(width=34)
pw_entry.grid(row=3, column=1)

pw_button = Button(text="Generate PW", width=10, command=gen_pw)
pw_button.grid(row=3, column=2)

# Save PW
add_button = Button(width=40, text="Save PW", command=save_pw)
add_button.grid(row=4, column=1, columnspan=2)

# Status
status_label = Label(text="")
status_label.grid(row=5, column=0, columnspan=3)

window.mainloop()