from tkinter import *
from tkinter.font import Font

root = Tk()
# root.title is used to add the title of the app
root.title("To-Do-List")
# root.geometry is used to give the width and height of the workspace/app
root.geometry("500x500")

# Define fonts
my_font = Font(family="Times New Roman", size=30,weight="bold")

# to create afrom we frame method
my_frame = Frame(root)
my_frame.pack(pady=10)

# Created a Listbox
my_list = Listbox(my_frame,
                  font=my_font,
                  width=25,
                  height=5,
                  bg="#91A3B0",
                  fg="white",
                  bd=0,
                  highlightthickness=0,
                  selectbackground="#36454F",
                  activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

stuff = ["Walk a dog", "Learn Tkinter"]
for item in stuff:
    my_list.insert(END, item)

# Added Scroll bar
my_scroll = Scrollbar(my_frame)
my_scroll.pack(side=RIGHT, fill=BOTH)

# Add Scrollbar
my_list.config(yscrollcommand=my_scroll.set)
my_scroll.config(command=my_list.yview)

# create a entry box to add items to the list
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

# Create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)


def delete_item():
    my_list.delete(ANCHOR)


def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


# Add Some buttons
delete_button = Button(button_frame, text="Delete Item", command = delete_item)
add_button = Button(button_frame, text="Add Item", command = add_item)


delete_button.grid(row=0,column=0)
add_button.grid(row=0, column=1, padx=20)


# root.mainloop() is used to run the root in a loop until we close
root.mainloop()