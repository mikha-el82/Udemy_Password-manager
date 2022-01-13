from tkinter import *

DEFAULT_EMAIL = "somebody@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_entry.get()
    email = user_entry.get()
    password = pwd_entry.get()
    with open("passwords.txt", "a") as passwords:
        passwords.write(f"{website} | {email} | {password}\n")
    website_entry.delete(0, END)
    user_entry.delete(0, END)
    user_entry.insert(0, DEFAULT_EMAIL)
    pwd_entry.delete(0, END)


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
website_txt.grid(column=0, row=1)
user_txt = Label(text="Email/Username: ")
user_txt.grid(column=0, row=2)
pwd_txt = Label(text="Password: ")
pwd_txt.grid(column=0, row=3)

# Entries
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
user_entry = Entry(width=50)
user_entry.insert(0, DEFAULT_EMAIL)
user_entry.grid(column=1, row=2, columnspan=2)
pwd_entry = Entry(width=32)
pwd_entry.grid(column=1, row=3)

generate_btn = Button(text="Generate Password")
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=43, command=add_password)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()
