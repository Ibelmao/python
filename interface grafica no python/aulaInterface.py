#criando uma janela gráfica simples
import tkinter as tk


def clique():
    label.config(text='Botão foi clicado! ')
def mostra_informacao():
    texto = entrada.get()
    label.config(text=texto)
def saudacao():
    label.config(text='Olá, Tkinter!')

janela = tk.Tk()
janela.title('Minha primeira janela gráfica')
janela.geometry('300x300')



entrada = tk.Frame(janela)
entrada.pack(pady=10)


botao = tk.Button(janela, text='Clique aqui',command=saudacao)
botao.pack(side='left')

label = tk.Label(janela, text='Aguardando')
label.pack(side='left')
janela.mainloop()
    