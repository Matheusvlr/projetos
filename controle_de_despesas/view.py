# importação do SQLite
import sqlite3 as lite

# conexão
con = lite.connect('dados.db')

# inserção da categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Categoria (nome) VALUES (?)'
        cur.execute(query,i)

# inserção de Receitas
def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Receitas (categoria, adicionando_em,valor) VALUES (?,?,?)'
        cur.execute(query,i)
        
# inserção de Gastos
def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Gastos (categoria, retirado_em,valor) VALUES (?,?,?)'
        cur.execute(query,i)

# ----------------------------- funções para deletar --------------------------

# deletar Receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Receitas WHERE id=?'
        cur.execute(query, i)

# deletar Gastos
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Gastos WHERE id=?'
        cur.execute(query, i)

# --------------------------- funções para ver dados ---------------------------

# ------------------ Ver categoria ----------------------
def ver_categoria():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Categoria')
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens


# ------------------ Ver Receitas ----------------------
def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Receitas')
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

# ------------------ Ver Gastos ----------------------
def ver_gastos():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Gastos')
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

