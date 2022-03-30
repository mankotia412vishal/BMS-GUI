import tkinter as tk
import mysql.connector
import tkinter.font as tf

from tkinter import *


def search_user_account():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vishal123",
        database="project_dbms"
    )

    mycursor = mydb.cursor()

    root = Toplevel()
    # making Full screen as Default
    root.attributes("-fullscreen", True)
    # Title of the window
    root.title('Search User Account')

    # Flag vairable is for the function Trigger!
    temp = StringVar()
    temp.set('Waiting for user Response')
    
    
    def search_account():
        
        acc_no = int(account_entry.get())
        mycursor.execute("SELECT account_number FROM user_account")

        numb = mycursor.fetchall()
        numb_list = list(sum(numb, ()))

        if acc_no in numb_list:
            right_frame.config(bg = 'black')
            def clear_widget(e):
                name_label.destroy()
                aadhar_label.destroy()
                ac_no_label.destroy()
                ac_type_label.destroy()
                contact_label.destroy()
                gender_label.destroy()
                DOB_label.destroy()
                address_label.destroy()

                right_frame.config(bg = "#4cc9f0")
            temp.set('Account Found!')
            mycursor.execute(
                "SELECT * FROM user_account WHERE account_number = {}".format(acc_no))
            rec = mycursor.fetchall()
            rec_list = []
            rec_list = list(sum(rec, ()))
            account_entry.delete(0, 20)

            # text for the name
            name_label = Label(right_frame, text="Name:- {}".format(rec_list[0]),
                               bg="#ced4da", fg="#7209b7", font='Times 30 bold', anchor=W)
            name_label.pack(fill=X, pady=2, padx=2)

            # Date of Birth
            DOB_label = Label(right_frame, text="DOB:-  {}".format(str(rec_list[4])),
                              bg="#7209b7", fg="#ced4da", font='Times 30 bold', anchor=W)
            DOB_label.pack(fill=X, pady=2, padx=2)

            # Account number
            ac_no_label = Label(right_frame, text="A/C No:-  {}".format(rec_list[1]),
                                bg="#ced4da", fg="#7209b7", font='Times 30 bold', anchor=W)
            ac_no_label.pack(fill=X, pady=2, padx=2)

            # Contact Number
            contact_label = Label(right_frame, text="Contact:- {}".format(rec_list[7]),
                                  bg="#7209b7", fg="#ced4da", font='Times 30 bold', anchor=W)
            contact_label.pack(fill=X, pady=2, padx=2)

            # Gender
            gender_label = Label(right_frame, text="Gender:- {}".format(rec_list[2]),
                                 bg="#ced4da", fg="#7209b7", font='Times 30 bold', anchor=W)
            gender_label.pack(fill=X, pady=2, padx=2)

            # aadhar
            aadhar_label = Label(right_frame, text="Aadhar no:- {}".format(rec_list[3]),
                                 bg="#7209b7", fg="#ced4da", font='Times 30 bold', anchor=W)
            aadhar_label.pack(fill=X, pady=2, padx=2)

            # Account Type
            ac_type_label = Label(right_frame, text="Account Type:-{}".format(rec_list[6]),
                                  bg="#ced4da", fg="#7209b7", font='Times 30 bold', anchor=W)
            ac_type_label.pack(fill=X, pady=2, padx=2)

            # address Type
            address_label = Label(right_frame, text="Address:- {}".format(rec_list[5]),
                                  bg="#7209b7", fg="#ced4da", font='Times 30 bold', anchor=W)
            address_label.pack(fill=X, pady=2, padx=2)

            root.bind("<Return>",  clear_widget)
            

            right_frame.place(x=750, y=80)

            # mycursor.execute("SELECT * FROM user_account WHERE account_number = {}".format(acc_no))
        else:
            temp.set('Account not found')
            account_entry.delete(0, 20)
            right_frame.place_forget()
            
    
    # Heading Configurations
    hed = Label(root, text="Search User Account", bg="#4361ee",
                fg="#e9ecef", font="Times 60 underline bold")
    # placing the widget on the screen
    hed.pack(fill=X)

    main_frame = Frame(root, bg="#4cc9f0")

    left_frame = Frame(main_frame, bg='#4cc9f0')

    instruction_delete = Label(left_frame,
                               text=""" 1.Enter valid Account Number \n 2.Press "Esc" key to Exit \n 3.Press "Enter" to delete""", bg="green", fg="#000000",
                               font="Times 25 bold", justify=LEFT, anchor=W)
    instruction_delete.pack(padx=0, fill=X)

    # nested frame for the Label , Text input and button
    base_frame = Frame(left_frame, bg="#4cc9f0")

    account_number = Label(base_frame, text="Enter A/C No:",
                           bg="#7209b7", fg="#ced4da", font='Times 30 bold', width=11)
    account_number.grid(row=0, column=0, padx=(0, 5))

    account_entry = Entry(base_frame, font='Times 30 bold',
                          width=12, bg='#7209b7', fg='#ced4da')
    account_entry.grid(row=0, column=1)

    search = Button(base_frame,
                    bg="#4361ee", fg="#e9ecef",
                    text='Search Account',
                    anchor=CENTER,
                    font='Times 20 bold',
                    justify=CENTER,
                    activebackground="#e9ecef",
                    activeforeground="#4361ee",
                    command=search_account
                    )
    search.grid(row=1, column=0, columnspan=2, padx=(27, 0), pady=35)

    

    base_frame.pack(pady=(120,0))

    

    left_frame.pack(anchor=W, fill=Y, padx=(20, 0), pady=80)

    right_frame = Frame(main_frame, bg='black')

    msg_frame = Frame(main_frame)

    wait = Label(msg_frame, textvariable=temp,
                 bg="#7209b7", fg="#ced4da", font='Times 30 bold', anchor=W)
    wait.pack(fill=X, pady=2, padx=2)
    msg_frame.place(x=750, y=0)
    right_frame.place(x=750, y=170)

    main_frame.pack(fill=X, expand=TRUE , pady = (0,100))

    # Adding an event to the Esc button for program termination
    root.bind("<Escape>", lambda event: root.destroy())

    # configuring the base window background
    root.configure(bg="#4cc9f0")

    # Termination of the Tkinter Process
    mainloop()


def call_search_user_account():
    search_user_account()
