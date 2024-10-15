import tkinter
import customtkinter


# Classe para a criação da janela de teste
class Tela(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        """self.janela = customtkinter.CTk()"""
        self.title('janela mae')
        self.geometry('400x400')
        self.resizable(False, False)
        self.title('Cadastro')
        self.text1 = customtkinter.CTkLabel(self, text='CADASTRO')
        self.text1.pack(padx=10, pady=10)

        self.nome = customtkinter.CTkEntry(self, placeholder_text="seu nome", width=200, height=40)
        self.nome.pack(padx=10, pady=10)

        self.senha = customtkinter.CTkEntry(self, placeholder_text="sua senha", width=200, height=40)
        self.senha.pack(padx=10, pady=10)

        self.bot = customtkinter.CTkButton(self, text='Fazer Cadastro', width=200, height=40)
        self.bot.pack(padx=10, pady=10)
        self.bot2 = customtkinter.CTkButton(self, text='fazer login', width=200, height=40)
        self.bot2.pack(padx=10, pady=10)

    # limpar os campos de entrada de dados
    def clear(self):
        self.nome.delete(0, tkinter.END)
        self.senha.delete(0, tkinter.END)

    def run(self):
        self.mainloop()
