from tkinter import *
from tkinter import messagebox
from Bank import Bank

class BankGUI:

    def __init__(self, title: str, reswid: bool, reshei: bool, geometry='no'):
        self.__window = Tk()
        self.__window.title(title)
        self.__window.resizable(reswid, reshei)
        if geometry == 'no':
            pass
        else:
            self.__window.geometry(geometry)
        self.__build_interface(self.__window)

        self.__window.mainloop()


    def __build_interface(self, window):
        self.__frame = Frame(window, bg='#000')
        self.__frame.pack(expand=True)

        self.__label_welcome = Label(self.__frame, text='Welcome to Bank.py', font=('Times new Roman', 26, 'bold'), fg='#0266f2', bg='#000')
        self.__label_welcome.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

        self.__username_label_login = Label(self.__frame, text='Username:', font=('Times new Roman', 20, 'bold'), bg='#000', fg='#fff')
        self.__username_label_login.grid(row=1, column=0, padx=(20, 0))

        self.__username_login = Entry(self.__frame, font=('Times new Roman', 20))
        self.__username_login.grid(row=1, column=1, padx=(0, 20))

        self.__password_label_login = Label(self.__frame, text='Password:', font=('Times new Roman', 20, 'bold'), bg='#000', fg='#fff')
        self.__password_label_login.grid(row=2, column=0, padx=(20, 0))

        self.__password_login = Entry(self.__frame, font=('Times new Roman', 20))
        self.__password_login.grid(row=2, column=1, pady=20, padx=(0, 20))

        self.__login_button = Button(self.__frame, text='Log in', font=('Times new Roman', 12, 'bold'), bg='#E6FFFF', activebackground='#E6FFFF', command=lambda: Bank(self.__username_login.get(), self.__password_login.get(), self.__window).log_in())
        self.__login_button.grid(row=3, column=0, columnspan=2, pady=(0, 20))

        self.__sign_button = Button(self.__frame, text='Sign Up!', font=('Times new Roman', 12, 'bold'), bg='#E6FFFF', activebackground='#E6FFFF', command=self.__build_signup)
        self.__sign_button.grid(row=3, column=1, pady=(0, 20))


    def __build_signup(self):
        self.__new_window = Toplevel()
        self.__new_window.title('Sign Up!')
        self.__new_window.resizable(FALSE, FALSE)

        self.__signup_frame = Frame(self.__new_window, bg='#000')
        self.__signup_frame.pack(expand=True)

        self.__signup_label = Label(self.__signup_frame, text='Enter your credentials', font=('Times new Roman', 26, 'bold'), fg='#fcfc03', bg='#000')
        self.__signup_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.__username_label_signup = Label(self.__signup_frame, text='Username:', font=('Times new Roman', 20, 'bold'), bg='#000', fg='#fff')
        self.__username_label_signup.grid(row=1, column=0, padx=(20, 0))

        self.__username_signup = Entry(self.__signup_frame, font=('Times new Roman', 20))
        self.__username_signup.grid(row=1, column=1, padx=(0, 20))

        self.__password_label_signup = Label(self.__signup_frame, text='Password:', font=('Times new Roman', 20, 'bold'), bg='#000', fg='#fff')
        self.__password_label_signup.grid(row=2, column=0, padx=(20, 0))

        self.__password_signup = Entry(self.__signup_frame, font=('Times new Roman', 20))
        self.__password_signup.grid(row=2, column=1, padx=(0, 20), pady=20)

        self.__repeat_password_label = Label(self.__signup_frame, text='Repeat password:', font=('Times new Roman', 20, 'bold'), bg='#000', fg='#fff')
        self.__repeat_password_label.grid(row=3, column=0, padx=(20, 0))

        self.__repeat_password = Entry(self.__signup_frame, font=('Times new Roman', 20))
        self.__repeat_password.grid(row=3, column=1, padx=(0, 20))

        self.__signup = Button(
            self.__signup_frame, 
            text='Sign Up!', font=('Times new Roman', 12, 'bold'), 
            width=15, bg='#FFFEE6', 
            activebackground='#FFFEE6', 
            command=lambda: Bank(self.__username_signup.get(), self.__password_signup.get(), self.__new_window).sign_up() if self.__password_signup.get() == self.__repeat_password.get() and self.__username_signup.get() != '' and self.__password_signup.get() != '' else messagebox.showerror('Error', 'Please enter all fields or match the passwords!'))
        self.__signup.grid(row=4, column=0, columnspan=2, pady=20)