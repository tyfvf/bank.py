from tkinter import *
from tkinter import messagebox
from Bank import Bank

class BankGUI:

    def __init__(self, title: str, reswid: bool, reshei: bool, geometry='no'):
        self.__title = title
        self.__reswid = reswid
        self.__reshei = reshei
        self.__geometry = geometry
        
        self.__window = Tk()
        self.__window.title(self.__title)
        self.__window.resizable(self.__reswid, self.__reshei)
        if self.__geometry == 'no':
            pass
        else:
            self.__window.geometry(self.__geometry)
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

        self.__password_login = Entry(self.__frame, font=('Times new Roman', 20), show='*')
        self.__password_login.grid(row=2, column=1, pady=20, padx=(0, 20))

        self.__login_button = Button(self.__frame, text='Log in', font=('Times new Roman', 12, 'bold'), bg='#E6FFFF', activebackground='#E6FFFF', command=lambda: self.__build_bank(self.__username_login.get()) if Bank(self.__username_login.get(), self.__window, self.__password_login.get()).log_in() else messagebox.showerror('Wrong credentials', 'Wrong username or password, please try again!'))
        self.__login_button.grid(row=3, column=0, columnspan=2, pady=(0, 20))

        self.__sign_button = Button(self.__frame, text='Sign Up!', font=('Times new Roman', 12, 'bold'), bg='#E6FFFF', activebackground='#E6FFFF', command=self.__build_signup)
        self.__sign_button.grid(row=3, column=1, pady=(0, 20))


    def __build_signup(self):
        self.__new_window = Toplevel()
        self.__new_window.title(self.__title)
        self.__new_window.resizable(self.__reswid, self.__reshei)
        if self.__geometry == 'no':
            pass
        else:
            self.__new_window.geometry(self.__geometry)

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

        self.__password_signup = Entry(self.__signup_frame, font=('Times new Roman', 20), show='*')
        self.__password_signup.grid(row=2, column=1, padx=(0, 20), pady=20)

        self.__repeat_password_label = Label(self.__signup_frame, text='Repeat password:', font=('Times new Roman', 20, 'bold'), bg='#000', fg='#fff')
        self.__repeat_password_label.grid(row=3, column=0, padx=(20, 0))

        self.__repeat_password = Entry(self.__signup_frame, font=('Times new Roman', 20), show='*')
        self.__repeat_password.grid(row=3, column=1, padx=(0, 20))

        self.__signup = Button(
            self.__signup_frame, 
            text='Sign Up!', font=('Times new Roman', 12, 'bold'), 
            width=15, bg='#FFFEE6', 
            activebackground='#FFFEE6', 
            command=lambda: Bank(self.__username_signup.get(), self.__new_window, self.__password_signup.get()).sign_up() if self.__password_signup.get() == self.__repeat_password.get() and self.__username_signup.get() != '' and self.__password_signup.get() != '' else messagebox.showerror('Error', 'Please enter all fields or match the passwords!'))
        self.__signup.grid(row=4, column=0, columnspan=2, pady=20)


    def __build_bank(self, username):
        self.__window.destroy()
        self.__bank_window = Tk()
        self.__bank_window.title(self.__title)
        self.__bank_window.resizable(self.__reswid, self.__reshei)
        if self.__geometry == 'no':
            pass
        else:
            self.__bank_window.geometry(self.__geometry)

        self.__bank_frame = Frame(self.__bank_window, bg='#000')
        self.__bank_frame.pack()

        self.__bank_label = Label(self.__bank_frame, text=f'Welcome {username}', font=('Times new Roman', 26, 'bold'), bg='#000', fg='#13e305')
        self.__bank_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.__bank_deposit = Button(self.__bank_frame, text='Deposit', font=('Times new Roman', 12, 'bold'), width=10, command=lambda: self.__build_deposit(username))
        self.__bank_deposit.grid(row=1, column=0, padx=20, pady=20)

        self.__bank_transfer = Button(self.__bank_frame, text='Transfer', font=('Times new Roman', 12, 'bold'), width=10, command=lambda: self.__build_transfer(username))
        self.__bank_transfer.grid(row=1, column=1, padx=20, pady=20)

        self.__bank_withdraw = Button(self.__bank_frame, text='Withdraw', font=('Times new Roman', 12, 'bold'), width=10, command=lambda: self.__build_withdraw(username))
        self.__bank_withdraw.grid(row=2, column=0, padx=20, pady=20)

        self.__bank_statment = Button(self.__bank_frame, text='Statment', font=('Times new Roman', 12, 'bold'), width=10, command=lambda: self.__build_statment(username))
        self.__bank_statment.grid(row=2, column=1, padx=20, pady=20)

        self.__bank_quit = Button(self.__bank_frame, text='Quit', font=('Times new Roman', 12, 'bold'), bg='#de1818', activebackground='#de1818', border=0, width=10, command=quit)
        self.__bank_quit.grid(row=3, column=0, columnspan=2, padx=20, pady=20)


        self.__bank_window.mainloop()


    def __build_deposit(self, username):
        self.__deposit_window = Toplevel()
        self.__deposit_window.title(self.__title)
        self.__deposit_window.resizable(self.__reswid, self.__reshei)
        if self.__geometry == 'no':
            pass
        else:
            self.__deposit_window.geometry(self.__geometry)

        self.__deposit_frame = Frame(self.__deposit_window, bg='#000')
        self.__deposit_frame.pack()

        self.__deposit_label = Label(self.__deposit_frame, text='Enter how much you want to deposit in your account', font=('Times new Roman', 26, 'bold'), bg='#000', fg='#fcfc03')
        self.__deposit_label.grid(row=0, column=0, padx=20, pady=20)

        self.__deposit_money = Entry(self.__deposit_frame, font=('Times new Roman', 20))
        self.__deposit_money.grid(row=1, column=0, padx=20, pady=20)

        self.__deposit_button = Button(self.__deposit_frame, text='Deposit', font=('Times new Roman', 12, 'bold'), command=lambda: Bank(username, self.__deposit_window, money=self.__deposit_money.get()).deposit() if self.__deposit_money.get() != '' else messagebox.showerror('No value found', 'Please enter a value on the field'))
        self.__deposit_button.grid(row=2, column=0, padx=20, pady=20)


    def __build_transfer(self, username):
        self.__transfer_window = Toplevel()
        self.__transfer_window.title(self.__title)
        self.__transfer_window.resizable(self.__reswid, self.__reshei)
        if self.__geometry == 'no':
            pass
        else:
            self.__transfer_window.geometry(self.__geometry)

        self.__transfer_frame = Frame(self.__transfer_window, bg='#000')
        self.__transfer_frame.pack()

        self.__transfer_label = Label(self.__transfer_frame, text='How much money do you wish to transfer:', font=('Times new Roman', 20, 'bold'), bg='#000', fg='#0266f2')
        self.__transfer_label.grid(row=0, column=0, padx=20, pady=20)

        self.__transfer_money = Entry(self.__transfer_frame, font=('Times new Roman', 20))
        self.__transfer_money.grid(row=0, column=1, padx=20, pady=20)

        self.__transfer_label_to = Label(self.__transfer_frame, text='To (enter the username of the person):', font=('Times new Roman', 20, 'bold'), bg='#000', fg='#0266f2')
        self.__transfer_label_to.grid(row=1, column=0, padx=20, pady=20)

        self.__transfer_to = Entry(self.__transfer_frame, font=('Times new Roman', 20))
        self.__transfer_to.grid(row=1, column=1, padx=20, pady=20)

        self.__transfer_button = Button(self.__transfer_frame, text='Transfer', font=('Times new Roman', 12, 'bold'), command=lambda: Bank(username, self.__transfer_window, money=self.__transfer_money.get()).transfer(self.__transfer_to.get()) if self.__transfer_money.get() != '' and self.__transfer_to.get() != '' else messagebox.showerror('No value found', 'Please enter a value on all fields'))
        self.__transfer_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20)


    def __build_withdraw(self,username):
        self.__withdraw_window = Toplevel()
        self.__withdraw_window.title(self.__title)
        self.__withdraw_window.resizable(self.__reswid, self.__reshei)
        if self.__geometry == 'no':
            pass
        else:
            self.__withdraw_window.geometry(self.__geometry)

        self.__withdraw_frame = Frame(self.__withdraw_window, bg='#000')
        self.__withdraw_frame.pack()

        self.__withdraw_label = Label(self.__withdraw_frame, text='Enter how much you want to withdraw from your account', font=('Times new Roman', 26, 'bold'), bg='#000', fg='#0266f2')
        self.__withdraw_label.grid(row=0, column=0, padx=20, pady=20)

        self.__withdraw_money = Entry(self.__withdraw_frame, font=('Times new Roman', 20))
        self.__withdraw_money.grid(row=1, column=0, padx=20, pady=20)

        self.__withdraw_button = Button(self.__withdraw_frame, text='Withdraw', font=('Times new Roman', 12, 'bold'), command=lambda: Bank(username, self.__withdraw_window, money=self.__withdraw_money.get()).withdraw() if self.__withdraw_money.get() != '' else messagebox.showerror('No value found', 'Please enter a value on the field'))
        self.__withdraw_button.grid(row=2, column=0, padx=20, pady=20)


    def __build_statment(self, username):
        self.__statment_window = Toplevel()
        self.__statment_window.title(self.__title)
        self.__statment_window.resizable(self.__reswid, self.__reshei)
        if self.__geometry == 'no':
            pass
        else:
            self.__statment_window.geometry(self.__geometry)

        self.__statment_frame = Frame(self.__statment_window, bg='#000')
        self.__statment_frame.pack()

        self.__statment_label = Label(self.__statment_frame, text=f'$ {Bank(username, window=self.__statment_window).statment()}', font=('Times new Roman', 40, 'bold'), bg='#000', fg='#fcfc03')
        self.__statment_label.pack(padx=40, pady=40)