# importação do SQLite
import sqlite3 as lite
import pandas as pd

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
        query = 'INSERT INTO Receitas (categoria, adicionado_em,valor) VALUES (?,?,?)'
        cur.execute(query,i)
        
# inserção de Gastos
def inserir_gastos(i):
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

# funcao para dados da tabela
def tabela():
    gastos = ver_gastos()
    receitas = ver_receitas()

    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista

# funções para dados do gráfico de barra
def bar_valores():
    # receita total
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)
    
    # despesas totais
    gastos = ver_gastos()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])

    gasto_total = sum(gastos_lista)

    # saldo total
    saldo_total = receita_total - gasto_total

    return [receita_total, gasto_total, saldo_total]

# função gráfico pizza
def pie_valores():
    gastos = ver_gastos()
    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    dataframe = pd.DataFrame(tabela_lista, columns = ['id', 'categoria', 'Data', 'Valor'])
    dataframe = dataframe.groupby('Categoria')['valor'].sum()

    lista_quantias

