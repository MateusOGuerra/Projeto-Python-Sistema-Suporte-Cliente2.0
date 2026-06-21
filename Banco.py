import sqlite3

conexao = sqlite3.connect("Cadastro.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

conexao.commit()

print("Banco criado com sucesso!")