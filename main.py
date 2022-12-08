import tkinter as tk
from tkinter import ttk
from tkinter import *
import datetime as dt
from collections import Counter
import time

numero_pedido = 100
lista_pratos = ["(1) - Pizza [R$26,90]","(2) - Beirute[R$19,90]","(3) - X-tudo[R$5,50]","(4) - Batata-Frita[R$3,00]","(5) - Coca-Cola 2 Litros[R$8,50]","(6) - Coca-Cola 1 Litro[R$5,25]"]
lista_precos = [26.90,19.90,5.50,3.0,8.50,5.25]
formas_pagamento = ['Cartão de Debito',"Cartão de Crédito","Dinheiro","PIX"]

def checar_parametros(txt):
    if txt == None:
        return

class clientes:
    def __init__(self, top=None):
        self.caches_produtos = {"Pizza": 0, "Beirute": 0, "X-tudo": 0, "Batata-Frita": 0, "cocacola2": 0, 'cocacola1': 0}
        self.comanda_ativa = False
        self.total = 0
        self.nome = ''
        self.pagamento = ''
        top.geometry("368x441+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Point Restaurante")
        top.iconphoto(False, tk.PhotoImage(file="pizza.png"))
        top.resizable(width=False, height=False)
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.combobox = tk.StringVar()
        self.combobox2 = tk.StringVar()

        self.Message1 = tk.Message(self.top)
        self.Message1.place(relx=0.019, rely=0.134, relheight=0.041
                , relwidth=0.195)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(padx="1")
        self.Message1.configure(pady="1")
        self.Message1.configure(text='''Nome:''')
        self.Message1.configure(width=52)

        self.Message2 = tk.Message(self.top)
        self.Message2.place(relx=0.0, rely=0.2, relheight=0.043, relwidth=0.284)
        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(padx="1")
        self.Message2.configure(pady="1")
        self.Message2.configure(text='''Sobrenome:''')
        self.Message2.configure(width=81)

        self.Message3 = tk.Message(self.top)
        self.Message3.place(relx=-0.074, rely=0.268, relheight=0.041
                , relwidth=0.342)
        self.Message3.configure(background="#d9d9d9")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(padx="1")
        self.Message3.configure(pady="1")
        self.Message3.configure(text='''E-mail:''')
        self.Message3.configure(width=92)

        self.Message4 = tk.Message(self.top)
        self.Message4.place(relx=-0.039, rely=0.333, relheight=0.041
                , relwidth=0.307)
        self.Message4.configure(background="#d9d9d9")
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(padx="1")
        self.Message4.configure(pady="1")
        self.Message4.configure(text='''Telefone:''')
        self.Message4.configure(width=82)

        self.Message5 = tk.Message(self.top)
        self.Message5.place(relx=-0.039, rely=0.399, relheight=0.043
                , relwidth=0.307)
        self.Message5.configure(background="#d9d9d9")
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#d9d9d9")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(padx="1")
        self.Message5.configure(pady="1")
        self.Message5.configure(text='''Endereço:''')
        self.Message5.configure(width=82)

        self.Message6 = tk.Message(self.top)
        self.Message6.place(relx=-0.039, rely=0.467, relheight=0.041
                , relwidth=0.323)
        self.Message6.configure(background="#d9d9d9")
        self.Message6.configure(cursor="fleur")
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(padx="1")
        self.Message6.configure(pady="1")
        self.Message6.configure(text='''Nº da casa:''')
        self.Message6.configure(width=86)

        self.Message11 = tk.Message(self.top)
        self.Message11.place(relx=-0.030, rely=0.527, relheight=0.041
                            , relwidth=0.323)
        self.Message11.configure(background="#d9d9d9")
        self.Message11.configure(cursor="fleur")
        self.Message11.configure(foreground="#000000")
        self.Message11.configure(highlightbackground="#d9d9d9")
        self.Message11.configure(highlightcolor="black")
        self.Message11.configure(padx="1")
        self.Message11.configure(pady="1")
        self.Message11.configure(text='''Pagamento:''')
        self.Message11.configure(width=86)

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.3, rely=0.134, height=20, relwidth=0.599)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.insert(0,'Qual seu nome?')
        self.Entry1.bind('<FocusIn>', lambda event=self.Entry1, btn=self.Entry1: self.selecionado(event, btn))
        self.Entry1.bind('<FocusOut>', lambda event=self.Entry1, btn=self.Entry1: self.deselecionado(event, btn))

        self.Entry2 = tk.Entry(self.top)
        self.Entry2.place(relx=0.3, rely=0.2, height=20, relwidth=0.599)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.insert(0, 'Qual seu sobrenome?')
        self.Entry2.bind('<FocusIn>', lambda event=self.Entry2, btn=self.Entry2: self.selecionado(event, btn))
        self.Entry2.bind('<FocusOut>', lambda event=self.Entry2, btn=self.Entry2: self.deselecionado(event, btn))

        self.Entry3 = tk.Entry(self.top)
        self.Entry3.place(relx=0.3, rely=0.268, height=20, relwidth=0.599)
        self.Entry3.configure(background="white")
        self.Entry3.configure(cursor="fleur")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.insert(0, 'Qual seu E-mail?')
        self.Entry3.bind('<FocusIn>', lambda event=self.Entry3, btn=self.Entry3: self.selecionado(event, btn))
        self.Entry3.bind('<FocusOut>', lambda event=self.Entry3, btn=self.Entry3: self.deselecionado(event, btn))

        self.Entry4 = tk.Entry(self.top)
        self.Entry4.place(relx=0.3, rely=0.333, height=20, relwidth=0.599)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")
        self.Entry4.insert(0, 'Qual é seu Telefone?')
        self.Entry4.bind('<FocusIn>', lambda event=self.Entry4, btn=self.Entry4: self.selecionado(event, btn))
        self.Entry4.bind('<FocusOut>', lambda event=self.Entry4, btn=self.Entry4: self.deselecionado(event, btn))

        self.Entry5 = tk.Entry(self.top)
        self.Entry5.place(relx=0.3, rely=0.399, height=20, relwidth=0.599)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="#c4c4c4")
        self.Entry5.configure(selectforeground="black")
        self.Entry5.insert(0, 'Qual seu Endereço?')
        self.Entry5.bind('<FocusIn>', lambda event=self.Entry5, btn=self.Entry5: self.selecionado(event, btn))
        self.Entry5.bind('<FocusOut>', lambda event=self.Entry5, btn=self.Entry5: self.deselecionado(event, btn))

        self.Entry6 = tk.Entry(self.top)
        self.Entry6.place(relx=0.3, rely=0.467, height=20, relwidth=0.599)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(selectforeground="black")
        self.Entry6.insert(0, 'Qual o nº da casa?')
        self.Entry6.bind('<FocusIn>', lambda event=self.Entry6, btn=self.Entry6: self.selecionado(event, btn))
        self.Entry6.bind('<FocusOut>', lambda event=self.Entry6, btn=self.Entry6: self.deselecionado(event, btn))

        self.TSeparator1 = ttk.Separator(self.top)
        self.TSeparator1.place(relx=0.0, rely=0.578,  relwidth=1.027)

        self.Message7 = tk.Message(self.top)
        self.Message7.place(relx=0.0, rely=0.621, relheight=0.043
                , relwidth=0.214)
        self.Message7.configure(background="#d9d9d9")
        self.Message7.configure(font="-family {Segoe UI} -size 12 -slant italic")
        self.Message7.configure(foreground="#000000")
        self.Message7.configure(highlightbackground="#d9d9d9")
        self.Message7.configure(highlightcolor="black")
        self.Message7.configure(padx="1")
        self.Message7.configure(pady="1")
        self.Message7.configure(text='''Pratos:''')
        self.Message7.configure(width=57)

        self.TCombobox1 = ttk.Combobox(self.top,values=lista_pratos)
        self.TCombobox1.place(relx=0.226, rely=0.621, relheight=0.048 ,relwidth=0.560)
        self.combobox.set('Selecione')
        self.TCombobox1.configure(textvariable=self.combobox)
        self.TCombobox1.configure(takefocus="tt")

        self.TCombobox2 = ttk.Combobox(self.top, values=formas_pagamento)
        self.TCombobox2.place(relx=0.306, rely=0.521, relheight=0.048
                              , relwidth=0.389)
        self.combobox2.set('Selecione')
        self.TCombobox2.configure(textvariable=self.combobox2)
        self.TCombobox2.configure(takefocus="tt")

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.787, rely=0.621, height=24, width=27)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 11")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''+''')
        self.Button1.configure(command=self.add)

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.867, rely=0.621, height=24, width=27)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''-''')
        self.Button2.configure(command=self.remover)

        self.scrollbar = Scrollbar(self.top)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(self.top)
        self.listbox.pack()
        self.listbox.place(relx=0.117, rely=0.748, relheight=0.145
                , relwidth=0.805)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.Button3 = tk.Button(self.top)
        self.Button3.place(relx=0.159, rely=0.907, height=34, width=237)
        self.Button3.configure(activebackground="beige")
        self.Button3.configure(activeforeground="black")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(compound='left')
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Finalizar pedido''')
        self.Button3.configure(command=self.finalizar)

        self.Message8 = tk.Message(self.top)
        self.Message8.place(relx=-0.074, rely=0.0, relheight=0.086, relwidth=1.0)

        self.Message8.configure(background="#d9d9d9")
        self.Message8.configure(font="-family {Segoe UI} -size 14 -weight bold -slant italic")
        self.Message8.configure(foreground="#944ff2")
        self.Message8.configure(highlightbackground="#d9d9d9")
        self.Message8.configure(highlightcolor="black")
        self.Message8.configure(padx="1")
        self.Message8.configure(pady="1")
        self.Message8.configure(text='''POINT - Restaurante''')
        self.Message8.configure(width=268)

        self.Message9 = tk.Message(self.top)
        self.Message9.place(relx=0.010, rely=0.068, relheight=0.063
                , relwidth=0.903)
        self.Message9.configure(background="#d9d9d9")
        self.Message9.configure(font="-family {Segoe UI} -size 14 -weight bold -slant italic")
        self.Message9.configure(foreground="#f06551")
        self.Message9.configure(highlightbackground="#d9d9d9")
        self.Message9.configure(highlightcolor="black")
        self.Message9.configure(padx="1")
        self.Message9.configure(pady="1")
        self.Message9.configure(text='''Faça já seu pedido''')
        self.Message9.configure(width=256)

        self.Message10 = tk.Message(self.top)
        self.Message10.place(relx=0.3, rely=0.689, relheight=0.041
                , relwidth=0.327)
        self.Message10.configure(background="#d9d9d9")
        self.Message10.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Message10.configure(foreground="#000000")
        self.Message10.configure(highlightbackground="#d9d9d9")
        self.Message10.configure(highlightcolor="black")
        self.Message10.configure(padx="1")
        self.Message10.configure(pady="1")
        self.Message10.configure(text='''Comanda''')
        self.Message10.configure(width=84)

    def remover(self):
        if self.listbox.curselection():
            size = self.listbox.size()
            items = self.listbox.get(0, size)
            self.listbox.delete(self.listbox.curselection())
            self.combobox.get()
            counter = Counter(items)
            for i in reversed(range(size)):
                self.listbox.delete(i)
            self.caches_produtos = {"Pizza": 0, "Beirute": 0, "X-tudo": 0, "Batata-Frita": 0, "cocacola2": 0, 'cocacola1': 0}
            self.total=0


    def selecionado(self,event, textnome):
        textnome.delete(0, 'end')
        textnome.config(fg='black')

    def deselecionado(self,event, textnome):
        if textnome.get() == "":
            textnome.insert(0, '*obrigatório!')
            textnome.config(fg='red')

    def add(self):
        n = self.combobox.get()
        size = self.listbox.size()
        items = self.listbox.get(0, size)
        if not n in lista_pratos:
            return

        #nao esta funcionando corretamente
        elif self.comanda_ativa == True:
            print(self.total)
            self.total = 0
            self.comanda_ativa=False
            for i in reversed(range(size)):
                self.listbox.delete(i)
            if n == lista_pratos[0]:
                self.caches_produtos[f'Pizza'] += 1
                self.total += self.caches_produtos['Pizza']* 26.90
            elif n == lista_pratos[1]:
                self.caches_produtos[f'Beirute'] += 1
                self.total += self.caches_produtos['Beirute'] * 19.90
            elif n == lista_pratos[2]:
                self.caches_produtos['X-tudo'] += 1
                self.total += self.caches_produtos['X-tudo'] * 5.50
            elif n == lista_pratos[3]:
                self.caches_produtos[f'Batata-Frita'] += 1
                self.total += self.caches_produtos['Batata-Frita'] * 3.0
            elif n == lista_pratos[4]:
                self.caches_produtos[f'cocacola2'] += 1
                self.total += self.caches_produtos['cocacola2'] * 8.50
            elif n == lista_pratos[5]:
                self.caches_produtos[f'cocacola1'] += 1
                self.total += self.caches_produtos['cocacola1'] * 5.50
            for i in self.caches_produtos.keys():
                quantidade = self.caches_produtos[i]
                if quantidade >= 1:
                    msg = i.split("[", 1)[0]
                    print(quantidade,msg)
                    self.listbox.insert(0, f'({quantidade}) {msg}'.replace('cocacola2', 'Coca-Cola 2 Litros').replace("cocacola1",'Coca-Cola 1 Litro'))

            print(self.total)
            self.listbox.insert(0,f'Total: {self.total:.2f}'.replace('.',','))


        # print('Foram pedidos: '+f"({quantidade}) - "+i)

        else:
            if n == lista_pratos[0]:
                self.caches_produtos[f'Pizza'] += 1
                self.listbox.insert(0, 'Pizza[R$26,90]')
            elif n == lista_pratos[1]:
                self.caches_produtos[f'Beirute'] += 1
                self.listbox.insert(0, 'Beirute[R$19,90]')
            elif n == lista_pratos[2]:
                self.caches_produtos['X-tudo'] += 1
                self.listbox.insert(0, 'X-tudo[R$5,50]')
            elif n == lista_pratos[3]:
                self.caches_produtos[f'Batata-Frita'] += 1
                self.listbox.insert(0, '[R$3,00]')
            elif n == lista_pratos[4]:
                self.caches_produtos[f'cocacola2'] += 1
                self.listbox.insert(0, 'Coca-Cola 2 Litros[R$8,50]')
            elif n == lista_pratos[5]:
                self.caches_produtos[f'cocacola1'] += 1
                self.listbox.insert(0, 'Coca-Cola 1 Litro[R$5,25]')



    def finalizar(self):
        self.pagamento = self.combobox2.get()
        self.combobox.get()
        self.nome = self.Entry1.get() + ' ' + self.Entry2.get()
        size = self.listbox.size()
        items = self.listbox.get(0, size)
        counter = Counter(items)
        messagem = ''
        for i in reversed(range(size)):
            self.listbox.delete(i)
        for i, pairs in enumerate(counter.items()):
            k, v = pairs
            if v > 1:
                msg = k.split("[", 1)[0]
                self.listbox.insert(i, f"({v}) - {msg}")
            else:
                self.listbox.insert(i, k)
        for i in self.caches_produtos.keys():
            quantidade = self.caches_produtos[i]
            if quantidade >=1:
                if i == "Pizza":
                    soma = quantidade*26.90
                    self.total += soma
                elif i == "Beirute":
                    self.total += quantidade*19.90
                elif i == "X-tudo":
                    self.total += quantidade*5.50
                elif i == "Batata-frita":
                    self.total +=quantidade*3.00
                elif i == "Coca-Cola 2 Litros":
                    self.total +=quantidade*8.50
                elif i == "Coca-Cola 1 Litro":
                    self.total +=quantidade*5.25



                print('Foram pedidos: '+f"({quantidade}) - "+i)
                #messagem = ''.join(f'({quantidade}) - {i}\n')

        self.listbox.insert(0, f"Total: R${self.total:.2f}".replace('.', ','))
        self.comanda_ativa=True
        time.sleep(5)

        #checagem
        if "Qual" in self.Entry5.get() or 'Qual' in self.Entry3.get() or '*obriga' in self.Entry5.get() or '*obriga' in self.Entry3.get():
            self.Entry1.delete(0, 'end')
            self.Entry2.delete(0, 'end')
            self.Entry3.delete(0, 'end')
            self.Entry4.delete(0, 'end')
            self.Entry5.delete(0, 'end')
            self.Entry6.delete(0, 'end')
            self.TCombobox1.delete(0, 'end')
            self.TCombobox2.delete(0,'end')
            self.listbox.delete(0, 'end')
        if self.Entry1.get() == "" or self.Entry2.get() == "" or self.Entry3.get() == "" or self.Entry4.get() == "" or self.Entry5.get() == "" or self.Entry6.get() == "" or self.combobox.get() == "" or self.combobox2 == "":
            self.Button3.configure(background='#d90005')
            self.Entry1.insert(0, '*obrigatório!')
            self.Entry1.config(fg='red')
            self.Entry2.insert(0, '*obrigatório!')
            self.Entry2.config(fg='red')
            self.Entry3.insert(0, '*obrigatório!')
            self.Entry3.config(fg='red')
            self.Entry4.insert(0, '*obrigatório!')
            self.Entry4.config(fg='red')
            self.Entry5.insert(0, '*obrigatório!')
            self.Entry5.config(fg='red')
            self.Entry6.insert(0, '*obrigatório!')
            self.Entry6.config(fg='red')
            self.TCombobox1.insert(0, '*obrigatório!')
            self.TCombobox2.insert(0, '*obrigatório!')
            return

        #nova janela
        self.Entry1.destroy()
        self.Entry2.destroy()
        self.Entry3.destroy()
        self.Entry4.destroy()
        self.Entry5.destroy()
        self.Entry6.destroy()
        self.listbox.destroy()
        self.Message1.destroy()
        self.Message2.destroy()
        self.Message3.destroy()
        self.Message4.destroy()
        self.Message5.destroy()
        self.Message6.destroy()
        self.Message7.destroy()
        self.Message8.destroy()
        self.Message9.destroy()
        self.Message10.destroy()
        self.scrollbar.destroy()
        self.TCombobox1.destroy()
        self.Button1.destroy()
        self.Button2.destroy()
        self.Button3.destroy()

        self.Message1 = tk.Message(self.top)
        self.Message1.place(relx=0.037, rely=0.0, relheight=0.156
                            , relwidth=0.963)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Message1.configure(foreground="#944ff2")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(padx="1")
        self.Message1.configure(pady="1")
        self.Message1.configure(text='''POINT - Restaurante''')
        self.Message1.configure(width=260)

        self.TSeparator1 = ttk.Separator(self.top)
        self.TSeparator1.place(relx=-0.074, rely=0.136, relwidth=1.259)

        self.Message2 = tk.Message(self.top)
        self.Message2.place(relx=0.148, rely=0.158, relheight=0.066
                            , relwidth=0.704)
        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(padx="1")
        self.Message2.configure(pady="1")
        self.Message2.configure(text=f'{self.nome}')
        self.Message2.configure(width=190)

        self.Message3 = tk.Message(self.top)
        self.Message3.place(relx=0.0, rely=0.339, relheight=0.088, relwidth=1.0)
        self.Message3.configure(background="#d9d9d9")
        self.Message3.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Message3.configure(foreground="#213dfa")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(padx="1")
        self.Message3.configure(pady="1")
        self.Message3.configure(text='''Seu pedido está a caminho!''')
        self.Message3.configure(width=240)


        self.TSeparator2 = ttk.Separator(self.top)
        self.TSeparator2.place(relx=-0.037, rely=0.43, relwidth=1.185)

        self.Message4 = tk.Message(self.top)
        self.Message4.place(relx=-0.037, rely=0.452, relheight=0.133
                            , relwidth=1.037)
        self.Message4.configure(background="#d9d9d9")
        self.Message4.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Message4.configure(foreground="#53a40b")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(padx="1")
        self.Message4.configure(pady="1")
        self.Message4.configure(text='''Previsão para entrega de 40-50 minutos.''')
        self.Message4.configure(width=280)

        self.TSeparator3 = ttk.Separator(self.top)
        self.TSeparator3.place(relx=0.0, rely=0.588, relwidth=1.0)
        self.TSeparator3.configure(cursor="fleur")

        self.Message5 = tk.Message(self.top)
        self.Message5.place(relx=0.0, rely=0.611, relheight=0.133, relwidth=1.0)
        self.Message5.configure(background="#d9d9d9")
        self.Message5.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#d9d9d9")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(padx="1")
        self.Message5.configure(pady="1")
        self.Message5.configure(text='''Entre em contato conosco via telefone.''')
        self.Message5.configure(width=270)

        self.Message6 = tk.Message(self.top)
        self.Message6.place(relx=0.0, rely=0.792, relheight=0.088
                            , relwidth=0.852)
        self.Message6.configure(background="#d9d9d9")
        self.Message6.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(padx="1")
        self.Message6.configure(pady="1")
        self.Message6.configure(text='''SAC: (81) 9-84757192''')
        self.Message6.configure(width=230)

        self.Message7 = tk.Message(self.top)
        self.Message7.place(relx=0.107, rely=0.226, relheight=0.066
                            , relwidth=0.481)
        self.Message7.configure(background="#d9d9d9")
        self.Message7.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Message7.configure(foreground="#000000")
        self.Message7.configure(highlightbackground="#d9d9d9")
        self.Message7.configure(highlightcolor="black")
        self.Message7.configure(padx="1")
        self.Message7.configure(pady="1")
        self.Message7.configure(text='''Valor total: 1''')
        self.Message7.configure(width=130)

        self.Message8 = tk.Message(self.top)
        self.Message8.place(relx=0.10, rely=0.294, relheight=0.066
                            , relwidth=0.704)
        self.Message8.configure(background="#d9d9d9")
        self.Message8.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Message8.configure(foreground="#000000")
        self.Message8.configure(highlightbackground="#d9d9d9")
        self.Message8.configure(highlightcolor="black")
        self.Message8.configure(padx="1")
        self.Message8.configure(pady="1")
        self.Message8.configure(text=f'Forma de pagamento: {self.pagamento}')
        self.Message8.configure(width=190)


def main(*args):
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = clientes(_top1)
    root.mainloop()

if __name__ == '__main__':
    main()
