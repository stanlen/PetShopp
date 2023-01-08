from cProfile import label
from tkinter import *
from tkinter import ttk
from functions import *
import tkinter as root
import Cadastro
import Cadastro_pet
import tkinter as tk
import adocao
import relatorio

class menus_lat(functions):
    def __init__(self):
        self.root = Tk()
        image = tk.PhotoImage(file='cad_pet.png')
        image = image.subsample(1,1)
        labelimage = tk.Label(image = image)
        labelimage.place(x=90,y=0,relwidth=1.0,relheight=1.0)
        self.tela()
        self.inicial()
        #self.frames_tela()
        #self.grid_cliente()
        #self.widgets_frame1()
        #self.Menus()
        #self.criar_tabela()
        #self.select_lista()
        root.mainloop()
    def botao_click1(self):
        self.root.destroy()
        Cadastro_pet.Aplication_pet()

    def botao_click2(self):
        self.root.destroy()
        Cadastro.Aplication()

    def botao_click3(self):
        self.root.destroy()
        adocao.Aplication_adocao()
        
    def botao_click4(self):
        relatorio.Relatorios()
        
    def inicial (self):

        botao_1 = Button(self.root, text = "PETS", padx = 70, pady = 47, borderwidth = 5, background='#4169E1', fg="white", font=('verdana', 8, 'bold'), command = lambda: self.botao_click1())
        botao_2 = Button(self.root, text = "CLIENTES", padx = 56, pady = 47, borderwidth = 5,background='#4169E1', fg="white", font=('verdana', 8, 'bold'), command = lambda: self.botao_click2())
        botao_3 = Button(self.root, text = "ADOÇOES", padx = 56, pady = 47, borderwidth = 5, background='#4169E1', fg="white", font=('verdana', 8, 'bold'),command = lambda: self.botao_click3())
        botao_4 = Button(self.root, text = "RELATÓRIOS", padx = 45, pady = 47, borderwidth = 5, background='#4169E1', fg="white", font=('verdana', 8, 'bold'),command = lambda: self.botao_click4())
        botao_5 = Button(self.root, text = "SAIR", padx = 70, pady = 47, borderwidth = 5,background='#4169E1', fg="white", font=('verdana', 8, 'bold') ,command = lambda: exit())

        botao_1.grid(row = 0, column = 0,columnspan=1)
        botao_2.grid(row = 1, column = 0,columnspan=1)
        botao_3.grid(row = 2, column = 0,columnspan=1)
        botao_4.grid(row = 3, column = 0,columnspan=1)
        botao_5.grid(row = 4, column = 0,columnspan=1)

    def tela(self):
        self.root.title("PetShopp")
        self.root.configure(background='#6a50c9')
        self.root.geometry("800x600+280+1")
        self.root.resizable(True, True)
        self.root.maxsize(width=850, height=700)
        self.root.minsize(width=400, height=300)


