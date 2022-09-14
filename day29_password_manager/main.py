from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config (padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="./day29_password_manager/logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
email_entry = Entry(width=35)
password_entry = Entry(width=21)
window.mainloop()