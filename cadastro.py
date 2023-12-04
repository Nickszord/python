import sqlite3

conn = sqlite3.connect('pessoas.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    email TEXT,
                    telefone INTEGER,
                    idade INTEGER,
                )''')

conn.commit()


def criar_pessoa(nome, email, telefone, idade):
    cursor.execute('''INSERT INTO Pessoa (nome, email, telefone, idade)
                    VALUES (?, ?, ?, ?)''', (nome, email, telefone, idade))
    conn.commit()

def ler_todas_pessoas():
    cursor.execute('''SELECT * FROM Pessoa''')
    return cursor.fetchall()

def atualizar_pessoa(id_pessoa, nome, email, telefone, idade):
    cursor.execute('''UPDATE Pessoa SET nome=?, email=?, telefone=?, idade=?
                    WHERE id=?''', (nome, email, telefone, idade, id_pessoa))
    conn.commit()

def deletar_pessoa(id_pessoa):
    cursor.execute('''DELETE FROM Pessoa WHERE id=?''', (id_pessoa,))
    conn.commit()


conn.close()