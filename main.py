import tkinter as tk
from tkinter import ttk
from tkinter import *
import datetime as dt
from collections import Counter


lista_pratos = ["pizza","beirute","x-tudo"]
caches_produtos = {"pizza": 0,"beirute": 0,"x-tudo":0}


class clientes:
    def __init__(self, top=None):
        top.geometry("268x441+383+106")
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
        self.Message2.place(relx=0.0, rely=0.2, relheight=0.043, relwidth=0.304)
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
        self.TCombobox1.place(relx=0.226, rely=0.621, relheight=0.048
                , relwidth=0.389)
        self.combobox.set('Selecione')
        self.TCombobox1.configure(textvariable=self.combobox)
        self.TCombobox1.configure(takefocus="tt")

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.634, rely=0.621, height=24, width=27)
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
        self.Button2.place(relx=0.747, rely=0.621, height=24, width=27)
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
        self.Button3.place(relx=0.039, rely=0.907, height=34, width=237)
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
        self.listbox.delete(self.listbox.curselection())

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
        if n == "Selecione":
            return
        else:
            self.listbox.insert(0, n)
            caches_produtos[f'{n}'] += 1

    def finalizar(self):
        self.combobox.get()
        size = self.listbox.size()
        items = self.listbox.get(0, size)
        counter = Counter(items)
        for i in reversed(range(size)):
            self.listbox.delete(i)
        for i, pairs in enumerate(counter.items()):
            k, v = pairs
            if v > 1:
                self.listbox.insert(i, f"{k} ({v})")
            else:
                self.listbox.insert(i, k)
        for i in caches_produtos.keys():
            quantidade = caches_produtos[i]
            if quantidade >=1:
                print('Foram pedidos: '+f"({quantidade})"+i)

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
