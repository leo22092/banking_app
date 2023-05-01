from tkinter import *
import os
import PIL
from PIL import ImageTk, Image
from login import login
root = Tk()
root.title("Soft Bank")

img = Image.open('bank.jpg')
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)
mylabel1 = Label(root, text="North Indian BAnk of Kerala", font=('Calibri', 20))
mylabel2 = Label(root, text="Affordable Banking For all", font=('Calibri', 10))
im1label = Label(root, image=img)


mylabel1.grid(row=0, sticky=N, pady=10, padx=10)
mylabel2.grid(row=1, sticky=N)
im1label.grid(row=2, sticky=N, pady=15, padx=10)


def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    #     User needs to fill all fields befor registering
    if name == "" or age == "" or gender == "" or password == "":
        register_notif.config(fg="red",text = "ALERT!! All fields are mandatory")
        return
    else:
        if name in all_accounts:
            print(f"{name } is already a registered user ")
            register_notif.config(fg="red", text="ALERT!! Account in this name already exists")
            return
        else:
            new_file = open(name, "w")
            new_file.write(name + '\n')
            new_file.write(password + '\n')
            new_file.write(age + '\n')
            new_file.write(gender + '\n')
            new_file.write("0")
            new_file.write("\n END")
            new_file.close()
            register_notif.config(fg="blue", text="Your account has been created successfully")
            print("Successfully registered!!!")
            register_notif.config(fg="blue", text="Successfully registered...")



def register():
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global register_notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    register_screen = Toplevel(root)
    register_screen.title("Registration")
    register_label_1 = Label(register_screen, text="Welcome to the North indian Bank of Kerala Registration Screen")
    register_label_2 = Label(register_screen, text="Please enter your details below..")
    register_label_3 = Label(register_screen, text=" Name", font=("Arial", 12))
    register_label_4 = Label(register_screen, text=" Age ", font=("Arial", 12))
    register_label_5 = Label(register_screen, text=" Gender", font=("Arial", 12))
    register_label_6 = Label(register_screen, text=" Password ", font=("Arial", 12))
    register_notif = Label(register_screen, fg="red",font=("Arial", 15))
    # Entries

    entry_name = Entry(register_screen, textvariable=temp_name)
    entry_age = Entry(register_screen, textvariable=temp_age)
    entry_gender = Entry(register_screen, textvariable=temp_gender)
    entry_password = Entry(register_screen, textvariable=temp_password, show="*")

    # Entries
    entry_name.grid(row=3, sticky=E, pady=10)
    entry_age.grid(row=4, sticky=E, pady=10)
    entry_gender.grid(row=5, sticky=E, pady=10)
    entry_password.grid(row=6, sticky=E, pady=10)

    register_label_1.grid(row=0, sticky=W, pady=10)
    register_label_2.grid(row=2, sticky=W, pady=10)
    register_label_3.grid(row=3, sticky=W, pady=10)
    register_label_4.grid(row=4, sticky=W, pady=10)
    register_label_5.grid(row=5, sticky=W, pady=10)
    register_label_6.grid(row=6, sticky=W, pady=10)
    register_notif.grid(row=8, sticky=W, pady=10)

    # Button
    reg_button = Button(register_screen, text="Register", command=finish_reg, bg='green')
    reg_button.grid(row=7, sticky=N, padx=10, pady=10)


# def login():
#     pass


button1 = Button(root, text='Registraion', font=('Arial', 15), width=20, command=register)
button2 = Button(root, text='Login', font=('Arial', 15), width=20, command=login)

button1.grid(row=3, sticky=N)
button2.grid(row=4, sticky=N)

root.mainloop()
