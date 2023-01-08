from logging import root
from tkinter import *
import tkinter as tk
import sqlite3 as lite
from matplotlib.pyplot import text
import pandas as pd
import webbrowser 
import canvas
from reportlab.pdfgen import  canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import  pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import  SimpleDocTemplate,Image
import  webbrowser

#Criando Janela:



class Relatorios():
    def __init__(self):
        self.inicio()
        self.root.mainloop()
        
    def mostrar(self):
        webbrowser.open('ficha_Cliente_'+self.nomerel+'.pdf')

    def Gerar_Ficha(self):
        self.codigorel = self.entry_nome.get()
        self.nomerel = self.entry_sobrenome.get()
        self.telefonerel = self.entry_telefone.get()
        self.cidaderel = self.entry_email.get()

        self.ficha_cliente = canvas.Canvas(
             'ficha_Cliente_'+self.nomerel+'.pdf')

        self.ficha_cliente.setFont("Helvetica-Bold", 20)
        self.ficha_cliente.drawString(200, 780, 'CERTIDÃO DO SEU PET')

        self.ficha_cliente.setFont("Helvetica-Bold", 20)
        self.ficha_cliente.drawString(50, 680, 'Nome do Pet: '+self.codigorel)
        self.ficha_cliente.drawString(50, 650, 'Raça: ' + self.nomerel)
        self.ficha_cliente.drawString(50, 620, 'Peso: ' + self.telefonerel)
        self.ficha_cliente.drawString(50, 590, 'Vacinas: ' + self.cidaderel)

        self.ficha_cliente.rect(20, 430, 550, 400, fill=False, stroke=True)

        self.ficha_cliente.showPage()
        self.ficha_cliente.save()
        self.mostrar()


 

    def exporta_clientes():
        conexao = lite.connect('petshopp.db')
        c = conexao.cursor()

        # Inserir dados na tabela:
        c.execute("SELECT *, oid FROM clientes")
        clientes_cadastrados = c.fetchall()
        print(clientes_cadastrados)
        clientes_cadastrados=pd.DataFrame(clientes_cadastrados,columns=['id','nome','sobrenome','email','telefone', 'teste'])
        clientes_cadastrados.to_excel('clientes.xlsx')

        # Commit as mudanças:
        conexao.commit()

        # Fechar o banco de dados:
        conexao.close()

    def inicio(self):
        root = tk.Tk()
        #Rótulos Entradas:
        label_nome = tk.Label(root, text='Nome')
        label_nome.grid(row=0,column=0, padx=10, pady=10)

        label_sobrenome = tk.Label(root, text='Sobrenome')
        label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

        label_email = tk.Label(root, text='E-mail')
        label_email.grid(row=2, column=0 , padx=10, pady=10)

        label_telefone = tk.Label(root, text='Telefone')
        label_telefone.grid(row=3, column=0, padx=10, pady=10)

        #Caixas Entradas:
        self.entry_nome = tk.Entry(root , width =35)
        self.entry_nome.grid(row=0,column=1, padx=10, pady=10)

        self.entry_sobrenome = tk.Entry(root, width =35)
        self.entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

        self.entry_email = tk.Entry(root, width =35)
        self.entry_email.grid(row=2, column=1 , padx=10, pady=10)

        self.entry_telefone = tk.Entry(root, width =35)
        self.entry_telefone.grid(row=3, column=1, padx=10, pady=10)

        # Botão de Cadastrar

        self.botao_cadastrar = tk.Button(root,text='Gerar',
                                    command=self.Gerar_Ficha())
        self.botao_cadastrar.grid(row=4, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)
        root.destroy()
        self.botao_cadastrar.destroy()
        self.entry_telefone.destroy()
        self.entry_sobrenome.destroy()
        self.entry_nome.destroy()
        self.entry_email.destroy()