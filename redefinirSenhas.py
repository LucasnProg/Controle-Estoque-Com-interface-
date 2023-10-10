from tkinter import *
import banco_de_dados as bd
from tkinter import messagebox


def salvarSenhaAdm():
    if cpfEntryAdm.get() == "" or nomeEntryAdm.get() =="" or emailEntryAdm.get() == "" or senhaEntryAdm.get()=="":
       messagebox.showerror("Campos em branco!", "Por favor, preencha todos os campos corretamente!")
    elif len(cpfEntryAdm.get()) != 11 or not cpfEntryAdm.get().isdigit():
       messagebox.showerror("CPF invalido!", "Por favor, insira numero de cpf válido e apenas números")
    elif bd.verificarCpfAdmin(cpfEntryAdm.get()) == False:
       messagebox.showerror("ERRO NO CPF!", "Este CPF não está cadastrado no sistema!")
    else:
        if bd.verificarInfosAdmin(cpfEntryAdm.get(),nomeEntryAdm.get(),emailEntryAdm.get()) == False:
          messagebox.showerror("Dados Inválidos", "Verifique seus dados e tente novamente.")
        else:
            if len(senhaEntryAdm.get()) <8 or senhaEntryAdm.get().isalpha() == True or senhaEntryAdm.get().isdigit() == True:
                messagebox.showerror("Senha inválido!", "Por favor, insira uma senha de pelo menos 8 digitos e que possua letras e numeros")
            else:
                bd.redefinirSenhaAdmin(cpfEntryAdm.get(),senhaEntryAdm.get())
                messagebox.showinfo("ÊXITO","Senha redefinida com Sucesso!")
                redefinirSenhaAdm.destroy()
           
def salvarSenhaUsuario():
    if cpfEntryUser.get() == "" or nomeEntryUser.get() =="" or emailEntryUser.get() == "" or senhaEntryUser.get()=="":
       messagebox.showerror("Campos em branco!", "Por favor, preencha todos os campos corretamente!")
    elif len(cpfEntryUser.get()) != 11 or not cpfEntryUser.get().isdigit():
       messagebox.showerror("CPF invalido!", "Por favor, insira numero de cpf válido e apenas números")
    elif bd.verificarCpfUser(cpfEntryUser.get()) == False:
       messagebox.showerror("ERRO NO CPF!", "Este CPF não está cadastrado no sistema!")
    else:
        if bd.verificarInfosUser(cpfEntryUser.get(),nomeEntryUser.get(),emailEntryUser.get()) == False:
          messagebox.showerror("Dados Inválidos", "Verifique seus dados e tente novamente.")
        else:
            if len(senhaEntryUser.get()) <8 or senhaEntryUser.get().isalpha() == True or senhaEntryUser.get().isdigit() == True:
                messagebox.showerror("Senha inválido!", "Por favor, insira uma senha de pelo menos 8 digitos e que possua letras e numeros")
            else:
                bd.redefinirSenhaUser(cpfEntryUser.get(),senhaEntryUser.get())
                messagebox.showinfo("ÊXITO","Senha redefinida com Sucesso!")
                redefinirSenhaUser.destroy()



def telaRedefinirAdm(event):
    global cpfEntryAdm, nomeEntryAdm, senhaEntryAdm, emailEntryAdm, redefinirSenhaAdm
    redefinirSenhaAdm = Tk()

    redefinirSenhaAdm.geometry("350x450")
    redefinirSenhaAdm.title("Esqueceu sua senha?")
    redefinirSenhaAdm.resizable(False,False)
    redefinirSenhaAdm.config(bg="#6495ED",pady=50)

    mainFrame = LabelFrame(redefinirSenhaAdm, font = ("Arial", 14, "bold"),text="Redefinir Senha", pady=20, padx=30)
    mainFrame.pack(side=TOP)



    cpfLabelAdm = Label(mainFrame, text="CPF",font=("Arial", 10, "bold"))
    cpfLabelAdm.grid(column=0,row=0,pady=5,sticky="w")

    cpfEntryAdm = Entry(mainFrame, width=40)
    cpfEntryAdm.grid(column=0,row=1,sticky="w")

    nomeLabelAdm = Label(mainFrame,text="Nome",font=("Arial", 10, "bold"))
    nomeLabelAdm.grid(column=0,row=2, pady=5,sticky="w")
    nomeEntryAdm = Entry(mainFrame, width=40)
    nomeEntryAdm.grid(column=0,row=3,sticky="w")

    emailLabelAdm = Label(mainFrame,text="Email",font=("Arial", 10, "bold"))
    emailLabelAdm.grid(column=0,row=4, pady=5,sticky="w")
    emailEntryAdm = Entry(mainFrame, width=40)
    emailEntryAdm.grid(column=0,row=5,sticky="w")

    senhaLabelAdm = Label(mainFrame,text="Nova Senha",font=("Arial", 10, "bold"))
    senhaLabelAdm.grid(column=0,row=6, pady=5,sticky="w")
    senhaEntryAdm = Entry(mainFrame, width=40,show="*")
    senhaEntryAdm.grid(column=0,row=7,sticky="w")

    redefinirAdm = Button(mainFrame, text="Redefinir",command = salvarSenhaAdm)
    redefinirAdm.grid(column=0,row=8,sticky="W",pady=10)


    redefinirSenhaAdm.mainloop()

def telaRedefinirUser(event):
    global cpfEntryUser, nomeEntryUser, senhaEntryUser, emailEntryUser, redefinirSenhaUser
    redefinirSenhaUser = Tk()

    redefinirSenhaUser.geometry("350x450")
    redefinirSenhaUser.title("Esqueceu sua senha?")
    redefinirSenhaUser.resizable(False,False)
    redefinirSenhaUser.config(bg="#6495ED",pady=50)

    mainFrame = LabelFrame(redefinirSenhaUser, font = ("Arial", 14, "bold"),text="Redefinir Senha", pady=20, padx=30)
    mainFrame.pack(side=TOP)



    cpfLabelUser = Label(mainFrame, text="CPF",font=("Arial", 10, "bold"))
    cpfLabelUser.grid(column=0,row=0,pady=5,sticky="w")

    cpfEntryUser = Entry(mainFrame, width=40)
    cpfEntryUser.grid(column=0,row=1,sticky="w")

    nomeLabelUser = Label(mainFrame,text="Nome",font=("Arial", 10, "bold"))
    nomeLabelUser.grid(column=0,row=2, pady=5,sticky="w")
    nomeEntryUser = Entry(mainFrame, width=40)
    nomeEntryUser.grid(column=0,row=3,sticky="w")

    emailLabelUser = Label(mainFrame,text="Email",font=("Arial", 10, "bold"))
    emailLabelUser.grid(column=0,row=4, pady=5,sticky="w")
    emailEntryUser = Entry(mainFrame, width=40)
    emailEntryUser.grid(column=0,row=5,sticky="w")

    senhaLabelUser = Label(mainFrame,text="Nova Senha",font=("Arial", 10, "bold"))
    senhaLabelUser.grid(column=0,row=6, pady=5,sticky="w")
    senhaEntryUser = Entry(mainFrame, width=40,show="*")
    senhaEntryUser.grid(column=0,row=7,sticky="w")

    redefinirUser = Button(mainFrame, text="Redefinir",command = salvarSenhaUsuario)
    redefinirUser.grid(column=0,row=8,sticky="W",pady=10)


    redefinirSenhaUser.mainloop()
