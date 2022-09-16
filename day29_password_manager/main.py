import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """generate random password with letters, numbers and symbols"""
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
    """saving entry to JSON file when save button is pressed"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password" : password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please check entry! Empty fields.")
    else:
        is_ok = messagebox.askokcancel(title="User info for "+website, message=f"Email: {email}\nPassword: {password}\nProceed to save?")
        if is_ok: 
            try:
                with open("./day29_password_manager/data.json","r") as data_file:
                    pass
            except FileNotFoundError:
                #if file not found/does not exist - create it
                with open("./day29_password_manager/data.json","w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #if file exists - append new data    
                with open("./day29_password_manager/data.json","r") as data_file:
                    #JSON requires 3 step approach to append new data
                    #1.reading old data
                    data = json.load(data_file)
                    #2.update old with new data
                    data.update(new_data)
                with open("./day29_password_manager/data.json","w") as data_file:
                    #3.save data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
def search():
    """search through the password database when button seach is pressed"""
    website = website_entry.get()
    try:
        with open("./day29_password_manager/data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="JSON file not found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Website found!", message=f"Email: {email}\nPassword: {password}")
            email_entry.insert(0,data[website]['email'])
            password_entry.insert(0,data[website]['password'])
            pyperclip.copy(data[website]['password'])
        else:
            messagebox.showinfo(title="Error", message=f"Website: {website} not found.")

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config (padx=20, pady=20)

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
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
#set cursor into website entry on start
website_entry.focus()
email_entry = tk.Entry(width=57)
email_entry.grid(row=2, column=1, columnspan=2, sticky=tk.W, padx=5, pady=5)
password_entry = tk.Entry(width=35)
password_entry.grid(row=3,column=1, sticky=tk.W, padx=5, pady=5)

#buttons
search_button = tk.Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2, sticky=tk.W, padx=0, pady=5)
generate_password_button = tk.Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky=tk.W, padx=0, pady=5)
add_button = tk.Button(text="Add", width=50, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=tk.W, padx=5, pady=5)

window.mainloop()