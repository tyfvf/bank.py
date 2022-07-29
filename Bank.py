from tkinter import messagebox
from User import User

class Bank:

    def __init__(self, username: str, password: str, window):
        self.__window = window
        self.__username = username
        self.__password = password


    def sign_up(self):
        User(self.__username, self.__password)
        messagebox.showinfo('Signed up with sucess!', 'You created your account with sucess!')
        self.__window.destroy()


    def log_in(self):
        for i in User.all:
            if self.__username == i[0] and self.__password == i[1]:
                messagebox.showinfo('Welcome', f'Welcome to your bank.py account {self.__username}')
                return
        
        messagebox.showerror('Wrong credentials', 'Wrong username or password, please try again!')
