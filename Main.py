import tkinter as tk
from tkinter import CENTER, END, NO,  W, Button, Frame, ttk
import sqlite3 as lite


# def db_conect(self):
#     self.conexao = lite.connect('clientes.db')
#     self.cursor = self.conexao.cursor()
#     print("conectando ao banco de dados")


# def select_lista(self):
#     self.conexao = lite.connect('clientes.db')
#     self.cursor = self.conexao.cursor()
#     print("conectando ao banco de dados")
#     lista = self.cursor.execute("""SELECT id, Nome, Sobrenome, Telefone, Email
#             FROM clientes ORDER BY nome DESC;""")
#     for l in lista:
#         self.my_table.insert("", END, values=l)


def tester():

    conexao = lite.connect('clientes.db')
    cursor = conexao.cursor()
    print("conectando ao banco de dados")

    root = tk.Tk()
    root.title("Pet")
    root.geometry('550x400')
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Tab 1')
    tabControl.add(tab2, text='Tab 2')
    tabControl.pack(expand=1, fill="both")

    tabela = Frame(tab1)
    tabela.pack()
    my_table = ttk.Treeview(tabela)

    lista = cursor.execute("""SELECT id, Nome, Sobrenome, Telefone, Email
            FROM clientes ORDER BY nome DESC;""")
    for l in lista:
        my_table.insert("", END, values=l)

    my_table['columns'] = ('col1', 'col2', 'col3', 'col4', 'col5')
    my_table.column("#0", width=0, stretch=NO)
    my_table.column("#1", anchor=CENTER, width=50)
    my_table.column("#2", anchor=CENTER, width=100)
    my_table.column("#3", anchor=CENTER, width=100)
    my_table.column("#4", anchor=CENTER, width=100)
    my_table.column("#5", anchor=CENTER, width=200)

    my_table.heading("#0", text="", )
    my_table.heading("#1", text="id")
    my_table.heading("#2", text="Nome", )
    my_table.heading("#3", text="Sobrenome", )
    my_table.heading("#4", text="Telefone", )
    my_table.heading("#5", text="Email", )

    # my_table.insert(parent='', index='end', iid=0, text='',
    #                 values=('1', 'Ninja', '101', 'Oklahoma', 'Moore'))
    # my_table.insert(parent='', index='end', iid=1, text='',
    #                 values=('2', 'Ranger', '102', 'Wisconsin', 'Green Bay'))
    # my_table.insert(parent='', index='end', iid=2, text='',
    #                 values=('3', 'Deamon', '103', 'California', 'Placentia'))
    # my_table.insert(parent='', index='end', iid=3, text='',
    #                 values=('4', 'Dragon', '104', 'New York', 'White Plains'))
    # my_table.insert(parent='', index='end', iid=4, text='',
    #                 values=('5', 'CrissCross', '105', 'California', 'San Diego'))
    # my_table.insert(parent='', index='end', iid=5, text='',
    #                 values=('6', 'ZaqueriBlack', '106', 'Wisconsin', 'TONY'))

    my_table.pack()

    # button
    Input_button = Button(tab1, text="Cadastrar", command='')
    Input_button.pack()

    ttk.Label(tab2,
              text="Lets dive into the\
              world of computers").grid(column=0,
                                        row=0,
                                        padx=30,
                                        pady=30)

    root.mainloop()
