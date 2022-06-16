import tkinter as tk
from collections import Counter

root = tk.Tk()
root.title('Lab 10')
root.geometry('700x500')

my_text = tk.Text(root, height=16, width=60, font=("Helvetica", 13))
my_text.pack(pady=20)

def read_button():
    my_text.delete("1.0", "end")
    file = open("C:/Users/ardas/Desktop/Marvel.txt", "r")
    message = file.read()

    my_text.insert("end", message)
    file.close()

def calculate_button():
    my_text.delete("1.0", "end")
    file = open("C:/Users/ardas/Desktop/Marvel.txt", "r")
    calculation = Counter(file.read().split())
    my_text.insert("end", calculation)
    file.close()


button1 = tk.Button(root, text = "Read", command=read_button)
button1.place(x=250, y=425)
button1.config(height=3, width=10)

button2 = tk.Button(root, text="Calculate", command=calculate_button)
button2.place(x=400, y=425)
button2.config(height=3, width=10)

root.mainloop()