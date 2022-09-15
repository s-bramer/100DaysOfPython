import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing entry", message="Please check entry! Empty fields.")
        return
    is_ok = messagebox.askokcancel(title="User info for "+website, message=f"Email: {email}\nPassword: {password}\nProceed to save?")
    if is_ok: 
        with open("./day29_password_manager/data.txt","a") as data_file:
            data_file.write(f"{website},{email},{password}\n")
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
        
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config (padx=30, pady=30)

canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="./day29_password_manager/logo.png")
canvas.create_image(100,100, image=logo_img)

#configure the grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)
window.columnconfigure(2, weight=1)

canvas.grid(row=0,column=1, sticky=tk.S, padx=5, pady=5)

#labels
website_label = tk.Label(text="Website")
website_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
email_label = tk.Label(text="Email/Username")
email_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
password_label = tk.Label(text="Password")
password_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

#entries
website_entry = tk.Entry(width=55)
website_entry.grid(row=1, column=1, columnspan=2, sticky=tk.W, padx=5, pady=5)
#set cursor into website entry on start
website_entry.focus()
email_entry = tk.Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2, sticky=tk.W, padx=5, pady=5)
password_entry = tk.Entry(width=25)
password_entry.grid(row=3,column=1, sticky=tk.W, padx=5, pady=5)

#buttons
generate_password_button = tk.Button(text="Generate Password", width=16, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky=tk.W, padx=0, pady=5)
add_button = tk.Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=tk.W, padx=5, pady=5)

window.mainloop()