from tkinter import *
import pandas as pd
import random

#----------------------Word engine-------------------
current_card = {}
lexico = {}


try:
    data_lexico_raw = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data_lexico_raw = pd.read_csv("data/french_words.csv")
    lexico = original_data_lexico_raw.to_dict(orient="records")
else:
    lexico = data_lexico_raw.to_dict(orient="records")


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(lexico)
    canvas.itemconfig(card_title, text="French", fill = "black")
    canvas.itemconfig(card_word, text=current_card["French"], fill ="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill = "white")
    canvas.itemconfig(card_word, text=current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image=card_back_image)

def already_known ():

    lexico.remove(current_card)
    data = pd.DataFrame(lexico)
    data.to_csv("data/word_to_learn.csv", index=False)
    next_word()

    if len(lexico) == 0:
        window.after_cancel(flip_timer)
        canvas.itemconfig(card_title, text="You've completed the dictionary!!!", fill="black")
        canvas.itemconfig(card_word, text="Congratulations!!!", fill="black")
        canvas.itemconfig(card_background, image=card_front_image)





#----------------------------User Interface---------------------------
window = Tk()
window.title("Flash cards!!")
window.config(width=800, height=526, bg="#B1DDC6", padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(410,270, image=card_front_image)
card_title = canvas.create_text(400,150,text="French",font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="Salut!",font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

button_check_image = PhotoImage(file="images/right.png")
button_right = Button(image=button_check_image, highlightthickness=0, command=already_known)
button_right.grid(column=1, row=1)

button_cross_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=button_cross_image, highlightthickness=0, command=next_word)
button_wrong.grid(column=0, row=1)

next_word()















window.mainloop()