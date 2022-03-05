import tkinter
import turtle


window = tkinter.Tk()
window.title("km to miles (nobody is interested in)")
#window.minsize(width=400, height=150)
window.config(padx=10, pady=10)

# Label

km_label = tkinter.Label(text="km", font=("Arial", 10, "bold"))
#my_label.pack() # side = "left"
km_label.grid(row=0, column=2)
#my_label.config(padx=50, pady=50)

#km_label["text"] = "km"
#km_label.config(text="New Text")

ml_label = tkinter.Label(text="miles", font=("Arial", 10))
ml_label.grid(row=1, column=2)

ml_value = tkinter.Label(text="0", font=("Arial", 10, "bold"))
ml_value.grid(row=1, column=1)

eq_label = tkinter.Label(text="is equal to", font=("Arial", 10, "bold"))
eq_label.grid(row=1, column=0)

# Button


def button_clicked():
    ml_value["text"] = round(int(inp.get()) * 1.6) if inp.get().isdigit() else "42"


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

# Entry

inp = tkinter.Entry()
inp.grid(row=0, column=1)


window.mainloop()