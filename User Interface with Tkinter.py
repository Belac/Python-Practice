from tkinter import *
from random import *
w = Tk()

t = Label(w,text="Ratr",font=("Verdana", 40))
t.pack()

rates = ["bananas","oranges","apples","cherries","mango","passion fruit","avocado","strawberries","blueberries","peaches"]
rate = randint(0,(len(rates)-1))
pos = rates[rate]
def Submit():
    rate = randint(0,(len(rates)-1))
    pos = rates[rate]

def rateit():
    rater = ("How would you rate... ",pos,"?")
    r = Label(w,text=rater)
    r.pack()
    rating = Scale(w,orient=HORIZONTAL)
    rating.pack()
    submit = Button(w,text="Submit",command=Submit)
    submit.pack()

rateit()



w.mainloop()
