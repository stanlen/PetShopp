from tkinter import *
from tkinter import ttk
from functions_adocao import *
import tkinter as root
import menus
import functions_adocao

class buscar_cliente(functions):
        def __init__(self):
            self.root = Tk()
            self.tela()
            self.frames_tela()
            #self.grid_adocao()
            #self.widgets_frame1()
            #self.Menus()
            #self.criar_tabela()
            #self.select_lista()
            self.grid_cliente()
            root.mainloop()

        def tela(self):
            self.root.title("PetShopp")
            self.root.configure(background='#6a50c9')
            self.root.geometry("800x600+280+1")
            self.root.resizable(True, True)
            self.root.maxsize(width=850, height=700)
            self.root.minsize(width=400, height=300)

        def frames_tela(self):
            self.frame1 = Frame(self.root, bd=4, bg="#fff",
                                highlightbackground="#b471f8", highlightthickness=3)
            self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

            self.frame2 = Frame(self.root, bd=4, bg="#fff",
                                highlightbackground="#b471f8", highlightthickness=3)
            self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        def grid_cliente(self):
            self.lista_cliente_grid = ttk.Treeview(self.frame2, height=3,
                                        column=('col1', 'col2', 'col3', 'col4', 'col5'))
            self.lista_cliente_grid.heading("#0",  text='')
            self.lista_cliente_grid.heading("#1", text='ID')
            self.lista_cliente_grid.heading("#2", text='NOME')
            self.lista_cliente_grid.heading("#3", text='SOBRENOME')
            self.lista_cliente_grid.heading("#4", text='TELEFONE')
            self.lista_cliente_grid.heading("#5", text='EMAIL')

            self.lista_cliente_grid.column("#0", width=0)
            self.lista_cliente_grid.column("#1", anchor=CENTER, width=2)
            self.lista_cliente_grid.column("#2", anchor=CENTER, width=25)
            self.lista_cliente_grid.column("#3", anchor=CENTER, width=100)
            self.lista_cliente_grid.column("#4", anchor=CENTER, width=125)
            self.lista_cliente_grid.column("#5", anchor=CENTER, width=125)
            self.lista_cliente_grid.place(relx=0.005, rely=0.1,
                                relwidth=0.95, relheight=0.86)

            self.scrol_lista = Scrollbar(self.frame2, orient='vertical')
            self.lista_cliente_grid.configure(yscroll=self.scrol_lista.set)
            self.scrol_lista.place(relx=0.96, rely=0.1,
                                relwidth=0.04, relheight=0.88)
            self.lista_cliente_grid.bind("<Double-1>", self.OnDubleClick)
buscar_cliente()