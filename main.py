import tkinter
from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    pass


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website: ")
website_label.grid(column=0, row=1)
website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(index=0,string="yasowant@live.com")

password_label = tkinter.Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = tkinter.Entry(width=17)
password_entry.grid(column=1, row=3)

generate_pass_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=30, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
