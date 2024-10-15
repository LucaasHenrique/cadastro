import front as ft
import backend as bk
from tkinter import messagebox

app = None

# Função que realiza o cadastro de usuario
def Cadastro():
    bk.criarBanco()

    dados_login = bk.read()
    nome: str = app.nome.get()
    senha: str = app.senha.get()
    
    usuarioExist: bool = False

    for rows in dados_login:
        nome_db, senha_db = rows
        if nome == nome_db and senha == senha_db in rows:
            usuarioExist = True
            break

    if usuarioExist:
        messagebox.showerror('ERROR', 'O usuario ja está cadastrado')
    else:
        bk.create(nome, senha)
        messagebox.showinfo('cadastro', 'cadastro feito com sucesso')
        app.clear()

#
def Login():
    dados_login = bk.read()
    nome: str = app.nome.get().strip()
    senha: str = app.senha.get().strip()
    login: bool = False

    print(dados_login)

    for rows in dados_login:
        nome_db, senha_db = rows
        if nome == nome_db and senha == senha_db in rows:
            login = True
            break
    if login:
        messagebox.showinfo('OK', 'Login feito com sucesso')
        app.clear()
    else:
        messagebox.showerror('ERROR', 'Senha ou nome incorreto')
    

if __name__=='__main__':
    app = ft.Tela()
    app.bot.configure(command=Cadastro)
    app.bot2.configure(command=Login)
    app.run()
