from tkinter import *   #imports JUST about everything except for MessageBoxes, etc.. (eveyrthing = classes, constants)
from tkinter import messagebox
import pyperclip
from random import choice, randint, shuffle   #just remove all the places that have 'random.'

#constants:
my_dummy_email = "test<3sKoalas@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Cleaner Code:
def generate_secure_password():
    from random import shuffle, randint, choice



    #Password Generator function:

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, string=password)

    pyperclip.copy(password)

    # print(f"Your new secure Generated Password is: {password}")
    # return password

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    get_website_url = website_entry.get()
    get_email_username = email_username_entry.get()
    get_password = password_entry.get()

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:  #if the 1st or 3rd box is empty, then give an error popup:
        messagebox.showerror(title="Oops", message="Please fill in ALL of the blanks before clicking the Add button!")
    else:   #if there's no fields empty, then move on to the Confirmation box:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"These are the details entered: \nWebsite: {get_website_url} \nEmail/Username: {get_email_username} \nPassword: {get_password} \nIs it okay to save?")  # if the user clicks cancel, then we need to be able to go BACK to edit the field details. We need to be able to receive the output from this Method call, which is going to be a Boolean. It's either True or False. (we add 'is_ok=' to the very front, like a variable)

        if is_ok:
            with open("data29_01.txt", mode="a") as data_file:    # OR data_file = open("data29_01.txt", mode="a"):  # data_file.close(), but our current code line, we do not have to use the .close() code bit afterwards.
                data_file.write(f"{get_website_url}, {get_email_username}, {get_password}\n")
                website_entry.delete(0, END)    #or (0, 'end')
                password_entry.delete(0, END)    #or (0, 'end')

# ---------------------------- UI SETUP ------------------------------- #


# Window Setup:
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Canvas Widget:
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(107, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Website label:
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

# Website Entry:
website_entry = Entry(width=52)
# website_entry.insert(END, string="Enter website URL here! ")
website_entry.grid(row=1, column=1, columnspan=2)    #columnspan=2 is a keyword argument.
website_entry.focus() #If you want to start the blinking cursor on the first Entry text box field, then you would get ahold of the website_entry and use a Method on it called: .focus() and you would place it right after the .grid() method, of the Entry block we want it to Only apply to.


#############

# Email/Username label:
email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

# Email/Username Entry:
email_username_entry = Entry(width=52)
email_username_entry.insert(END, my_dummy_email)
email_username_entry.grid(row=2, column=1, columnspan=2)

#############

# Password label:
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Password Entry:
password_entry = Entry(width=33)
# password_entry.insert(END, string="Enter your Password here, or --> ")
password_entry.grid(row=3, column=1)

# Generate Password button:
# def generate_secure_password():
    # email_username_entry = Entry(width=52)
    # email_username_entry.insert(END, my_dummy_email)
    # email_username_entry.grid(row=2, column=1, columnspan=2)
    # print(password)


generate_password_button = Button(text="Generate Password", command=generate_secure_password, width=15)
generate_password_button.grid(row=3, column=2, columnspan=2)


# Add button:
# def add_password_action():
#     print("Add Password Button was Clicked.")
    # save()

add_button = Button(text="Add", command=save, width=45)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()