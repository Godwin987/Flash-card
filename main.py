from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT_SIZE = 25
QUESTION_FONT_SIZE = 50

window = Tk()
width = window.winfo_screenwidth()
spacer = (" " * (int(width//11)))
window.title(spacer+"Flashyy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
to_learn = {}

# ------------------------ FUNCTIONALITY --------------------- #

def card_flip():
    canvas.delete(image)
    image2 = canvas.create_image(400, 263, image=card_back_image)
    engligh_language = canvas.create_text(350, 100, text="English", fill="white", font=("Arial", LANGUAGE_FONT_SIZE, "italic"))
    answer = canvas.create_text(350, 300, text=english_list[question], fill="white", font=("Arial", QUESTION_FONT_SIZE, "bold"))

def card_flip2():
    canvas.delete(image)
    image2 = canvas.create_image(400, 263, image=card_front_image)
    engligh_language = canvas.create_text(350, 100, text="French", fill="black", font=("Arial", LANGUAGE_FONT_SIZE, "italic"))
    answer = canvas.create_text(350, 300, text=french_list[question], fill="black", font=("Arial", QUESTION_FONT_SIZE, "bold"))

def right_answer_management():
    # french_question = random.randint(0, len(french_list) - 1)
    french_list.remove(french_list[question])
    english_list.remove(english_list[question])
    # new_question = random.randint(0, len(french_list) - 1)
    # canvas.itemconfig(question, text=french_list[new_question])
    card_flip2()
    window.after(3000, card_flip)
    # data = pandas.DataFrame(words_dataframe)
    # data.to_csv("./data/words_to_learn.csv")

def wrong_answer_management():
    # french_question = random.randint(0, len(french_list) - 1)
    # canvas.itemconfig(question, text=french_list[question])
    global question
    question = generate_question()
    card_flip2()
    window.after(3000, card_flip)

# ------------------------ FILE MANAGEMENT AND QUESTIONS DISPLAY -----------------  #


words_dataframe = pandas.read_csv("./data/french_words.csv")
french_list = words_dataframe["French"].to_list()
english_list = words_dataframe["English"].to_list()

def generate_question():
    question_index = random.randint(0, len(french_list)-1)
    return question_index


question = generate_question()
# ------------------------ UI SETUP ----------------------------- #

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="./images/card_back.png")
card_front_image = PhotoImage(file="./images/card_front.png")
image = canvas.create_image(400, 263, image=card_front_image)
language = canvas.create_text(350, 100, text="French", fill="black", font=("Arial", LANGUAGE_FONT_SIZE, "italic"))
question = canvas.create_text(350, 300, text=french_list[question], fill="black", font=("Arial", QUESTION_FONT_SIZE, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# ------------------------ BUTTONS -------------------------------#
right_button_image = PhotoImage(file="./images/right.png")
right = Button(height=100, width=100, command=right_answer_management, image=right_button_image,
               borderwidth=0, highlightthickness=0)
right.grid(row=1, column=0, sticky=W, padx=90)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong = Button(height=99, width=100, command=wrong_answer_management, image=wrong_button_image,
               borderwidth=0, highlightthickness=0)
wrong.grid(row=1, column=1, sticky=E, padx=90)

window.after(3000, card_flip)

window.mainloop()
