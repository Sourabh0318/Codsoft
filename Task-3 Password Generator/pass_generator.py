from tkinter import *

root = Tk()

root.title("Password Generator")
root.geometry("300x400")


def generate_password():
    import random
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = upper_case.lower()
    numbers = "1234567890"
    symbols = "/*-+!@#$%^&~"

    al = upper_case + lower_case + numbers + symbols

    length = length_box.get()
    try:
        length = int(length)
        password = "".join(random.sample(al, length))
        password_box.config(text=password)
    except:
        password_box.config(text="Invalid Input")


def clear():
    password = ""
    password_box.config(text=password)


password_box = Label(root, width=27, height=2, text="", font=("arial", 15), bg="#363062", fg="#EEF5FF")
password_box.pack(pady=30)


length_msg = Label(root, text="Enter the length of the Password below", font=("arial", 10))
length_msg.pack()


length_box = Entry(root, width=15, font=("arial",16))
length_box.pack(pady=10)


Button(root, text="Generate Password", bg="#001B79", fg="#fff", command=generate_password).place(x=60, y=200)
Button(root, text="Clear", bg="#001B79", fg="#fff", command=clear).place(x=200, y=200)

root.mainloop()
