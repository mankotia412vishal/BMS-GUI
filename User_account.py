import tkinter as tk
import mysql.connector
# from mysql.connector import connect,Error
from tkinter import *

def create_user_account():
    query1 = "INSERT INTO user_account VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
 

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vishal123",
        database="project_dbms"
    )

    mycursor = mydb.cursor()

    root = Tk()
    # making Full screen as Default
    root.attributes("-fullscreen", True)
    # Title of the window
    root.title('Create User Account')

    # add widgets here
    # Heading Configurations
    hed = Label(root, text="Create User Account", bg="#4361ee",
                fg="#e9ecef", font="Times 60 underline bold")
    # placing the widget on the screen
    hed.pack(fill=X)


    # Creating the Grid for the Entries

    # Creating the name Frame
    base_frame = Frame(root, bg="#4cc9f0")

    name_label = Label(base_frame, text="Name:", bg="#023047",
                    fg="#ced4da", font='Times 30 bold', width=12)
    name_label.grid(row=0, column=0, padx=5, pady=(5, 30))

    name_entry = Entry(base_frame, font='Times 30 bold',
                    width=10, bg='#023047', fg='#ced4da')
    name_entry.grid(row=0, column=1, padx=(0, 100), pady=(5, 30))


    # Creating the Address Frame

    Address_label = Label(base_frame, text="Address:",
                        bg="#023047", fg="#ced4da", font='Times 30 bold', width=11)
    Address_label.grid(row=0, column=2, padx=(100, 5), pady=(5, 30))

    Address_entry = Entry(base_frame, font='Times 30 bold',
                        width=10, bg='#023047', fg='#ced4da')
    Address_entry.grid(row=0, column=3, pady=(5, 30), padx=(0, 5))

    # Creating the DOB Frame

    dob_label = Label(base_frame, text="DOB:",
                    bg="#023047", fg="#ced4da", font='Times 30 bold', width=12)
    dob_label.grid(row=1, column=0, padx=5, pady=(5, 30))

    dob_entry = Entry(base_frame, font='Times 30 bold',
                    width=10, bg='#023047', fg='#ced4da')
    dob_entry.grid(row=1, column=1, padx=(0, 100), pady=(5, 30))

    # Creating the Account NO Frame
    Account_no_label = Label(base_frame, text="Account No:",
                            bg="#023047", fg="#ced4da", font='Times 30 bold', width=11)
    Account_no_label.grid(row=1, column=2, padx=(100, 5), pady=(5, 30))

    Account_no_entry = Entry(base_frame, font='Times 30 bold',
                            width=10, bg='#023047', fg='#ced4da')
    Account_no_entry.grid(row=1, column=3, pady=(5, 30), padx=(0, 5))


    # Creating the Contact Frame
    Contact_label = Label(base_frame, text="Contact:", bg="#023047",
                        fg="#ced4da", font='Times 30 bold', width=12)
    Contact_label.grid(row=2, column=0, padx=5, pady=(5, 30))

    Contact_entry = Entry(base_frame, font='Times 30 bold',
                        width=10, bg='#023047', fg='#ced4da')
    Contact_entry.grid(row=2, column=1, padx=(0, 100), pady=(5, 30))


    # Creating the Aadhar Frame
    Aadhar_label = Label(base_frame, text="Aadhar:",
                        bg="#023047", fg="#ced4da", font='Times 30 bold', width=11)
    Aadhar_label.grid(row=2, column=2, padx=(100, 5), pady=(5, 30))

    Aadhar_entry = Entry(base_frame, font='Times 30 bold',
                        width=10, bg='#023047', fg='#ced4da')
    Aadhar_entry.grid(row=2, column=3, pady=(5, 30), padx=(0, 5))

    # Creating the Gender Frame
    Gender_label = Label(base_frame, text="Gender(M/F/O):", bg="#023047",
                        fg="#ced4da", font='Times 30 bold', width=12)
    Gender_label.grid(row=3, column=0, padx=5, pady=(5, 5))

    Gender_entry = Entry(base_frame, font='Times 30 bold',
                        width=10, bg='#023047', fg='#ced4da')
    Gender_entry.grid(row=3, column=1, padx=(0, 100), pady=(5, 5))


    # Creating the Account_Type Frame
    Account_Type_label = Label(base_frame, text="Account_Type:",
                            bg="#023047", fg="#ced4da", font='Times 30 bold', width=11)
    Account_Type_label.grid(row=3, column=2, padx=(100, 5), pady=(5, 5))

    Account_Type_entry = Entry(base_frame, font='Times 30 bold',
                            width=10, bg='#023047', fg='#ced4da')
    Account_Type_entry.grid(row=3, column=3, pady=(5, 5), padx=(0, 5))


    # Funtion for on click
    def fetch_value():
        name = name_entry.get()
        address = Address_entry.get()
        dob = dob_entry.get()
        account_no = int(Account_no_entry.get())
        contact = int(Contact_entry.get())
        aadhar = int(Aadhar_entry.get())
        gender = Gender_entry.get()
        account_type = Account_Type_entry.get()

        data = (name,account_no,gender,aadhar,dob,address,account_type,contact)
        mycursor.execute(query1, data)
        mydb.commit()
        root.destroy()


    # Placing the Element Frame on to the Screen
    base_frame.pack(pady=(65, 50))

    # Adding Button to submit data
    submit = Button(root,
                    bg="#4361ee", fg="#e9ecef",
                    text='Create Account',
                    anchor=CENTER,
                    font='Times 25 bold',
                    justify=CENTER,
                    activebackground="#e9ecef",
                    activeforeground="#4361ee",
                    height=2,
                    bd=5,
                    width=25,
                    command = fetch_value
                    )

    submit.pack()
    # Adding an event to the Esc button for program termination
    root.bind("<Escape>", lambda event: root.destroy())


    # configuring the base window background
    root.configure(bg="#4cc9f0")

    # Termination of the Tkinter Process
    mainloop()

def call_function():
    
    create_user_account()
