from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import datetime
import controleEstoque as ct
import banco_de_dados as bd


def validaPreco(valor):
    try: 
        float(valor)
        return(True)
    except ValueError:
        return False

def validaData(data):
    try: 
        dataAtual = date.today().strftime("%d/%m/%Y")
        dia,mes,ano = map(int,data.split("/")) 
        diaAtual, mesAtual, anoAtual = map(int, dataAtual.split("/"))
        if dia < 1 or dia > 31 or mes < 1 or mes >12 or ano < anoAtual:
            return False
        elif ano == anoAtual and mes < mesAtual:
            return False
        elif ano == anoAtual and mes == mesAtual and dia<=diaAtual:
            return False
        else: 
            return True
    except ValueError:
        return False
    
def validaAdicionar():
    if inserirFornecedor.get()=="" or inserirId.get()=="" or inserirPrecoCompra.get()=="" or inserirPrecoVenda.get()=="" or inserirProduto.get()=="" or inserirqtd.get()=="" or inserirValidade.get()=="":
        messagebox.showerror("Campos em Branco!", "Por favor preencha os campos corretamente.")
    elif not inserirId.get().isdigit():
        messagebox.showerror("Código inválido!", "Código inválido!\nPor favor, verifique e tente novamente.")
    elif ct.consultaId(int(inserirId.get())) == True :
        messagebox.showerror("Código ja Existe!", "Esse produto ja existe!\nPor favor, verifique e tente novamente.")
    elif not all(part.isalnum() or part.isspace() for part in str(inserirProduto.get()).split()):
        messagebox.showerror("Descrição inválida", "Essa descrição está inválida\nPor favor, verifique e tente novamente.")
    elif ct.consultaDescricao(str(inserirProduto.get()))==True:
        messagebox.showerror("Esse produto ja existe!", "Esse produto ja existe!\nPor favor, verifique e tente novamente.")
    elif not inserirqtd.get().isdigit():
        messagebox.showerror("Quantidade inválida!", "Quantidade inválida!\nPor favor, verifique e tente novamente.")
    elif validaPreco(inserirPrecoCompra.get()) == False:
        messagebox.showerror("Preço de Compra inválido!", "O preço que você inseriu não é valido!\nPor favor, verifique e tente novamente e tente representa com '.' o valor real .")
    elif validaPreco(inserirPrecoVenda.get()) == False:
        messagebox.showerror("Preço de Venda inválido!", "O preço que você inseriu não é valido!\nPor favor, verifique e tente novamente e tente representa com '.' o valor real .")
    elif bd.verificarEmail(str(inserirFornecedor.get())) == False:
        messagebox.showerror("Email de fornecedor inválido!", "O email do fornecedor que você inseriu não é valido!\nPor favor, verifique e tente novamente\ncertifique-se de que este email existe.")
    elif validaData(str(inserirValidade.get())) == False:
        messagebox.showerror("Data inválida!","Verifique se a data está correta e tente novamente!")
    else:
        validade = datetime.datetime.strptime(inserirValidade.get(), "%d/%m/%Y").strftime("%y-%m-%d %H:%M:%S")
        ct.adicionarProduto(int(inserirId.get()), str(inserirProduto.get()),int(inserirqtd.get()),float(inserirPrecoCompra.get()),float(inserirPrecoVenda.get()),str(inserirFornecedor.get()), str(validade))
        messagebox.showinfo("Produto Adicionado!", "Esse produto foi adicionado com sucesso!\nAtualize o estoque para ver a mudança")
        telaAdd.destroy()

def validaRemover():
    if inserirIdRemover.get() == "":
        messagebox.showerror("Campo em Branco!", "Por favor insira o Código do produto que deseja remover.")
    elif not inserirIdRemover.get().isdigit():
        messagebox.showerror("Código Invalido!", "Código inválido!\nPor favor digite apenas numeros, verifique e tente novamente.")
    elif ct.consultaId(int(inserirIdRemover.get())) ==False:
        messagebox.showerror("Código Invalido!", "O código que você inseriu é invalido ou não existe.")
    else:
        ct.removerProduto(int(inserirIdRemover.get()))
        messagebox.showinfo("Produto Removido!", "Esse produto foi Removido com sucesso!\nAtualize o estoque para ver a mudança")
        telaRemove.destroy()

def validaEdicao():
    if inserirFornecedorEdit.get() == "" or inserirIdEdit.get() == "" or inserirPrecoVendaEdit.get() == "" or inserirProdutoEdit.get() == "" or inserirqtdEdit.get() == "":
        messagebox.showerror("Campos em Branco!", "Por favor preencha os campos corretamente.")
    elif not inserirIdEdit.get().isdigit():
        messagebox.showerror("Código inválido!", "Código inválido!\nPor favor digite apenas numeros, verifique e tente novamente.")
    elif ct.consultaId(int(inserirIdEdit.get())) == False :
        messagebox.showerror("Código Invalido!", "O código que você inseriu é invalido ou não existe.")
    elif not all(part.isalnum() or part.isspace() for part in str(inserirProdutoEdit.get()).split()):
        messagebox.showerror("Descrição inválida", "Essa descrição está inválida\nPor favor, verifique e tente novamente.")
    elif not inserirqtdEdit.get().isdigit():
        messagebox.showerror("Quantidade inválida!", "Quantidade inválida!\nPor favor, verifique e tente novamente.")
    elif validaPreco(inserirPrecoVendaEdit.get()) == False:
        messagebox.showerror("Preço de Venda inválido!", "O preço que você inseriu não é valido!\nPor favor, verifique e tente novamente e tente representa com '.' o valor real .")
    elif bd.verificarEmail(str(inserirFornecedorEdit.get())) == False:
        messagebox.showerror("Email de fornecedor inválido!", "O email do fornecedor que você inseriu não é valido!\nPor favor, verifique e tente novamente\ncertifique-se de que este email existe.")
    else:
        ct.editarProduto(int(inserirIdEdit.get()), str(inserirProdutoEdit.get()), int(inserirqtdEdit.get()), float(inserirPrecoVendaEdit.get()), str(inserirFornecedorEdit.get()))
        messagebox.showinfo("Produto Editado!", "Esse produto foi Editado com sucesso!\nAtualize o estoque para ver a mudança")
        telaEdit.destroy()

def telaAdicionar():
    global inserirFornecedor, inserirId, inserirPrecoCompra, inserirPrecoVenda, inserirProduto, inserirqtd,inserirValidade, telaAdd
    telaAdd = Tk()

    telaAdd.geometry("350x500")
    telaAdd.title("Adicione um produto!")
    telaAdd.resizable(False,False)
    telaAdd.config(bg="#6495ED",pady=30)

    # ------------ Label principal

    container = LabelFrame(telaAdd,font = ("Arial", 14, "bold"),text="Adicionar produto ao estoque", padx=30)
    container.pack(side="top")
    
    labelId = Label(container,text="Código do produto:",font=("Arial", 10, "bold"))
    labelId.grid(column=0,row=0, pady=5,sticky="w")
    inserirId = Entry(container, width=40)
    inserirId.grid(column=0,row=1,sticky="w")

    labelProduto = Label(container,text="Descrição do produto:",font=("Arial", 10, "bold"))
    labelProduto.grid(column=0,row=2, pady=5,sticky="w")
    inserirProduto = Entry(container, width=40)
    inserirProduto.grid(column=0,row=3,sticky="w")

    labelqtd = Label(container,text="Quantidade:",font=("Arial", 10, "bold"))
    labelqtd.grid(column=0,row=4, pady=5,sticky="w")
    inserirqtd = Entry(container, width=40)
    inserirqtd.grid(column=0,row=5,sticky="w")

    labelPrecoCompra = Label(container,text="Preço de compra:",font=("Arial", 10, "bold"))
    labelPrecoCompra.grid(column=0,row=6, pady=5,sticky="w")
    inserirPrecoCompra = Entry(container, width=40)
    inserirPrecoCompra.grid(column=0,row=7,sticky="w")

    labelPrecoVenda = Label(container,text="Preço de venda:",font=("Arial", 10, "bold"))
    labelPrecoVenda.grid(column=0,row=8, pady=5,sticky="w")
    inserirPrecoVenda = Entry(container, width=40)
    inserirPrecoVenda.grid(column=0,row=9,sticky="w")

    labelFornecedor = Label(container,text="Fornecedor desse produto:",font=("Arial", 10, "bold"))
    labelFornecedor.grid(column=0,row=10, pady=5,sticky="w")
    inserirFornecedor = Entry(container, width=40)
    inserirFornecedor.grid(column=0,row=11,sticky="w")

    labelValidade = Label(container,text="Validade desse produto:",font=("Arial", 10, "bold"))
    labelValidade.grid(column=0,row=12, pady=5,sticky="w")
    inserirValidade = Entry(container, width=40)
    inserirValidade.grid(column=0,row=13,sticky="w")

    botaoAdicionar = Button(container, text="Adicionar produto", command=validaAdicionar)
    botaoAdicionar.grid(column=0,row=14,sticky="W",pady=5)

    telaAdd.mainloop()

def validaEnviarEmail():
    if inserirTexto.get("1.0", "end-1c") == "" or inserirAssunto.get() == "" or inserirEmailFornecedor == "":
        messagebox.showerror("Não foi possivel Enviar email","Existem campos em branco!\nPreencha e tente novamente.")
    elif bd.verificarEmail(str(inserirEmailFornecedor.get())) == False:
        messagebox.showerror("Email inválido","O email que você inseriu está inválido!\nverifique e tente novamente.")
    elif ct.consultaFornecedor(str(inserirEmailFornecedor.get())) == False:
        messagebox.showerror("Email inválido","O email que você inseriu não pertence a nenhum fornecedor!\nverifique e tente novamente.")
    else:
        ct.enviarEmail(str(inserirEmailFornecedor.get()),str(inserirAssunto.get()),str(inserirTexto.get("1.0", "end-1c")))
        messagebox.showinfo("Email Enviado com sucesso!","Seu email foi enviado com sucesso!")
        telaEmail.destroy()

def telaRemover():
    global inserirIdRemover,telaRemove

    telaRemove = Tk()
    
    telaRemove.geometry("350x330")
    telaRemove.title("Remova um produto")
    telaRemove.resizable(False,False)
    telaRemove.config(bg="#6495ED",pady=30)

    # ------------ Label principal

    container = LabelFrame(telaRemove,font = ("Arial", 14, "bold"),text="Remover produtos", padx=30)
    container.pack(side="top")
    
    labelIdRemover = Label(container,text="Código do produto:",font=("Arial", 10, "bold"))
    labelIdRemover.grid(column=0,row=0, pady=20,sticky="w")
    inserirIdRemover = Entry(container, width=40)
    inserirIdRemover.grid(column=0,row=1,sticky="w")

    botaoRemover = Button(container, text="Remover produto", command=validaRemover)
    botaoRemover.grid(column=0,row=2,sticky="W",pady=20)

    labeInfo = Label(container,text="Esse produto será removido\ndo seu estoque permanentemente",font=("Arial", 10, "bold"))
    labeInfo.grid(column=0,row=3, pady=20,sticky="w")

    telaRemove.mainloop()

def telaDeEditar():
    global inserirFornecedorEdit, inserirIdEdit, inserirPrecoVendaEdit, inserirProdutoEdit, inserirqtdEdit, telaEdit
    
    telaEdit = Tk()

    telaEdit.geometry("350x450")
    telaEdit.title("Editar informações de um produto!")
    telaEdit.resizable(False,False)
    telaEdit.config(bg="#6495ED",pady=30)

    # ------------ Label principal

    container = LabelFrame(telaEdit,font = ("Arial", 14, "bold"),text="Editar produto do estoque", padx=30)
    container.pack(side="top")
    
    labelIdEdit = Label(container,text="Código do produto:",font=("Arial", 10, "bold"))
    labelIdEdit.grid(column=0,row=0, pady=10,sticky="w")
    inserirIdEdit = Entry(container, width=40)
    inserirIdEdit.grid(column=0,row=1,sticky="w")

    labelProdutoEdit = Label(container,text="Nova Descrição do produto:",font=("Arial", 10, "bold"))
    labelProdutoEdit.grid(column=0,row=2, pady=10,sticky="w")
    inserirProdutoEdit = Entry(container, width=40)
    inserirProdutoEdit.grid(column=0,row=3,sticky="w")

    labelqtdEdit = Label(container,text="Nova Quantidade:",font=("Arial", 10, "bold"))
    labelqtdEdit.grid(column=0,row=4, pady=10,sticky="w")
    inserirqtdEdit = Entry(container, width=40)
    inserirqtdEdit.grid(column=0,row=5,sticky="w")

    labelPrecoVendaEdit = Label(container,text="Novo Preço de venda:",font=("Arial", 10, "bold"))
    labelPrecoVendaEdit.grid(column=0,row=8, pady=10,sticky="w")
    inserirPrecoVendaEdit = Entry(container, width=40)
    inserirPrecoVendaEdit.grid(column=0,row=9,sticky="w")

    labelFornecedorEdit = Label(container,text="Novo Fornecedor desse produto:",font=("Arial", 10, "bold"))
    labelFornecedorEdit.grid(column=0,row=10, pady=10,sticky="w")
    inserirFornecedorEdit = Entry(container, width=40)
    inserirFornecedorEdit.grid(column=0,row=11,sticky="w")

    botaoAdicionarEdit = Button(container, text="Atualizar produto", command=validaEdicao)
    botaoAdicionarEdit.grid(column=0,row=14,sticky="W",pady=15)

    telaEdit.mainloop()

def telaEnviarEmail():
    global inserirAssunto,inserirEmailFornecedor, inserirTexto, telaEmail

    telaEmail = Tk()

    telaEmail.geometry("400x550")
    telaEmail.title("Enviar Email para fornecedor!")
    telaEmail.resizable(False,False)
    telaEmail.config(bg="#6495ED",pady=30)

    container = LabelFrame(telaEmail,font = ("Arial", 14, "bold"),text="Entrar em contato com o fornecedor:", padx=30)
    container.pack(side="top")

    labelFornecerdor = Label(container,text="Email do fornecedor:",font=("Arial", 10, "bold"))
    labelFornecerdor.grid(column=0,row=0,sticky="W",pady=10)
    inserirEmailFornecedor = Entry(container, width=54)
    inserirEmailFornecedor.grid(column=0,row=1,sticky="w")

    labelAssunto = Label(container,text="Assunto do Email:",font=("Arial", 10, "bold"))
    labelAssunto.grid(column=0,row=2,sticky="W",pady=10)
    inserirAssunto = Entry(container, width=54)
    inserirAssunto.grid(column=0,row=3,sticky="w")

    labelTexto = Label(container,text="Texto:",font=("Arial", 10, "bold"))
    labelTexto.grid(column=0,row=4,sticky="W",pady=15)
    inserirTexto = Text(container, width=40, height=15)
    inserirTexto.grid(column=0,row=5,sticky="w")

    botaoEnviar = Button(container, text="Enviar Mensagem", command=validaEnviarEmail)
    botaoEnviar.grid(column=0,row=6,sticky="e",pady=15)

    telaEmail.mainloop()

