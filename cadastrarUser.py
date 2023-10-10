from tkinter import *
from tkinter import messagebox
import banco_de_dados as bd

def validarCadastro(cpf,nome,email,senha):
    if cpf == "" or nome =="" or email == "" or senha=="":
       messagebox.showerror("Campos em branco!", "Por favor, preencha todos os campos corretamente!")
    elif len(cpf) != 11 or not cpf.isdigit():
       messagebox.showwarning("CPF invalido!", "Por favor, insira numero de cpf válido e apenas números")
    elif bd.verificarCpfUser(cpf) == True:
       messagebox.showwarning("ERRO NO CPF!", "Este CPF já está cadastrado no sistema!")
    elif not all(part.isalpha() or part.isspace() for part in nome.split()):
        messagebox.showwarning("Nome inválido!", "Por favor, insira apenas letras")
    elif bd.verificarEmail(email) == False:
        messagebox.showwarning("Email inválido!", "Por favor, insira um email válido")
    elif len(senha) <8 or senha.isalpha() == True or senha.isdigit() == True:
        messagebox.showwarning("Senha inválido!", "Por favor, insira uma senha de pelo menos 8 digitos e que possua letras e numeros")
    else:
        bd.adicionaUsuario(cpf,nome,email,senha)
        cadastraUser.destroy()

def chamaValidar():
    cpf = str(inserirCpf.get())
    nome = str(inserirnome.get())
    email = str(inseriremail.get())
    senha = str(inserirsenha.get())
    validarCadastro(cpf, nome, email, senha)


def telaCadastro():

    global inserirCpf, inserirnome, inseriremail, inserirsenha, cadastraUser

    cadastraUser = Tk()

    cadastraUser.geometry("350x450")
    cadastraUser.title("Crie sua conta")
    cadastraUser.resizable(False,False)
    cadastraUser.config(bg="#6495ED",pady=50)

    # ------------ Label principal

    container = LabelFrame(cadastraUser,font = ("Arial", 14, "bold"),text="Cadastrar-se", pady=10, padx=30)
    container.pack(side="top")

    # --------- Formulario de cadastro

    labelCpf = Label(container,text="CPF",font=("Arial", 10, "bold"))
    labelCpf.grid(column=0,row=0, pady=5,sticky="w")
    inserirCpf = Entry(container, width=40)
    inserirCpf.grid(column=0,row=1,sticky="w")

    labelnome = Label(container,text="Nome",font=("Arial", 10, "bold"))
    labelnome.grid(column=0,row=2, pady=5,sticky="w")
    inserirnome = Entry(container, width=40)
    inserirnome.grid(column=0,row=3,sticky="w")

    labelemail = Label(container,text="Email",font=("Arial", 10, "bold"))
    labelemail.grid(column=0,row=4, pady=5,sticky="w")
    inseriremail = Entry(container, width=40)
    inseriremail.grid(column=0,row=5,sticky="w")

    labelsenha = Label(container,text="Senha",font=("Arial", 10, "bold"))
    labelsenha.grid(column=0,row=6, pady=5,sticky="w")
    inserirsenha = Entry(container, width=40,show="*")
    inserirsenha.grid(column=0,row=7,sticky="w")

    labelAviso = Label(container,text="* Senha deve conter letras, números\ne possuir pelo menos 8 digitos.",font=("Arial", 10, "bold"))
    labelAviso.grid(column=0,row=8, pady=5,sticky="w")
    labelAviso.config(foreground="red")

    cadastra = Button(container, text="Cadastrar-se",command=chamaValidar)
    cadastra.grid(column=0,row=9,sticky="W",pady=5)

    cadastraUser.mainloop()
