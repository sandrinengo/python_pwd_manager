from tkinter import *
from tkinter import messagebox as msg_box
from random import randint, choice, shuffle

import pyperclip
#Functions


def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    txt_pwd.insert(0, password)
    pyperclip.copy(password)


def add_pwd():
    website = txt_website.get()
    email = txt_email.get()
    pwd = txt_pwd.get()
    is_okay = msg_box.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {pwd}\nIs it OK to save?")

    if is_okay:
        with open("data/data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {pwd}\n")
            clear_form()

def clear_form():
    txt_website.delete(0, END)
    txt_email.insert(0, "sandrinengo@yahoo.com")
    txt_pwd.delete(0)
    txt_website.focus()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
logo = PhotoImage(file="img/logo.png")
canvas.create_image(100, 100,image=logo)
canvas.grid(row=0, column=1)

#Label
lbl_website = Label(text="Website Name:")
lbl_website.grid(row=1, column=0)
lbl_email = Label(text="Email/Username:")
lbl_email.grid(row=2, column=0)
lbl_pwd = Label(text="Password:")
lbl_pwd.grid(row=3, column=0)

#Entries
txt_website = Entry(width=35)
txt_website.grid(row=1, column=1, columnspan=2)
txt_website.focus()
txt_email = Entry(width=35)
txt_email.grid(row=2, column=1, columnspan=2)
txt_email.insert(0, "sandrinengo@yahoo.com")
txt_pwd = Entry(width=20)
txt_pwd.grid(row=3, column=1)

#Buttons
btn_generate_pwd = Button(window, text="Generate Password", command=generate_pwd)
btn_generate_pwd.grid(row=3, column=2)
btn_add = Button(window, text="Add", width=30, command=add_pwd)
btn_add.grid(row=4, column=1,columnspan=2)





window.mainloop()