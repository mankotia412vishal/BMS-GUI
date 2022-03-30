import tkinter as tk
import mysql.connector
import tkinter.font as tf

from tkinter import *


def update_user_account():
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
    root.title('Update User Account')

    # add widgets here
    # Heading Configurations
    hed = Label(root, text="Update User Account", bg="#4361ee",
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
    def fetch_account():
        acc_no = int(account_entry.get())
        numb_list = fetch_values()

        if acc_no in numb_list:
            mycursor.execute(
                "SELECT name,address,contact FROM user_account WHERE account_number = {}".format(acc_no))

            record = mycursor.fetchall()
            record_list = list(sum(record, ()))
            print(record_list)
            account_entry.delete(0,20)
            base_frame.destroy()
            display_Message.destroy()

            #Function to Update Account Details 
            def update_account_record():
                u_name = str(update_name_entry.get())
                u_contact = int(update_contact_entry.get())
                u_address = update_address_entry.get()
                sql = "UPDATE  user_account set name = %s ,address = %s ,contact = %s WHERE account_number = %s"
                values = (u_name,u_address,u_contact,acc_no)
                mycursor.execute(sql , values)
                mydb.commit()

                root.destroy()
            #Update Frame 
            update_frame = Frame(root, bg="#4cc9f0")

            #update frame widgets
            update_name = Label(update_frame, text="Name:",
                                bg="#7209b7", fg="#f5f5f5", font='Times 30 bold', width=11)
            update_name.grid(row=0, column=0, padx=(0, 5))

            update_name_entry = Entry(update_frame, font='Times 30 bold',
                                width=12, bg='#7209b7', fg='#b8c0c9')
            update_name_entry.insert(0,'{}'.format(record_list[0]))

            update_name_entry.grid(row=0, column=1)

            #update frame widgets
            update_contact = Label(update_frame, text="Contact:",
                                bg="#7209b7", fg="#f5f5f5", font='Times 30 bold', width=11)
            update_contact.grid(row=1, column=0, padx=(0, 5))

            update_contact_entry = Entry(update_frame, font='Times 30 bold',
                                width=12, bg='#7209b7', fg='#b8c0c9')
            update_contact_entry.insert(0,'{}'.format(record_list[2]))
            update_contact_entry.grid(row=1, column=1)

            #update frame widgets
            update_address = Label(update_frame, text="Address:",
                                bg="#7209b7", fg="#f5f5f5", font='Times 30 bold', width=11)
            update_address.grid(row=2, column=0, padx=(0, 5))

            update_address_entry = Entry(update_frame, font='Times 30 bold',
                                width=12, bg='#7209b7', fg='#b8c0c9')
            update_address_entry.insert(0,'{}'.format(record_list[1]))
            update_address_entry.grid(row=2, column=1)

            #Update Account Button
            Update_account = Button(update_frame,
                    bg="#4361ee", fg="#e9ecef",
                    text='Update Account',
                    anchor=CENTER,
                    font='Times 25 bold',
                    justify=CENTER,
                    activebackground="#e9ecef",
                    activeforeground="#4361ee",
                    command=update_account_record
                    )
            Update_account.grid(row=1, column=3, columnspan=3, padx=(27, 0), pady=35)
            update_frame.pack(pady = (50))
            

        else:
            message_disp.set('User account Not found please check it again')
            account_entry.delete(0,10)
            
    Find_account = Button(base_frame,
                    bg="#4361ee", fg="#e9ecef",
                    text='Find Account',
                    anchor=CENTER,
                    font='Times 20 bold',
                    justify=CENTER,
                    activebackground="#e9ecef",
                    activeforeground="#4361ee",
                    command=fetch_account
                    )
    Find_account.grid(row=1, column=0, columnspan=2, padx=(27, 0), pady=35)

    base_frame.pack(pady=80)

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

def call_update_user_account():
    update_user_account()

