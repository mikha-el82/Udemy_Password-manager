from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

DEFAULT_EMAIL = "somebody@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# from Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    generated_password = "".join(password_list)
    pwd_entry.delete(0, END)
    pwd_entry.insert(0, generated_password)

    window.clipboard_clear()
    window.clipboard_append(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    data = None
    website = website_entry.get()
    email = user_entry.get()
    password = pwd_entry.get()
    new_credentials = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error!", message="Please don't leave any field empty!")
    else:
        try:
            with open("passwords.json", "r") as passwords:
                # Reading the old data
                data = json.load(passwords)
            print(f"Data in file are: {data}")
            # Updating with new data
            data.update(new_credentials)
            print(f"Data are being updated with {new_credentials}.")
        except (json.decoder.JSONDecodeError, AttributeError):
            data = new_credentials
            print("No data in datafile.")
            print("or")
            print("Wrong data in existing datafile.")
        except FileNotFoundError:
            data = new_credentials
            print("No datafile. Creating new datafile.")

        finally:
            with open("passwords.json", "w") as passwords:
                # Saving updated/new data
                json.dump(data, passwords, indent=4)
                print("Dumping data in datafile.")

        website_entry.delete(0, END)
        user_entry.delete(0, END)
        user_entry.insert(0, DEFAULT_EMAIL)
        pwd_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    search_for = website_entry.get()
    if search_for == "":
        messagebox.showinfo(title="Error!", message="Please type in website name!")
    else:
        try:
            with open("passwords.json") as passwords:
                # search for website
                data = json.load(passwords)
        except FileNotFoundError:
            messagebox.showinfo(title="Error!", message="No Data File Found.")
        except json.decoder.JSONDecodeError:
            messagebox.showinfo(title="Error!", message="Data File Corrupted.")
        else:
            if search_for in data:
                email = data[search_for]["email"]
                pwd = data[search_for]["password"]
                messagebox.showinfo(title=search_for, message=f"Email:/Username: {email}\nPassword: {pwd}")
            else:
                messagebox.showinfo(title="Error!", message=f"No details for the website '{search_for}' exist.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_txt = Label(text="Website: ")
website_txt.grid(column=0, row=1, sticky="E")
user_txt = Label(text="Email/Username: ")
user_txt.grid(column=0, row=2, sticky="E")
pwd_txt = Label(text="Password: ")
pwd_txt.grid(column=0, row=3, sticky="E")

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, sticky="W")
website_entry.focus()
user_entry = Entry()
user_entry.insert(0, DEFAULT_EMAIL)
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
pwd_entry = Entry(width=35)
pwd_entry.grid(column=1, row=3, sticky="W")

search_btn = Button(text="Search", width=14, command=find_password)
search_btn.grid(column=2, row=1, sticky="E")
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="E")
add_btn = Button(text="Add", width=30, command=add_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
