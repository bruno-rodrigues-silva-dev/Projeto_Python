import tkinter as tk
from tkinter import messagebox

# Função para criar conta


def criar_conta():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if usuario and senha:
        messagebox.showinfo(
            "Conta criada", f"Usuário '{usuario}' cadastrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos!")


# Criar janela
janela = tk.Tk()
janela.title("Cadastro de Login")
janela.geometry("300x200")

# Rótulos e entradas
label_usuario = tk.Label(janela, text="Usuário:")
label_usuario.pack(pady=5)

entry_usuario = tk.Entry(janela)
entry_usuario.pack(pady=5)

label_senha = tk.Label(janela, text="Senha:")
label_senha.pack(pady=5)

entry_senha = tk.Entry(janela, show="*")
entry_senha.pack(pady=5)

# Botão
btn_criar = tk.Button(janela, text="Criar Conta", command=criar_conta)
btn_criar.pack(pady=20)

# Rodar janela
janela.mainloop()
