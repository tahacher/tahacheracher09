import num2words as n2w
from tkinter import *

def num_to_words():
    try:
        given_num = float(num.get())
        num_in_word = n2w.num2words(given_num)
        display.config(text=str(num_in_word).capitalize())
    except ValueError:
        display.config(text="Please enter a valid number.")

# Setup window
root = Tk()
root.title("Numbers to Words")
root.geometry("650x400")

# StringVar for entry
num = StringVar()

# Title label
title = Label(root, text="Number to Words converter", fg="Blue", font=("Arial", 20, 'bold'))
title.place(x=220, y=10)

# Supported formats labels
formats_label = Label(root, text="Formats supported:", fg="green", font=("Arial", 10, 'bold'))
formats_label.place(x=100, y=70)

pos_format_label = Label(root, text="1. Positives", fg="green", font=("Arial", 10, 'bold'))
pos_format_label.place(x=200, y=90)

neg_format_label = Label(root, text="2. Negatives", fg="green", font=("Arial", 10, 'bold'))
neg_format_label.place(x=200, y=110)

zero_format_label = Label(root, text="3. Zeros", fg="green", font=("Arial", 10, 'bold'))
zero_format_label.place(x=200, y=130)

float_format_label = Label(root, text="4. Floating points/decimals/fractions", fg="green", font=("Arial", 10, 'bold'))
float_format_label.place(x=200, y=150)

# Entry label and field
num_entry_label = Label(root, text="Enter a number:", fg="Blue", font=("Arial", 15, 'bold'))
num_entry_label.place(x=50, y=200)

num_entry = Entry(root, textvariable=num, width=30)
num_entry.place(x=220, y=200)

# Button to trigger conversion
btn = Button(root, text="Calculate", fg="green", font=("Arial", 10, 'bold'), command=num_to_words)
btn.place(x=280, y=230)

# Output display label
display = Label(root, text="", fg="black", font=("Arial", 10, 'bold'))
display.place(x=10, y=300)

# Try setting window icon (optional)
try:
    photo = PhotoImage(file="Num2Words/number.png")
    root.iconphoto(False, photo)
except Exception as e:
    print("Icon not set:", e)

# Run the GUI
root.mainloop()
