import sqlite3 as lite
from tkinter import *


class functions():

    def limpar_campos(self):
        self.entry_pesquisa.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_raca.delete(0, END)
        self.entry_dtnasc.delete(0, END)

    def db_conect(self):
        self.conexao = lite.connect('petshopp.db')
        self.cursor = self.conexao.cursor()
        print("conectando ao banco de dados")

    def db_desconect(self):
        self.conexao.close()
        print("Desconectando ao banco de dados sqlite3")

    def criar_tabela(self):
        self.db_conect()
        # Criando uma tabela se ela não existir
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pets(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome VARCHAR(50) NOT NULL,
                raca VARCHAR(50) NOT NULL,
                dtnasc DATE NOT NULL);""")
        self.conexao.commit()
        print("banco de dados criado")
        self.db_desconect()

    def capturar_campos(self):
        self.pesquisa = self.entry_pesquisa.get()
        self.nome = self.entry_nome.get()
        self.raca = self.entry_raca.get()
        self.dtnasc = self.entry_dtnasc.get()

    def add_pets(self):
        # obter dados dos campos
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""INSERT INTO pets (Nome, raca, dtnasc)
            VALUES(?,?,?)""", (self.nome, self.raca, self.dtnasc))
        self.conexao.commit()
        self.db_desconect()
        self.select_lista()
        self.limpar_campos()

    def select_lista(self):
        self.lista_grid.delete(*self.lista_grid.get_children())
        self.db_conect()
        lista = self.cursor.execute("""SELECT id, Nome, raca, dtnasc
            FROM pets ORDER BY id DESC;""")
        for l in lista:
            self.lista_grid.insert("", END, values=l)
        self.db_desconect()

    def OnDubleClick(self, event):
        self.limpar_campos()
        self.lista_grid.selection()

        for x in self.lista_grid.selection():
            col0, col1, col2, col3 = self.lista_grid.item(x, 'values')

            self.entry_pesquisa.insert(END, col0)
            self.entry_nome.insert(END, col1)
            self.entry_raca.insert(END, col2)
            self.entry_dtnasc.insert(END, col3)

    def deleta_pets(self):
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute(
            """DELETE FROM pets WHERE id = ?""", [self.pesquisa])
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()
        self.select_lista()

    def alterar_pets(self):
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""UPDATE pets SET Nome = ?, raca = ?, dtnasc = ? WHERE id = ?;
            """, (self.nome, self.raca, self.dtnasc, self.pesquisa))
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()
        self.select_lista()

    def Buscar_pets(self):
        self.db_conect()
        self.lista_grid.delete(*self.lista_grid.get_children())

        self.entry_pesquisa.insert(END, '%')
        nome = '%'+self.entry_pesquisa.get()
        self.cursor.execute(
            """SELECT * FROM pets WHERE Nome LIKE '%s' COLLATE NOCASE ORDER BY Nome DESC""" % nome)
        Resultado_busca = self.cursor.fetchall()
        for pets in Resultado_busca:
            self.lista_grid.insert("", END, values=pets)

        self.db_desconect()
        self.limpar_campos()
        self.db_desconect()
