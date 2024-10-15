import sqlite3
import os
import sys

# Classe que realiza as operações no banco de dados
class Transaction:
    def __init__(self):
        self.connected = False
        self.conn = None
        self.cursor = None
        self.database = 'cadastro.db'

        base_dir = os.path.dirname(os.path.abspath(sys.executable)) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
        self.database = os.path.join(base_dir, 'cadastro.db')

    # Realiza a conexao com o banco de dados
    def Connect(self):
        self.conn = sqlite3.connect(self.database)  # Conexão com SQLite
        self.cursor = self.conn.cursor()
        self.connected = True

    # Fecha a conexao com o banco de dados
    def Disconnect(self):
        if self.cursor:  # Verifica se o cursor foi criado
            self.cursor.close()  # Fecha o cursor antes
        if self.conn:  # Verifica se a conexão foi criada
            self.conn.close()  # Fecha a conexão
        self.connected = False

    # Função que executa os comando sql
    def Execute(self, sql):
        if self.connected:
            self.cursor.execute(sql)
            return True
        else:
            return False

    # Realiza a busca de items do banco de dados
    def Fetchall(self):
        return self.cursor.fetchall()

    # Salva as operações realizadas no banco
    def Commit(self):
        if self.connected:
            self.conn.commit()
            return True
        else:
            return False

def criarBanco():
    op = Transaction()
    op.Connect()
    op.Execute("CREATE TABLE IF NOT EXISTS cadastro (nome TEXT NOT NULL, senha NOT NULL)")
    op.Commit()
    op.Disconnect()

#armazena as informaçoes do usario no banco
def create(nome, senha):
    operacoes = Transaction()
    operacoes.Connect()
    operacoes.Execute(f'INSERT INTO cadastro (nome, senha) VALUES("{nome}", "{senha}")')
    operacoes.Commit()
    operacoes.Disconnect()


#retorna uma lista de usuarios
def read():
    operacoes = Transaction()
    operacoes.Connect()
    operacoes.Execute(f'SELECT * FROM cadastro')
    rows = operacoes.Fetchall()
    operacoes.Disconnect()
    return rows
