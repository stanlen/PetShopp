from distutils.cmd import Command
from tkinter import *
from tkinter import ttk
from functions_adocao import *
import tkinter as root
import menus
import functions_adocao


class Aplication_adocao(functions):
    def __init__(self):
        self.root = Tk()
        self.tela()
        self.frames_tela()
        self.grid_adocao()
        self.widgets_frame1()
        self.Menus()
        self.criar_tabela()
        self.select_lista()
        root.mainloop()

    def tela(self):
        self.root.title("Adoção de Pet")
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
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command = lambda: self.mostrar_adocao())
        self.bt_buscar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)


        # botão Buscar
        self.bt_limpar = Button(self.frame1, text="Limpar",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command=self.limpar_campos)
        self.bt_limpar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # botão Novo
        self.bt_novo = Button(self.frame1, text="Novo",
                              bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command=self.add_adocao)
        self.bt_novo.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão Altera
        #self.bt_alterar = Button(self.frame1, text="Alterar",
        #                         bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command=self.alterar_cliente)
        #self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão Apagar
        self.bt_apagar = Button(self.frame1, text="Cancelar",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command=self.deleta_adocao)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        self.lb_pesquisa = Label(self.frame1, text="Pesquisar",
                                 bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_pesquisa.place(relx=0.05, rely=0.05)

        self.entry_pesquisa = Entry(self.frame1, text="pesquisa",
                                    bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_pesquisa.place(relx=0.05, rely=0.15, relwidth=0.12)

        # label e entry - nome ----------------------------------
        self.lb_id_cliente = Label(self.frame1, text="COD TUTOR",
                             bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_id_cliente.place(relx=0.05, rely=0.35)

        self.entry_id_cliente = Entry(self.frame1,
                                bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_id_cliente.place(relx=0.05, rely=0.45, relwidth=0.2)

        # label e entry - Telfone--------------------------
        self.lb_nome_cliente = Label(self.frame1, text="NOME TUTOR",
                                  bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_nome_cliente.place(relx=0.35, rely=0.35)

        self.entry_nome_cliente = Entry(self.frame1,
                                     bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_nome_cliente.place(relx=0.35, rely=0.45, relwidth=0.3)


        self.bt_buscar = Button(self.frame1, text="Buscar",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command = lambda: self.botao_click1())
        self.bt_buscar.place(relx=0.70, rely=0.45, relwidth=0.2, relheight=0.15)


        # label e entry - Cidade -----------------------
        self.lb_id_pet= Label(self.frame1, text="COD PET",
                                 bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_id_pet.place(relx=0.05, rely=0.6)

        self.entry_id_pet = Entry(self.frame1,
                                    bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_id_pet.place(relx=0.05, rely=0.7, relwidth=0.2)

        # label e entry - Cidade -----------------------
        self.lb_nome_pet = Label(self.frame1, text="NOME PET",
                                 bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_nome_pet.place(relx=0.35, rely=0.6)

        self.entry_nome_pet = Entry(self.frame1,
                                    bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_nome_pet.place(relx=0.35, rely=0.7, relwidth=0.3)

        self.bt_buscar = Button(self.frame1, text="Buscar",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command = lambda: self.botao_click2())
        self.bt_buscar.place(relx=0.70, rely=0.7, relwidth=0.2, relheight=0.15)

        # label e entry - Cidade -----------------------
        self.lb_dtadocao = Label(self.frame1, text="DATA ADOÇÃO",
                                 bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_dtadocao.place(relx=0.05, rely=0.8)

        self.entry_dtadocao = Entry(self.frame1,
                                    bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_dtadocao.place(relx=0.05, rely=0.9, relwidth=0.2)

    def botao_click1(self):
        self.frame2.destroy()

        self.frame3 = Frame(self.root, bd=4, bg="#fff",
                            highlightbackground="#b471f8", highlightthickness=3)
        self.frame3.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        self.lista_cliente_grid = ttk.Treeview(self.frame3, height=3,
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

        self.scrol_lista = Scrollbar(self.frame3, orient='vertical')
        self.lista_cliente_grid.configure(yscroll=self.scrol_lista.set)
        self.scrol_lista.place(relx=0.96, rely=0.1,
                              relwidth=0.04, relheight=0.88)
        self.lista_cliente_grid.bind("<Double-1>", self.OnDubleClick_clientes)
        functions_adocao.functions.Buscar_cliente(self)

    def mostrar_adocao(self):
        self.root.destroy()
        Aplication_adocao()
    def botao_click2(self):
        self.frame2.destroy()


        self.frame4 = Frame(self.root, bd=4, bg="#fff",
                            highlightbackground="#b471f8", highlightthickness=3)
        self.frame4.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        self.listar_pet_grid = ttk.Treeview(self.frame4, height=3,
                                       column=('col1', 'col2', 'col3', 'col4'))
        self.listar_pet_grid.heading("#0",  text='')
        self.listar_pet_grid.heading("#1", text='ID')
        self.listar_pet_grid.heading("#2", text='NOME')
        self.listar_pet_grid.heading("#3", text='RAÇA')
        self.listar_pet_grid.heading("#4", text='DATA DE NASCIMENTO')

        self.listar_pet_grid.column("#0", width=0)
        self.listar_pet_grid.column("#1", anchor=CENTER, width=2)
        self.listar_pet_grid.column("#2", anchor=CENTER, width=25)
        self.listar_pet_grid.column("#3", anchor=CENTER, width=100)
        self.listar_pet_grid.column("#4", anchor=CENTER, width=125)
        self.listar_pet_grid.place(relx=0.005, rely=0.1,
                              relwidth=0.95, relheight=0.86)

        self.scrol_lista = Scrollbar(self.frame4, orient='vertical')
        self.listar_pet_grid.configure(yscroll=self.scrol_lista.set)
        self.scrol_lista.place(relx=0.96, rely=0.1,
                               relwidth=0.04, relheight=0.88)
        self.listar_pet_grid.bind("<Double-1>", self.OnDubleClick_pet)
        functions_adocao.functions.Buscar_pet(self)

    

    def grid_adocao(self):
        self.lista_grid = ttk.Treeview(self.frame2, height=3,
                                       column=('col0', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6'))
        self.lista_grid.heading("#0", text='#')
        self.lista_grid.heading("#1", text='id')
        self.lista_grid.heading("#2", text='ID_TUTOR')
        self.lista_grid.heading("#3", text='NOME TUTOR')
        self.lista_grid.heading("#4", text='ID_PET')
        self.lista_grid.heading("#5", text='NOME PET')
        self.lista_grid.heading("#6", text='DATA ADOÇÃO')

        self.lista_grid.column("#0", anchor=CENTER, width=0)
        self.lista_grid.column("#1", anchor=CENTER, width=50)
        self.lista_grid.column("#2", anchor=CENTER, width=70)
        self.lista_grid.column("#3", anchor=CENTER, width=150)
        self.lista_grid.column("#4", anchor=CENTER, width=110)
        self.lista_grid.column("#5", anchor=CENTER, width=150)
        self.lista_grid.column("#6", anchor=CENTER, width=160)
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
    
