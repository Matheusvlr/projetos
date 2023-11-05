# importação do SQLite
import sqlite3 as lite

# conexão
con = lite.connect('dados.db')

# criação da tabela de categoria
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)')

# criação da tabela de receitas
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)')

# criação da tabela de gastos
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)')


