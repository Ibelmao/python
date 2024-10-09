import tkinter as tk
from tkinter import messagebox

def verificar_login():
    usuario = entrada_user.get()
    senha = entrada_pwd.get()
    if usuario == 'admin' and senha == '12345':
        messagebox.showinfo('Login', 'O login foi bem sucedido!')
    else:
        messagebox.showinfo('erro','Usuário ou senha incorretos!')
janela = tk.Tk()
janela.title('Tela de Login')

janela.geometry('500x250')

label_usuario = tk.Label(janela, text='Usuário') 
label_usuario.pack(pady=20) 

entrada_user = tk.Entry(janela)
entrada_user.pack()       

label_senha = tk.Label(janela, text='Senha') 
label_senha.pack(pady=20) 

entrada_pwd = tk.Entry(janela,show='*')
entrada_pwd.pack()

botao_login = tk.Button(janela, text='LOGIN',command=verificar_login)
botao_login.pack(pady=50)

janela.mainloop()