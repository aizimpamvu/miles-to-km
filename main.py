from tkinter import *



window = Tk()

window.title("Miles to km Convertor")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)


#Label
input= Entry(width=10)
input.grid(column=1, row=0)
my_label = Label(text=" Miles", font=("Times new roman", 15,))
my_label.grid(column=2, row=0)
my_label = Label(text=" Miles", font=("Times new roman", 15,))
my_label.grid(column=2, row=0)





window.mainloop()