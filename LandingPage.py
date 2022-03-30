#importing the tkinter library
import tkinter as tk
from tkinter import *
import tkinter.font as tf

#importing the code files
import User_account as ua 
import Delete_account as da
import SearchAccount as sa
import Update_account as Update_ac
import Database_LogIn as DL

root = Tk()
#making Full screen as Default
root.attributes("-fullscreen", True)
#Title of the window
root.title('Bank Management System')
# add widgets here
 

#Heading Configurations
hed = Label(root, text = "Vishwakarma Pvt.Ltd.", bg = "#4361ee",fg="#e9ecef",font="Times 50 underline bold")
#placing the widget on the screen
hed.pack(fill=X)

#Bank details Heading Configurations 
instruction = Label(root, text = "Bank Details:",bg = "#7209b7",fg="#ced4da",font="Times 25 bold" , anchor = NW, padx=15, pady=10)
#placing the widget on the screen
instruction.pack(pady=(20,8),padx=100, fill=X) 
fontstyle=tf.Font(family="Times",size= 20, weight= "bold")

#Bank Details Body Configurations 
instruction_Message = Label(root, 
text = """  Branch Name:                           Pune ( 21196 ) \n  IFSC:                                          Pune0Maharastra\n  Customer Care(Toll Free):       +917537553257\n  Working Hours:                        10AM - 5PM\n Press "Escape(Esc)" Key to Exit.""",bg = "green",fg="#000000",
font=fontstyle, justify = LEFT , anchor = NW, padx=30,pady=10) 
#placing the widget on the screen
instruction_Message.pack(pady = 0 ,padx=100,fill = X)
 
#services Title configuration
services = Label(root, text = "Services:",bg = "#7209b7",fg="#ced4da",font="Times 25 bold" , anchor = NW, padx=15, pady=10)
#placing the widget on the screen
services.pack(pady=(20,1),padx=100, fill=X) 

#creating the Virtual frame
button_frame = Frame(root,bg="#000000")

#creating and configuring the button
create_usr_btn = Button(button_frame,
bg = "green",fg="#000000",
text = 'Create Account',
anchor = CENTER,
font = 'Times 25 bold',
justify = CENTER,
activebackground ="#7209b7",
activeforeground ="#ced4da",
height = 2,
bd = 5,
width = 28,
command = ua.call_function
)
#placing the widget on the screen with grid
create_usr_btn.grid(row = 0 , column = 0,padx = 1, pady = 1)

#creating and configuring the button
delete_usr_btn = Button(button_frame,
bg = "green",fg="#000000",
text = 'Delete Account',
anchor = CENTER,
font = 'Times 25 bold',
justify = CENTER,
activebackground ="#4361ee",
activeforeground ="#e9ecef",
height = 2,
bd = 5,
width = 28,
command = da.call_delete_user_account
)
#placing the widget on the screen with grid
delete_usr_btn.grid(row = 0 , column = 1,padx = 1, pady = 1)

#creating and configuring the button
search_usr_btn = Button(button_frame,
bg = "green",fg="#000000",
text = 'Search Account',
anchor = CENTER,
font = 'Times 25 bold',
justify = CENTER,
activebackground ="#ced4da",
activeforeground ="#7209b7",
height = 2,
bd = 5,
width = 28,
command = sa.call_search_user_account
)
#placing the widget on the screen with grid
search_usr_btn.grid(row = 1 , column = 0 , padx = 1 , pady = 1 )

#creating and configuring the button
update_usr_btn = Button(button_frame,
bg = "green",fg="#000000",
text = 'Update Account',
anchor = CENTER,
font = 'Times 25 bold',
justify = CENTER,
activebackground ="#000000",
activeforeground ="green",
height = 2,
bd = 5,
width = 28,
command = Update_ac.call_update_user_account
)
#placing the widget on the screen with grid
update_usr_btn.grid(row = 1 , column = 1, padx = 1, pady = 1)

#placing and Packing the entire frame to the screen or root frame
button_frame.pack(pady=10)

#Adding an event to the Esc button for program termination 
root.bind("<Escape>", lambda event: root.destroy())
 

#configuring the base window background
root.configure(bg="#4cc9f0")

#Termination of the Tkinter Process
mainloop()
 

