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
        self.frame = Frame(window, bg='#000')
        self.frame.pack(expand=True)

        self.label_welcome = Label(self.frame, text='Welcome to Bank.py', font=('Times new Roman', 26, 'bold'), fg='#0266f2', bg='#000')
        self.label_welcome.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

        self.username_label_login = Label(self.frame, text='Username:', font=('Times new Roman', 20, 'bold'), bg='#000', fg='#fff')
        self.username_label_login.grid(row=1, column=0, padx=(20, 0))

        self.username_login = Entry(self.frame, font=('Times new Roman', 20))
        self.username_login.grid(row=1, column=1, padx=(0, 20))

        self.password_label_login = Label(self.frame, text='Password:', font=('Times new Roman', 20, 'bold'), bg='#000', fg='#fff')
        self.password_label_login.grid(row=2, column=0, padx=(20, 0))

        self.password_login = Entry(self.frame, font=('Times new Roman', 20))
        self.password_login.grid(row=2, column=1, pady=20, padx=(0, 20))

        self.login_button = Button(self.frame, text='Log in', font=('Times new Roman', 12, 'bold'), bg='#E6FFFF', activebackground='#E6FFFF')
        self.login_button.grid(row=3, column=0, columnspan=2, pady=(0, 20))

        self.sign_button = Button(self.frame, text='Sign Up!', font=('Times new Roman', 12, 'bold'), bg='#E6FFFF', activebackground='#E6FFFF', command=self.build_signup)
        self.sign_button.grid(row=3, column=1, pady=(0, 20))


    @classmethod
    def build_signup(self):
        self.new_window = Toplevel()
        self.new_window.title('Sign Up!')
        self.new_window.resizable(FALSE, FALSE)

        self.signup_frame = Frame(self.new_window, bg='#000')
        self.signup_frame.pack(expand=True)

        self.signup_label = Label(self.signup_frame, text='Enter your credentials', font=('Times new Roman', 26, 'bold'), fg='#fcfc03', bg='#000')
        self.signup_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.username_label_signup = Label(self.signup_frame, text='Username:', font=('Times new Roman', 20, 'bold'), bg='#000', fg='#fff')
        self.username_label_signup.grid(row=1, column=0, padx=(20, 0))

        self.username_signup = Entry(self.signup_frame, font=('Times new Roman', 20))
        self.username_signup.grid(row=1, column=1, padx=(0, 20))

        self.password_label_signup = Label(self.signup_frame, text='Password:', font=('Times new Roman', 20, 'bold'), bg='#000', fg='#fff')
        self.password_label_signup.grid(row=2, column=0, padx=(20, 0))

        self.password_signup = Entry(self.signup_frame, font=('Times new Roman', 20))
        self.password_signup.grid(row=2, column=1, padx=(0, 20), pady=20)

        self.repeat_password_label = Label(self.signup_frame, text='Repeat password:', font=('Times new Roman', 20, 'bold'), bg='#000', fg='#fff')
        self.repeat_password_label.grid(row=3, column=0, padx=(20, 0))

        self.repeat_password = Entry(self.signup_frame, font=('Times new Roman', 20))
        self.repeat_password.grid(row=3, column=1, padx=(0, 20))

        self.signup = Button(self.signup_frame, text='Sign Up!', font=('Times new Roman', 12, 'bold'), width=15, bg='#FFFEE6', activebackground='#FFFEE6')
        self.signup.grid(row=4, column=0, columnspan=2, pady=20)