import json
import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search_website():
    with open("data.json","r") as fileread:
        print(json.load(fileread))






# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(0, nr_letters)]
    password_list += [random.choice(symbols) for char in range(0, nr_symbols)]
    password_list += [random.choice(numbers) for char in range(0, nr_numbers)]
    print(password_list)
    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #     password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    if len(website_entry.get()) == 0:
        messagebox.showwarning(title="Website Data missing", message="Website Data missing")
    elif len(email_entry.get()) == 0:
        messagebox.showwarning(title="Email Data missing", message="Email Data missing")
    elif len(password_entry.get()) == 0:
        messagebox.showwarning(title="Password Data missing", message="Password Data missing")
    else:
        isok = messagebox.askyesno(title=website_entry.get(),
                                   message=f"Email: {email_entry.get()}\n Password:{password_entry.get()}\n Should we proceed?")
        if isok:
            datadict={
                website_entry.get() : {
                    "email" : email_entry.get(),
                    "pwd" : password_entry.get()
                }
            }
            with open("data.txt", mode="a") as file:
                file.writelines(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")


            try:
                with open("data.json", mode = "r") as filejson:
                     data = json.load(filejson)

            except FileNotFoundError:
                with open("data.json", mode="w") as filejson:
                    json.dump(datadict, filejson, indent=4)

            else:
                data.update(datadict)
                with open("data.json", mode="w") as filejson:
                    json.dump(data, filejson, indent=4)




            website_entry.delete(0, END)
            password_entry.delete(0, END)


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
website_entry = tkinter.Entry(width=17)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(index=0, string="yasowant@live.com")

password_label = tkinter.Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = tkinter.Entry(width=17)
password_entry.grid(column=1, row=3)

generate_pass_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=30, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tkinter.Button(text="Search", width=15, command=search_website)
search_button.grid(column=2, row=1)

window.mainloop()
