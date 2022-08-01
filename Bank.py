from tkinter import messagebox
from openpyxl import load_workbook

class Bank:

    def __init__(self, username: str, password: str, window, money=0):
        self.__window = window
        self.__username = username
        self.__password = password
        self.__money = money


    def sign_up(self):
        wk = load_workbook('users.xlsx')
        sheet = wk.active
        
        for cell in sheet['A']:
            row = cell.row + 1

            if cell.value == self.__username:
                messagebox.showerror('Used username', 'This username already exists, please choose another one')
                return
            
            if sheet[f'A{row}'].value == None:
                sheet[f'A{row}'].value = self.__username

            if sheet[f'B{row}'].value == None:
                sheet[f'B{row}'].value = self.__password

            if sheet[f'C{row}'].value == None:
                sheet[f'C{row}'].value = self.__money
            

        wk.save('users.xlsx')
        messagebox.showinfo('Signed up!', 'You signed up with sucess!')
        self.__window.destroy()


    def log_in(self):
        wk = load_workbook('users.xlsx')
        sheet = wk.active

        for cell in sheet['A']:
            if cell.value == self.__username and sheet[f'B{cell.row}'].value == self.__password:
                return True
            
        return False
        