from tkinter import *
from tkinter import ttk
from functions import *
import tkinter as root
import menus


class Aplication(functions):
    def __init__(self):
        self.root = Tk()
        self.tela()
        self.frames_tela()
        self.grid_cliente()
        self.widgets_frame1()
        self.Menus()
        self.criar_tabela()
        self.select_lista()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
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

    def widgets_frame1(self):
        # botão limpar
        self.bt_buscar = Button(self.frame1, text="Buscar",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command=self.Buscar_Cliente)
        self.bt_buscar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # botão Buscar
        self.bt_limpar = Button(self.frame1, text="Limpar",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command=self.limpar_campos)
        self.bt_limpar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # botão Novo
        self.bt_novo = Button(self.frame1, text="Novo",
                              bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão Altera
        self.bt_alterar = Button(self.frame1, text="Alterar",
                                 bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command=self.alterar_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão Apagar
        self.bt_apagar = Button(self.frame1, text="Apagar",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        self.lb_pesquisa = Label(self.frame1, text="Pesquisar",
                                 bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_pesquisa.place(relx=0.05, rely=0.05)

        self.entry_pesquisa = Entry(self.frame1, text="pesquisa",
                                    bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_pesquisa.place(relx=0.05, rely=0.15, relwidth=0.12)

        # label e entry - nome ----------------------------------
        self.lb_nome = Label(self.frame1, text="Nome",
                             bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.entry_nome = Entry(self.frame1,
                                bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_nome.place(relx=0.05, rely=0.45, relwidth=0.2)

        # label e entry - Telfone--------------------------
        self.lb_sobrenome = Label(self.frame1, text="Sobrenome",
                                  bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_sobrenome.place(relx=0.35, rely=0.35)

        self.entry_sobrenome = Entry(self.frame1,
                                     bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_sobrenome.place(relx=0.35, rely=0.45, relwidth=0.3)

        # label e entry - Cidade -----------------------
        self.lb_telefone = Label(self.frame1, text="Telefone",
                                 bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.entry_telefone = Entry(self.frame1,
                                    bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_telefone.place(relx=0.05, rely=0.7, relwidth=0.2)

        # label e entry - Cidade -----------------------
        self.lb_email = Label(self.frame1, text="Email",
                              bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_email.place(relx=0.3, rely=0.6)

        self.entry_email = Entry(self.frame1,
                                 bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_email.place(relx=0.3, rely=0.7, relwidth=0.4)

    def grid_cliente(self):
        self.lista_grid = ttk.Treeview(self.frame2, height=3,
                                       column=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.lista_grid.heading("#0",  text='')
        self.lista_grid.heading("#1", text='ID')
        self.lista_grid.heading("#2", text='NOME')
        self.lista_grid.heading("#3", text='SOBRENOME')
        self.lista_grid.heading("#4", text='TELEFONE')
        self.lista_grid.heading("#5", text='EMAIL')

        self.lista_grid.column("#0", width=0)
        self.lista_grid.column("#1", anchor=CENTER, width=2)
        self.lista_grid.column("#2", anchor=CENTER, width=25)
        self.lista_grid.column("#3", anchor=CENTER, width=100)
        self.lista_grid.column("#4", anchor=CENTER, width=125)
        self.lista_grid.column("#5", anchor=CENTER, width=125)
        self.lista_grid.place(relx=0.005, rely=0.1,
                              relwidth=0.95, relheight=0.86)

        self.scrol_lista = Scrollbar(self.frame2, orient='vertical')
        self.lista_grid.configure(yscroll=self.scrol_lista.set)
        self.scrol_lista.place(relx=0.96, rely=0.1,
                               relwidth=0.04, relheight=0.88)
        self.lista_grid.bind("<Double-1>", self.OnDubleClick)

    def sair(self):
        self.root.destroy()
        menus.menus_lat()

    def Menus(self):
        Menubar = Menu(self.root)
        self.root.config(menu=Menubar)
        filemenu = Menu(Menubar)
        def Quit(): self.root.destroy()

        Menubar.add_cascade(label="opções", menu=filemenu)

        filemenu.add_command(label="Voltar", command=lambda:self.sair())
    

