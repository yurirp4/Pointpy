import tkinter as tk
from tkinter import ttk
from tkinter import *

janela = tk.Tk()
janela.title('Pedidos online - Point')
janela.geometry("530x500")
janela.iconphoto(False, tk.PhotoImage(file="pizza.png"))

lista_pratos = ["pizza","beirute","x-tudo"]

def selecionado(event, textnome):
    textnome.delete(0, 'end')
    textnome.config(fg='black')


def deselecionado(event, textnome):
    if textnome.get() == "":
        textnome.insert(0, '**Essa informação é obrigatório!')
        textnome.config(fg='red')
        
def add():
    n= entry_Pizza.get()
    size = Comanda.size()
    items = Comanda.get(0, size)
    if n == "Escolha seu pedido":
        return
        
# Rótulos Entradas:

label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=1, pady=1)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=1, pady=1)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=2, column=0, padx=1, pady=1)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=1, pady=1)

label_endereco = tk.Label(janela, text='Endereço')
label_endereco.grid(row=4, column=0, padx=1, pady=1)

label_numerocasa = tk.Label(janela, text='Numero da casa')
label_numerocasa.grid(row=5, column=0, padx=1, pady=1)

label_pizza = tk.Label(janela, text='Pratos')
label_pizza.grid(row=6, column=0, padx=5, pady=5)

label_pizza = tk.Label(janela, text='COMANDA:')
label_pizza.grid(row=1, column=2, padx=1, pady=1)

    # Caixas Entradas:
entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=0, column=1, padx=5, pady=5)
entry_nome.insert(0, 'Qual seu nome?')
entry_nome.bind('<FocusIn>', lambda event=entry_nome, btn=entry_nome: selecionado(event, btn))
entry_nome.bind('<FocusOut>', lambda event=entry_nome, btn=entry_nome: deselecionado(event, btn))

entry_sobrenome = tk.Entry(janela, width=30)
entry_sobrenome.grid(row=1, column=1, padx=5, pady=5)
entry_sobrenome.insert(0, 'Qual seu sobrenome?')
entry_sobrenome.bind('<FocusIn>', lambda event=entry_sobrenome, btn=entry_sobrenome: selecionado(event, btn))
entry_sobrenome.bind('<FocusOut>', lambda event=entry_sobrenome, btn=entry_sobrenome: deselecionado(event, btn))
entry_email = tk.Entry(janela, width=30)
entry_email.grid(row=2, column=1, padx=1, pady=1)
entry_email.insert(0, 'Qual seu email?')
entry_email.bind('<FocusIn>', lambda event=entry_email, btn=entry_email: selecionado(event, btn))
entry_email.bind('<FocusOut>', lambda event=entry_email, btn=entry_email: deselecionado(event, btn))

entry_endereco = tk.Entry(janela, width=30)
entry_endereco.grid(row=3, column=1, padx=1, pady=1)
entry_endereco.insert(0, 'Qual seu endereço?')
entry_endereco.bind('<FocusIn>', lambda event=entry_endereco, btn=entry_endereco: selecionado(event, btn))
entry_endereco.bind('<FocusOut>', lambda event=entry_endereco, btn=entry_endereco: deselecionado(event, btn))

entry_numerocasa = tk.Entry(janela, width=30)
entry_numerocasa.grid(row=4, column=1, padx=1, pady=1)
entry_numerocasa.insert(0, 'Qual seu numero?')
entry_numerocasa.bind('<FocusIn>', lambda event=entry_numerocasa, btn=entry_numerocasa: selecionado(event, btn))
entry_numerocasa.bind('<FocusOut>', lambda event=entry_numerocasa, btn=entry_numerocasa: deselecionado(event, btn))

entry_telefone = tk.Entry(janela, width=30)
entry_telefone.grid(row=5, column=1, padx=1, pady=1)
entry_telefone.insert(0, 'Qual  o numero da casa?')
entry_telefone.bind('<FocusIn>', lambda event=entry_telefone, btn=entry_telefone: selecionado(event, btn))
entry_telefone.bind('<FocusOut>', lambda event=entry_telefone, btn=entry_telefone: deselecionado(event, btn))


entry_Pizza = ttk.Combobox(values=lista_pratos,width=40)
entry_Pizza.set('Escolha seu pedido')
entry_Pizza.grid(row=6, column=1, padx=5, pady=5)

Comanda = Listbox(janela)
#entry_comanda = ttk.Entry(janela,textvariable=name,width=20)
Comanda.grid(row=2, column=2, padx=1, pady=1)




    # Botão de Cadastrar

botao_itens = tk.Button(text='adicionar a comanda', command=add)
botao_itens.grid(row=7, column=1, columnspan=1, padx=5, pady=5,ipadx=2,rowspan=1)

botao_cadastrar = tk.Button(text='Fazer pedido', command=finalizar)
botao_cadastrar.grid(row=10, column=1, columnspan=1, padx=10, pady=10, ipadx=80)

janela.mainloop()
