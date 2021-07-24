import tkinter as tk
import random as r
words = "words to scramble"
other_words = "more words to scramble"
x = r.randrange(1,2)

root = tk.Tk()







w = 700
h = 800

canvas = tk.Canvas(root, height=h, width=w)
canvas.pack()

frame = tk.Frame(root, bg="#f2f2f2", bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")
frame_2 = tk.Frame(root, bg="#f2f2f2", bd=10)
frame_2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=('Arial', 22))
entry.place(relwidth=0.65, relheight=1)

label = tk.Label(frame_2, font=('Arial', 22))
label.place(relwidth=1, relheight=1)


def word_gen():
  if x == 1 :
    word_list = words.split()
  elif x == 2 :
    word_list = other_words.split()  
  out = " "
  new_list = word_list.copy()
  for word in word_list :
    word_to_print = r.choice(new_list) 
    out = out + word_to_print + " " 
    new_list.remove(word_to_print)

  label['text']  = out

def check(answer):
  if answer == words and x == 1:
    #
    zzz= "correct"
  elif answer == other_words and x == 2 :
    zzz="correct"
  else :
    zzz="incorrect"
  label['text']  = zzz
  

Button = tk.Button(frame, text="check", fg='blue', font=('Arial', 10), command=lambda: check(entry.get()))
Button.place(relx=0.7, rely=0.3, relheight=1)
word_gen()
root.mainloop()
