from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card ={}
to_learn = {}
# ---------------------------- Load Data from file  --------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------- Get Next Flash Card --------------------------- #


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- Flip the  Flash Card --------------------------- #


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ---------------------------- Save Progress --------------------------- #
def is_known():
    to_learn.remove(current_card)
    save_data = pandas.DataFrame(to_learn)
    save_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

# flash card front
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# x button
x_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_img, command=next_card)
x_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
x_button.grid(column=0, row=1)

# check button
check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, command=is_known)
check_button.config(highlightthickness=0, bg=BACKGROUND_COLOR)
check_button.grid(column=1, row=1)

# loads initial word
next_card()
window.mainloop()