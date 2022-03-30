import tkinter as tk
import mysql.connector
import tkinter.font as tf
# from mysql.connector import connect,Error
from tkinter import *


def delete_user_account():
    # try:
    #     with connect(
    #         host="localhost",
    #         user="root",
    #         password="Vishal123",
    #         # database="project_dbms"

    #     )as connection:
    #         print(connection)
    # except Error as e:
    #     print(e)

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
    root.title('Delete User Account')

    # add widgets here
    # Heading Configurations
    hed = Label(root, text="Delete User Account", bg="#4361ee",
                fg="#e9ecef", font="Times 60 underline bold")
    # placing the widget on the screen
    hed.pack(fill=X)

    # Bank details Heading Configurations
    instruction1 = Label(root, text="Instruction:", bg="#7209b7",
                        fg="#ced4da", font="Times 25 bold", anchor=NW, padx=15, pady=10)
    # placing the widget on the screen
    instruction1.pack(pady=(20, 8), padx=100, fill=X)
    fontstyle = tf.Font(family="Times", size=20, weight="bold")

    # Bank Details Body Configurations
    instruction_Message1 = Label(root,
                                text=""" 1.Enter valid Account Number \n 2.Press "Esc" key to Exit""", bg="green", fg="#000000",
                                font=fontstyle, justify=LEFT, anchor=NW, padx=30, pady=10)

    # placing the widget on the screen
    instruction_Message1.pack(pady=0, padx=100, fill=X)

    base_frame = Frame(root, bg="#4cc9f0")
    account_number = Label(base_frame, text="Enter A/C No:",
                           bg="#7209b7", fg="#ced4da", font='Times 30 bold', width=11)
    account_number.grid(row=0, column=0, padx=(0, 5))

    account_entry = Entry(base_frame, font='Times 30 bold',
                          width=12, bg='#7209b7', fg='#ced4da')
    account_entry.grid(row=0, column=1)

    def fetch_values():
        mycursor.execute("SELECT account_number FROM user_account")
        numb = mycursor.fetchall()
        numb_list = list(sum(numb, ()))
        return numb_list

    message_disp = StringVar()
    message_disp.set('Waiting for user response')
    def delete_account():
        acc_no = int(account_entry.get())

        numb_list = fetch_values()
        if acc_no in numb_list:
            message_disp.set('Your account has been deleted SUCCESSFULLY')
            mycursor.execute(
                "DELETE FROM user_account WHERE account_number = {}".format(acc_no))
            mydb.commit()
            account_entry.delete(0,20)

        else:
            message_disp.set('User account Not found please check it again')
            account_entry.delete(0,10)
            
    delete = Button(base_frame,
                    bg="#4361ee", fg="#e9ecef",
                    text='Delete Account',
                    anchor=CENTER,
                    font='Times 20 bold',
                    justify=CENTER,
                    activebackground="#e9ecef",
                    activeforeground="#4361ee",
                    command=delete_account
                    )
    delete.grid(row=1, column=0, columnspan=2, padx=(27, 0), pady=35)

    base_frame.pack(pady=80)
    # display_text = {
    #     'default': 'Waiting for User Response',
    #     'delete': 'Your account has been deleted succesfully',
    #     'notFound': 'Your account is not present'
    # }

    display_Message = Label(root,
                            textvariable=message_disp, bg="green", fg="#000000",
                            font=fontstyle, justify=CENTER, padx=30, pady=10)

    # placing the widget on the screen
    display_Message.pack(pady=0, padx=100, fill=X)

    # Adding an event to the Esc button for program termination
    root.bind("<Escape>", lambda event: root.destroy())

    # configuring the base window background
    root.configure(bg="#4cc9f0")

    # Termination of the Tkinter Process
    mainloop()

def call_delete_user_account():
    delete_user_account()

