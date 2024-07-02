from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_new_password():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")

    else:
        try:
            with open("data.json", "r") as data:
                # reading the old data
                json_data = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            with open("data.json", "w") as data:
                # updating old data
                json_data.update(new_data)
                # saving updated data
                json.dump(json_data, data, indent=4)
        finally:
            clear_fields()


def clear_fields():
    website_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data:
            json_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in json_data:
            email = json_data[website]["email"]
            password = json_data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website}.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# lock image
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# website entry box
website_input = Entry(width=18)
website_input.grid(column=1, row=1)
website_input.focus()

# search password button
search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2, row=1)

# email/username label
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

# email/username entry box
email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "example@email.com")

# password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# password entry box
password_input = Entry(width=18)
password_input.grid(column=1, row=3)

# generate password button
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", command=add_new_password, width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
