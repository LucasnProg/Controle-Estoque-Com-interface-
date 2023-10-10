
from tkinter import *
import banco_de_dados as bd
from tkinter import messagebox
import cadastrarUser as cad
import redefinirSenhas as red
import telaUsuario as user
import telaAdministrador as admin

def logarUser():
   if cpfUser.get() == "" or senhaUser.get() == "":
       mensagemUser["text"] = "Preencha os campos corretamente"
   elif bd.verificarCpfUser(cpfUser.get()) == True and bd.verificaSenha(cpfUser.get(),senhaUser.get()) == True:
       telaInicial.destroy()
       user.telaDoUsuario()
   else:
       mensagemUser["text"] = "Login invalido"
     
def logarAdm():
   if cpfAdm.get() == "" or senhaAdm.get() == "":
      mensagemAdm["text"] = "Preencha os campos corretamente"
   elif bd.verificarAdm(cpfAdm.get()) == True and bd.logarAdm(cpfAdm.get(),senhaAdm.get()) == True:
      telaInicial.destroy()
      admin.telaDoAdministrador()
   else:
       mensagemAdm["text"] = "Login invalido"


# ---------------- TELA DE LOGIN ---------------

telaInicial = Tk()

telaInicial.geometry("900x500")
telaInicial.title("Tela Incial")
telaInicial.resizable(False,False)
telaInicial.config(bg="#6495ED",pady=50)

# ----- Container de Login

container = LabelFrame(telaInicial,font = ("Arial", 14, "bold"),text="Login", pady=50, padx=30)
container.pack(side="top")

# ----- Frame do login Usuario

divUser = LabelFrame(container,font = ("Arial", 14, "bold"),text="Comprador", pady=10, padx=30)
divUser.grid(column=0,row=0)


comprador = Label(divUser,text="CPF",font=("Arial", 10, "bold"))
comprador.grid(column=0,row=0, pady=10,sticky="w")
cpfUser = Entry(divUser, width=40)
cpfUser.grid(column=0,row=1)
labelSenhaUser = Label(divUser,text="Senha",font=("Arial", 10, "bold"))
labelSenhaUser.grid(column=0,row=2, pady=10,sticky="w")
senhaUser = Entry(divUser,show="*", width=40)
senhaUser.grid(column=0,row=3)
botaoLoginUser = Button(divUser, text="Login", command=logarUser)
botaoLoginUser.grid(column=0,row=4,sticky="W",pady=10)
botaoCadastraUser = Button(divUser, text="Cadastrar-se", command=cad.telaCadastro)
botaoCadastraUser.grid(column=0,row=4,sticky="e",pady=10)
mensagemUser = Label(divUser, text="")
mensagemUser.grid(column=0,row=6,sticky="W",pady=10)
esqueceuSenhaUser = Label(divUser, text="Esqueceu a senha?",font=("Arial", 8, "underline"))
esqueceuSenhaUser.grid(column=0,row=5,sticky="W",pady=10)
esqueceuSenhaUser.bind("<Enter>", lambda event: esqueceuSenhaUser.config(fg='blue',font=("Arial", 8, "underline")))
esqueceuSenhaUser.bind("<Leave>", lambda event: esqueceuSenhaUser.config(fg='Black', font=("Arial", 8)))
esqueceuSenhaUser.bind("<Button-1>", red.telaRedefinirUser)

# ----- Frame do login Administrador

divAdm = LabelFrame(container,font = ("Arial", 14, "bold"),text="Administrador", pady=10,padx=30)
divAdm.grid(column=2,row=0)
adm = Label(divAdm,text="CPF",font=("Arial", 10, "bold"))
adm.grid(column=0,row=0, pady=10,sticky="w")
cpfAdm = Entry(divAdm, width=40)
cpfAdm.grid(column=0,row=1)
labelSenhaAdm = Label(divAdm,text="Senha",font=("Arial", 10, "bold"))
labelSenhaAdm.grid(column=0,row=2, pady=10,sticky="w")
senhaAdm = Entry(divAdm,show="*", width=40)
senhaAdm.grid(column=0,row=3)
botaoLoginAdm = Button(divAdm, text="Login", command=logarAdm)
botaoLoginAdm.grid(column=0,row=4,sticky="W",pady=10)
mensagemAdm = Label(divAdm, text="")
mensagemAdm.grid(column=0,row=6,sticky="W",pady=10)
esqueceuSenha = Label(divAdm, text="Esqueceu a senha?",font=("Arial", 8, "underline"))
esqueceuSenha.grid(column=0,row=5,sticky="W",pady=10)
esqueceuSenha.bind("<Enter>", lambda event: esqueceuSenha.config(fg='blue',font=("Arial", 8, "underline")))
esqueceuSenha.bind("<Leave>", lambda event: esqueceuSenha.config(fg='Black', font=("Arial", 8)))
esqueceuSenha.bind("<Button-1>", red.telaRedefinirAdm)

telaInicial.mainloop()





