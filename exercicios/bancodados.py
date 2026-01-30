import sqlite3

# Conectar ao meu db (ou criar algum)
conexao = sqlite3.connect("/dados.db")

# Aqui vou criar a ponte entre o python e meu db
cursor = conexao.cursor()

#criar a tabela para o db

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    idade INTEGER
)
""")

# inserir dados dos usuarios

cursor.execute("""
INSERT INTO usuarios (nome, email, idade)
VALUES (?, ?, ?)
""", ("joao", "joao@email.com", 25))

# salva a conexao

conexao.commit()

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)
    
# fechando a conexao

conexao.close()
    

