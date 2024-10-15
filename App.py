import front as ft
import backend as bk
from tkinter import messagebox

app = None

# Função que realiza o cadastro de usuario
def Cadastro():
    bk.criarBanco()

    dados_login = bk.read() # recebe uma lista com todos os usuário cadastrados
    
    # armazena as informaçoes digitadas
    nome: str = app.nome.get()
    senha: str = app.senha.get()

    # usuario não existe na lista de cadastrados
    usuarioExist: bool = False

    # percorre a lista de usuário
    for rows in dados_login:
        nome_db, senha_db = rows
        # verifica se os dados ja estão na lista de cadastrados
        if nome == nome_db and senha == senha_db in rows:
            # se sim, a variavel recebe true
            usuarioExist = True
            break
    
    if usuarioExist:
        messagebox.showerror('ERROR', 'O usuario ja está cadastrado')
    else:
        # salva os dados digitados na lista de cadastrados
        bk.create(nome, senha)
        messagebox.showinfo('cadastro', 'cadastro feito com sucesso')
        app.clear()

# realiza o login caso o usuário esteja cadastrado
def Login():
    dados_login = bk.read()
    nome: str = app.nome.get().strip()
    senha: str = app.senha.get().strip()

    # usuário não está logado 
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
