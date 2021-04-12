import random,string
from tkinter import *
import pyperclip
#libraries imported above

root = Tk()  #initilized tkinter.window created
root.geometry("400x400")
root.title("Password Generator")
root.resizable(0,0)   #set fix size for window


#Label() - for labels that cant be changed by users

Label(root, text='Password Generator', font='arial 15 bold').pack()


pass_label = Label(root, text="Password Length", font = 'arial 10 bold').pack()
pass_len = IntVar()  #how u create variables in tkinter
#using spinbox widget.  can select from specifc value range

length = Spinbox(root, from_ = 8, to_ = 24, textvariable = pass_len, width = 15 ).pack()

pass_Str = StringVar()

def pwd_generator():
    password = ''
    for x in range(0,6):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + \
                   random.choice(string.digits) + random.choice(string.punctuation)
        print(password)
    for y in range(pass_len.get()-6):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + \
                   string.digits + string.punctuation)
        print(password)
        pass_Str.set(password)  #variable that stores final password for tkinter


#creating button to click to generate pasword

Button(root, text = 'Generate PASSWORD!!', command = pwd_generator ).pack(pady=5)
Entry(root, textvariable = pass_Str).pack()

#function to copy password onto clipboard

def copy_pwd():
    pyperclip.copy(pass_Str.get())

#button to call copy_pwd method
#pad y- pads along

Button(root ,text = "Copy to Clipboard", command = copy_pwd).pack(pady=5)



root.mainloop()

