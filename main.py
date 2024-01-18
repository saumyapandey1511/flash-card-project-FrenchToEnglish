from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
dict ={}

try:
    data_fr= pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data =pandas.read_csv("./data/french_words.csv")
    dict = original_data.to_dict(orient="records")
else:
    dict=data_fr.to_dict(orient="records")



def choose_word_fr():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,text=current_card['French'],fill="black")
    canvas.itemconfig(image,image=card_front_image)
    flip_timer=window.after(3000,choose_word_en)


def choose_word_en():
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=current_card['English'],fill="white")
    canvas.itemconfig(image, image=card_back_image)

def is_known():
    dict.remove(current_card)
    print(len(dict))
    choose_word_fr()
    data_fr = pandas.DataFrame(dict)
    data_fr.to_csv("data/words_to_learn.csv",index=False)



window =Tk()
window.title('Flashy')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR,width=1000,height=700)

flip_timer=window.after(3000,choose_word_en)

canvas =Canvas(width=800,height=526)
card_front_image =PhotoImage(file="images/card_front.png")
card_back_image =PhotoImage(file="images/card_back.png")
image=canvas.create_image(400,263,image=card_front_image)
title=canvas.create_text(400,150, text="Title",font=("Ariel",40,"italic"))
word=canvas.create_text(400,263, text="word",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

x_image =PhotoImage(file="images/wrong.png")
x_button=Button(image=x_image,bg=BACKGROUND_COLOR,command=choose_word_fr)
x_button.grid(column=0,row=1,sticky="EW")

tick_image =PhotoImage(file="images/right.png")
tick_button=Button(image=tick_image,bg=BACKGROUND_COLOR,command=is_known)
tick_button.grid(column=1,row=1,sticky="EW")





# choose_word_en()
# window.after_cancel()
choose_word_fr()
window.mainloop()