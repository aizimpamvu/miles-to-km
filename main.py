from tkinter import *

window = Tk()

window.title("Miles to km Convertor")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)


# calculate function

def convertor():
    to_km = float(input.get()) * 1.609
    km_label.config(text=to_km)


# Label
input = Entry(width=10)
input.grid(column=1, row=0)
my_label = Label(text=" Miles", font=("Times new roman", 15,))
my_label.grid(column=2, row=0)

my_label_2 = Label(text=" is equal to", font=("Times new roman", 15,))
my_label_2.grid(column=0, row=1)

my_label_3 = Label(text=" Km", font=("Times new roman", 15,))
my_label_3.grid(column=2, row=1)

# Result
km_label = Label(text="0", font=("Times new roman", 15,))
km_label.grid(column=1, row=1)

# calculate button
button = Button(text="Calculate", command=convertor)
button.grid(column=1, row=3)

window.mainloop()
