from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_field.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    user_website = website_input.get()
    user_email_username = email_username_input.get()
    user_password = password_field.get()

    if (len(user_website) == 0 or
        len(user_email_username) == 0 or
        len(user_password) == 0):
        messagebox.showerror(title="Oops!", message="Please do not leave any of the fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=user_website, message=f"These are the details entered:"
                                                       f"\nWebsite: {user_website}"
                                                       f"\nEmail: {user_email_username}"
                                                       f"\nPassword: {user_password}")

        if is_ok:
            with open("passwords.txt", "a") as passwords_file:
                passwords_file.write(f"{user_website} | {user_email_username} | {user_password}\n")
                messagebox.showinfo(title="Password saved!", message="Your new password was copied to clipboard as well!")

    website_input.delete(0, END)
    password_field.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= logo_img)
canvas.grid(column=1,row=0)

website_label = Label(text = "Website")
website_label.grid(column=0,row=1)

email_username_label = Label(text = "Email/Username")
email_username_label.grid(column=0,row=2)

passwd_label = Label(text = "Password")
passwd_label.grid(column=0,row=3)

website_input = Entry()
website_input.focus()
website_input.config(width=42, highlightthickness=0)
website_input.grid(column=1,row=1, columnspan=2)

email_username_input = Entry()
email_username_input.config(width=42, highlightthickness=0)
email_username_input.grid(column=1,row=2, columnspan=2)

password_field = Entry()
password_field.config(width=33, highlightthickness=0)
password_field.grid(column=1,row=3)

generate_password_button = Button(text="Generate", command=generate_passwd, highlightthickness=0)
generate_password_button.grid(column=2,row=3)

add_button = Button(text="Add", command=save, highlightthickness=0)
add_button.config(width=36)
add_button.grid(column=1,row=4, columnspan=2)

window.mainloop()