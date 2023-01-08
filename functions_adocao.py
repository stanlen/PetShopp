import sqlite3 as lite
from tkinter import *

class functions():

    def limpar_campos(self):
        self.entry_pesquisa.delete(0, END)
        self.entry_id_cliente.delete(0, END)
        self.entry_nome_cliente.delete(0, END)
        self.entry_id_pet.delete(0, END)
        self.entry_nome_pet.delete(0, END)
        self.entry_dtadocao.delete(0, END)

    def limpar_campos_clientes(self):
        self.entry_pesquisa.delete(0, END)
        self.entry_id_cliente.delete(0, END)
        self.entry_nome_cliente.delete(0, END)

    def limpar_campos_pet(self):
        self.entry_pesquisa.delete(0, END)
        self.entry_id_pet.delete(0, END)
        self.entry_nome_pet.delete(0, END)


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
               CREATE TABLE IF NOT EXISTS adocao( 
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   id_cliente INT,
                   nome_cliente VARCHAR(50),
                   id_pet INT,
                   nome_pet VARCHAR(50), 
                   dtadocao DATE, 
                   FOREIGN KEY('id_cliente') REFERENCES 'clientes'('id') ON DELETE CASCADE,
                   FOREIGN KEY('id_pet') REFERENCES 'pets'('id') ON DELETE CASCADE,
                   FOREIGN KEY('nome_cliente') REFERENCES 'clientes'('Nome') ON DELETE CASCADE,
                   FOREIGN KEY('nome_pet') REFERENCES 'pets'('Nome') ON DELETE CASCADE);""")


        self.conexao.commit()
        print("banco de dados criado")
        self.db_desconect()

    def capturar_campos(self):
        self.pesquisa = self.entry_pesquisa.get()
        self.id_cliente = self.entry_id_cliente.get()
        self.nome_cliente = self.entry_nome_cliente.get()
        self.id_pet = self.entry_id_pet.get()
        self.nome_pet = self.entry_nome_pet.get()
        self.dtadocao = self.entry_dtadocao.get()

    def add_adocao(self):
        # obter dados dos campos
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""INSERT INTO adocao (id_cliente, nome_cliente, id_pet, nome_pet, dtadocao)
            VALUES(?,?,?,?,?)""", (self.id_cliente, self.nome_cliente, self.id_pet, self.nome_pet, self.dtadocao))
        self.conexao.commit()
        self.db_desconect()
        #self.select_lista()
        self.limpar_campos()
        


    def select_lista(self):
        self.lista_grid.delete(*self.lista_grid.get_children())
        self.db_conect()
        lista = self.cursor.execute("""SELECT id, id_cliente, nome_cliente, id_pet, nome_pet, dtadocao
            FROM adocao ORDER BY id DESC;""")
        for l in lista:
            self.lista_grid.insert("", END, values=l)
        self.db_desconect()

    def OnDubleClick(self, event):
        self.limpar_campos()
        self.lista_grid.selection()

        for x in self.lista_grid.selection():
            col0, col1, col2, col3, col4, col5 = self.lista_grid.item(x, 'values')

            self.entry_pesquisa.insert(END, col0)
            self.entry_id_cliente.insert(END, col1)
            self.entry_nome_cliente.insert(END, col2)
            self.entry_id_pet.insert(END, col3)
            self.entry_nome_pet.insert(END, col4)
            self.entry_dtadocao.insert(END, col5)

    def OnDubleClick_clientes(self, event):
        self.limpar_campos_clientes()
        self.lista_cliente_grid.selection()

        for x in self.lista_cliente_grid.selection():
            col0, col1, col2, col3, col4 = self.lista_cliente_grid.item(x, 'values')

            self.entry_id_cliente.insert(END, col0)
            self.entry_nome_cliente.insert(END, col1)

    def OnDubleClick_pet(self, event):
        self.limpar_campos_pet()
        self.listar_pet_grid.selection()

        for x in self.listar_pet_grid.selection():
            col0, col1, col2, col3 = self.listar_pet_grid.item(x, 'values')

            self.entry_id_pet.insert(END, col0)
            self.entry_nome_pet.insert(END, col1)



    def deleta_adocao(self):
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute(
            """DELETE FROM adocao WHERE id = ?""", [self.pesquisa])
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()
        self.select_lista()
#retirar
    def alterar_cliente(self):
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""UPDATE adocao SET id_cliente = ?, nome_cliente = ?, id_pet = ?, nome_pet = ? WHERE id = ?;
            """, (self.nome, self.sobrenome, self.telefone, self.email, self.pesquisa))
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()
        self.select_lista()

    def Buscar_adocao(self):
        self.db_conect()
        self.limpar_campos()


        self.lista_grid.delete(*self.lista_grid.get_children())

        self.entry_pesquisa.insert(END, '%')
        nome = '%'+self.entry_pesquisa.get()
        self.cursor.execute(
            """SELECT * FROM adocao WHERE Nome LIKE '%s' COLLATE NOCASE ORDER BY Nome DESC""" % nome)
        Resultado_busca = self.cursor.fetchall()
        for adocao in Resultado_busca:
            self.lista_grid.insert("", END, values=adocao)

    
    def Buscar_cliente(self):
        self.db_conect()
        self.lista_cliente_grid.delete(*self.lista_cliente_grid.get_children())

        self.entry_nome_cliente.insert(END, '%')
        nome = '%'+self.entry_nome_cliente.get()
        self.cursor.execute(
            """SELECT * FROM clientes WHERE Nome LIKE '%s' COLLATE NOCASE ORDER BY Nome DESC""" % nome)
        Resultado_busca = self.cursor.fetchall()
        for cliente in Resultado_busca:
            self.lista_cliente_grid.insert("", END, values=cliente)


    def Buscar_pet(self):
        self.db_conect()
        self.listar_pet_grid.delete(*self.listar_pet_grid.get_children())

        self.entry_nome_pet.insert(END, '%')
        nome = '%'+self.entry_nome_pet.get()
        self.cursor.execute(
            """SELECT * FROM pets WHERE Nome LIKE '%s' COLLATE NOCASE ORDER BY Nome DESC""" % nome)
        Resultado_busca = self.cursor.fetchall()
        for pets in Resultado_busca:
            self.listar_pet_grid.insert("", END, values=pets)

        self.db_desconect()
        self.limpar_campos_pet()
        self.db_desconect()
