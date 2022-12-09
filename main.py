from tkinter import *
from PIL import Image, ImageTk
import csv
import random
window = Tk()
BACKGROUND_COLOR = "#B1DDC6"
window.title("Flashy")
window.config(pady=50, padx=50)
canvas = Canvas(window, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=1, column=1, columnspan=2)
front_img = ImageTk.PhotoImage(Image.open(r'images\card_front.png'))
back_img = ImageTk.PhotoImage(Image.open(r'images\card_back.png'))
right_img = PhotoImage(file=r'images\right.png')
wrong_img = PhotoImage(file=r'images\wrong.png')
LANG_FONT = ('Ariel', '40', 'italic')
MAIN_WORD_FONT = ('Ariel', '60', 'bold')
all_words = list()
with open("data/chinese_words.csv", 'r',encoding='UTF-8') as file:
    csvreader = csv.reader(file)
    next(csvreader)
    for row in csvreader:
        all_words.append(row)
def get_random_word():
    return random.choice(all_words)
word = get_random_word()
def show_word(word):
    flip_cards(image=front_img, text="Russian", fill_color="black", translate_word=word[1], tags="russian_word")
    window.after(3000, lambda: (canvas.delete('russian_word'), flip_cards(translate_word=word[0])))
def delete_from_file(word):
    all_words.remove(word)
    with open('data/words_to_learn.csv', 'w', newline='',encoding='utf8') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(all_words)
def next_word():
    global word
    prev_word = word
    delete_from_file(prev_word)
    print(prev_word)
    word=get_random_word()
    show_word(word)
def skip():
    global word
    word = get_random_word()
    show_word(word)
    print(word)
def flip_cards(text="English", anchor=NW, image=back_img, translate_word='', img_coordiante=10, x_axis=400, y_axis=263,
               fill_color="white", tags="english_word"):
    canvas.create_image(img_coordiante, img_coordiante, anchor=anchor, image=image),
    canvas.create_text(x_axis, y_axis, text=translate_word, font=MAIN_WORD_FONT, fill=fill_color, tags=tags),
    canvas.create_text(x_axis, y_axis - 113, text=text, font=LANG_FONT, fill=fill_color, tags=tags)
skip()
right_btn = Button(image=right_img, highlightthickness=0, borderwidth=0, command=next_word).grid(row=2, column=2)
wrong_btn = Button(image=wrong_img, highlightthickness=0, borderwidth=0,command=skip).grid(row=2, column=1)
window['bg'] = BACKGROUND_COLOR
window.mainloop()