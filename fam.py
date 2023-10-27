import customtkinter as ctk 
from tkinter  import *
from tkinter import messagebox
import sqlite3

app = ctk.CTk()

app.geometry('600x400')



conn = sqlite3.connect('famdatabase.db')
cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS usuarios (
                   username TEXT NOT NULL,
                   password TEXT NOT NULL )''')


def tela_principal():
    sistema = ctk.CTk()
    sistema.geometry('1920x1080')
    
    
    
    
    
    
    
    sistema.mainloop()







def validar_formulario():
    username = login_entry.get()
    password = senha_entry.get()

    if username != ''  and password != '':
        cursor.execute(
            'SELECT  username FROM usuarios WHERE username=?', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Erro', 'Usuário já existe.')
        else:
            cursor.execute('INSERT INTO usuarios VALUES (?,?)', [
                           username, password])
            conn.commit()
            messagebox.showinfo('Sucesso', 'Conta criada com sucesso ;)')
            return tela_principal()
            

    else:
        messagebox.showerror('Erro', 'Por favor, insira todos os dados.')





login_entry = ctk.CTkEntry(master=app, placeholder_text='Insira seu login', width=200)
login_entry.place(relx=0.3, rely=0.3)

senha_entry = ctk.CTkEntry(master=app, placeholder_text='Insira sua senha', width=200)
senha_entry.place(relx=0.3, rely=0.45)


botao_login = ctk.CTkButton(master=app,text='CADASTRAR', command=validar_formulario)
botao_login.place(relx=0.3, rely=0.55)


app.mainloop()