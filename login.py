from gui import *
import gui
from tkinter import *
import os
def login_session():
    print("xcvbnm,.")
    print(os.listdir())
    print(temp_login_name.get())
    global login_name
    global account_dashboard
    login_name=temp_login_name.get()
    if temp_login_name.get() in (os.listdir()):
        file=open(temp_login_name.get(),"r")
        details=[line.rstrip() for line in file.readlines()]
        print(details)
        print(type(details[4]))

        if details[1]==temp_password.get():
            login_notif.config(fg="red",text = "Congrats Login Successfull...")
            login_screen.destroy()
            #ACCOUNT DASHBOARD
            account_dashboard=Toplevel(gui.root)
            account_dashboard.title("Dashboard")
            acc_label1=Label(account_dashboard,text="Account Dashboard",font=("calibri",15))
            acc_label2=Label(account_dashboard,text=f"Welcome Mr/Ms {temp_login_name.get()}")
            details_button=Button(account_dashboard,text="Personal info",width=20,command=personal_info)
            deposit_button=Button(account_dashboard,text="Deposit",width=20,command=deposit)
            withdrawl_button=Button(account_dashboard,text="Withdrawl",width=20,command=withdraw)


            acc_label1.grid(row=0,sticky=N)
            acc_label2.grid(row=1,sticky=N)
            details_button.grid(row=4,sticky=N,padx=10,pady=5)
            deposit_button.grid(row=6,sticky=N)
            withdrawl_button.grid(row=8,sticky=N,padx=10,pady=5)

        else:
            login_notif.config(fg="red",text = "The password you entered is wrong...")

            print(f"Wrong passsword The correct password is {details[1]}and the typed password is {temp_password.get()}")
    else:
        login_notif.config(fg="red", text="The user name was not found in our database")

        print("Not found")
def deposit():

    global deposit_amnt
    deposit_amnt=StringVar()

    file = open(temp_login_name.get(), "r")
    details = [line.rstrip() for line in file.readlines()]
    details_balance=details[3]
    deposit_screen = Toplevel(account_dashboard)
    deposit_screen.title("Deposit")
    deposit_label1 = Label(deposit_screen, text="Enter the amount you want to deposit..", font=("calibri", 15))
    e_deposit=Entry(deposit_screen,textvariable=deposit_amnt)



    def deposit_finish():
        file=open(temp_login_name.get(),'r+')
        file_data=file.read()
        details=file_data.split('\n')
        current_bal=details[4]
        new_bal=float(current_bal)+float(deposit_amnt.get())
        print(new_bal)
        file_data=file_data.replace(current_bal,str(new_bal))
        file.seek(0)
        file.truncate(0)
        file.write(file_data)
        file.close()
        a = deposit_amnt.get()
        print("A is ....", a)
        print("sdfghjmk", deposit_amnt.get())
        # if deposit_amnt.isdigit():
        #     in_deposit_amnt=int(deposit_amnt)
        #     print(in_deposit_amnt)
        # else:
        #     print("Enter a valid amount")
        #     # print(f"{deposit_amnt} is not a valid one")
        # print(type(deposit_amnt))
        print(type(new_bal))
        # c=int(deposit_amnt)
        # d=int(new_bal)
        # print(type(d))
        # print(type(c))
        #
        new_bal=float(new_bal)
        new_bal+=float(deposit_amnt.get())
        # current_bal=int(details[3])
        # current_bal+= deposit_amnt
        # new_file = open(temp_login_name.get(), "w")
        #
        # # print(type(int(deposit_amnt)))
        # print(f"Your new balance is {details[3]}")
    deposit_button=Button(deposit_screen,text="Continue",command=deposit_finish)




    deposit_label1.grid(row=1, sticky=W)
    deposit_button.grid(row=4, sticky=W)
    # deposit_label3.grid(row=8, sticky=W)
    e_deposit.grid(row=12,sticky=N)
def withdraw():
    pass
def personal_info():
    # VAR
    file = open(temp_login_name.get(), "r")
    details = [line.rstrip() for line in file.readlines()]
    details_name=details[0]
    details_age=details[1]
    details_gender=details[2]
    personal_screen=Toplevel(account_dashboard)
    personal_screen.title("Personal information")
    personal_label1 = Label(personal_screen, text=f"Name   : {details_name}", font=("calibri", 15))
    personal_label2 = Label(personal_screen, text=f"age    : {details_age}", font=("calibri", 15))
    personal_label3 = Label(personal_screen, text=f"gender : {details_gender}", font=("calibri", 15))
    personal_label1.grid(row=1,sticky=W)
    personal_label2.grid(row=4,sticky=W)
    personal_label3.grid(row=8,sticky=W)


def login():
    global temp_login_name
    global temp_password
    global login_notif
    temp_login_name=StringVar()
    temp_password=StringVar()
    global login_screen
    login_screen = Toplevel(gui.root)
    login_screen.title("Login..")
    login_label1 = Label(login_screen, text="  Welcome to NIBK..login to continue", font=('Calibri', 20))
    login_label2=Label(login_screen, text="User Name")
    login_label3=Label(login_screen, text="Password")
    login_notif = Label(login_screen, fg="red",font=("Arial", 15))


    # ENtry
    e_login_name=Entry(login_screen,textvariable=temp_login_name)
    e_login_password=Entry(login_screen,textvariable=temp_password, show ="*")
    # Button
    log_button=Button(login_screen,text="Login",bg="green",fg="blue",command=login_session,width=15)

    login_label1.grid(row=0,sticky="N")
    login_label2.grid(row=1,sticky='W')
    login_label3.grid(row=2,sticky='W')
    login_notif.grid(row=4,sticky=N)


    e_login_name.grid(row=1, sticky=E, padx=10,pady=10)
    e_login_password.grid(row=2,sticky=E,padx=10,pady=10)
    log_button.grid(row=3,sticky=N)
