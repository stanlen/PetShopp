# importando o SQLite
import sqlite3 as lite

# Criando conexão
con = lite.connect('clientes.db')

# criação das tabelas ===========================================

# Criando tabela Categoria
# with con:
#     cur = con.cursor()
#     cur.execute(
#         "CREATE TABLE Categoria(id INTEGER, nome TEXT, PRIMARY KEY('id' AUTOINCREMENT))")

# Criando tabela Livro
# with con:
#     cur = con.cursor()
#     cur.execute("CREATE TABLE Livro(id INTEGER, titlo TEXT, actor TEXT, editora TEXT, categoria INTEGER, copias INT, adicionado_em DATE, PRIMARY KEY ('id' AUTOINCREMENT), FOREIGN KEY('categoria') REFERENCES 'Categoria' ('id') ON DELETE CASCADE)")

# Criando tabela Membro
# with con:
#     cur = con.cursor()
#     cur.execute(
#         "CREATE TABLE cliente(id INTEGER, nome TEXT, sobrenome TEXT, email TEXT, telefone TEXT , PRIMARY KEY('id' AUTOINCREMENT))")

# Criando tabela Livros_Alugados
# with con:
#     cur = con.cursor()
#     cur.execute("CREATE TABLE Livros_Alugado( id INTEGER, id_livro INT, id_membro INT, alugado_em DATEdata_de_retorno DATE, PRIMARY KEY('id' AUTOINCREMENT),FOREIGN KEY('id_livro') REFERENCES 'Livro'('id') ON DELETE CASCADE,FOREIGN KEY('id_membro') REFERENCES 'Membro'('id') ON DELETE CASCADE  )")


# querys para CRUD ===================================================================

with con:
    cur = con.cursor()
    query = "DELETE FROM clientes WHERE id = 10"
    cur.execute(query)


listar = []
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Livro")
    rows = cur.fetchall()

    for i in rows:
        listar.append(i)

print(listar)

with con:
    cur = con.cursor()
    query = "UPDATE Livro SET titlo=?  WHERE id=?"
    cur.execute(query)


valores = ['Wild', 'Azevedo', 'wild@mail.com', '8585987755']

with con:
    cur = con.cursor()
    query = "INSERT INTO cliente(nome, sobrenome, email, telefone) VALUES(?,?,?,?)"
    cur.execute(query, valores)
