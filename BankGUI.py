from tkinter import *

class BankGUI:

    def __init__(self, title: str, reswid: bool, reshei: bool, geometry='no'):
        self.window = Tk()
        self.window.title(title)
        self.window.resizable(reswid, reshei)
        if geometry == 'no':
            pass
        else:
            self.window.geometry(geometry)
        self.build_interface(self.window)

        self.window.mainloop()


    @classmethod
    def build_interface(self, window):
        self.frame = Frame(window)
        self.frame.pack(expand=True)

        self.label_welcome = Label(self.frame, text='Welcome to Bank.py', font=('Times new Roman', 26, 'bold'), fg='#012d6b')
        self.label_welcome.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

        self.username_label_login = Label(self.frame, text='Username:', font=('Times new Roman', 20))
        self.username_label_login.grid(row=1, column=0, padx=(20, 0))

        self.username_login = Entry(self.frame, font=('Times new Roman', 20))
        self.username_login.grid(row=1, column=1, padx=(0, 20))

        self.password_label_login = Label(self.frame, text='Password:', font=('Times new Roman', 20))
        self.password_label_login.grid(row=2, column=0, padx=(20, 0))

        self.password_login = Entry(self.frame, font=('Times new Roman', 20))
        self.password_login.grid(row=2, column=1, pady=10, padx=(0, 20))

        self.login_button = Button(self.frame, text='Log in', font=('Times new Roman', 12, 'bold'))
        self.login_button.grid(row=3, column=0, columnspan=2)

        self.sign_button = Button(self.frame, text='Sign Up!', font=('Times new Roman', 12, 'bold'), command=self.build_signup)
        self.sign_button.grid(row=3, column=1)
