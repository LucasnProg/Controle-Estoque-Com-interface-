from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import controleEstoque as ct


codigoCarrinho = []
nomeCarrinho = []
precoCarrinho = []
qtdCarrinho = []


def carrinhoDeCompras():
    if codigoAdicionar.get() == "" or quantAdicionar.get() == "":
        messagebox.showerror("Campos em branco", "Preencha os campos corretamente\nExistem campos em branco!")
    elif not codigoAdicionar.get().isdigit():
        messagebox.showerror("Código Invalido!", "O código, são apenas numeros!\nVerifique e tente novamente")
    elif ct.consultaId(int(codigoAdicionar.get())) == False:
        messagebox.showerror("Código Invalido!", "O Código digitado não existe!\nVerifique e tente novamente")
    elif int(codigoAdicionar.get()) in codigoCarrinho:
        messagebox.showerror("Código Invalido!", "Esse produto ja está no carrinho!\nVerifique e tente novamente")
    elif not quantAdicionar.get().isdigit() or int(quantAdicionar.get()) == 0:
        messagebox.showerror("Quantidade Invalido!", "Você inseriu alguma quantidade inválida\nVerifique e tente novamente")
    elif ct.verificarQuantidade(int(codigoAdicionar.get()),int(quantAdicionar.get())) == False:
        messagebox.showerror("Quantidade Invalido!", "Você inseriu alguma quantidade inválida, maior que a possivel no estoque\nlamentamos mas em breve teremos nosso estoque renovado.\nVerifique e tente novamente")
    else:
        adicionaCarrinho(int(codigoAdicionar.get()))

def comprar():
    if len(codigoCarrinho) == 0:
        messagebox.showerror("Erro na compra","Seu carrinho está vazio, adicione produtos antes de comprar.")
    else:
        precoTotal = 0
        for i in range(len(codigoCarrinho)):
            idProdutos = list(ct.bancoProdutos['ID_produto'].tolist())
            produtos = list(ct.bancoProdutos['Descrição_produto'].tolist())
            fornecedores = list(ct.bancoProdutos['fornecedor'].tolist()) 
            qtdEstoque = list(ct.bancoProdutos['qtd_produto'].tolist())
            indice = idProdutos.index(codigoCarrinho[i])
            if int(qtdEstoque[indice]) <= 15:
                ct.compra(codigoCarrinho[i],qtdCarrinho[i])
            else:       
                ct.compra(codigoCarrinho[i],qtdCarrinho[i])
                idProdutos = list(ct.bancoProdutos['ID_produto'].tolist())
                produtos = list(ct.bancoProdutos['Descrição_produto'].tolist())
                fornecedores = list(ct.bancoProdutos['fornecedor'].tolist()) 
                qtdEstoque = list(ct.bancoProdutos['qtd_produto'].tolist())
                if int(qtdEstoque[indice]) <= 15:
                    ct.fazerPedido(str(fornecedores[indice]), str(produtos[indice])) 
        for i in range(len(qtdCarrinho)):
            precoTotal += qtdCarrinho[i]*precoCarrinho[i]
        mensagem = "Compra realizada com sucesso!\n\n"
        for i in range(len(nomeCarrinho)):
            linha = f"{nomeCarrinho[i]}: {qtdCarrinho[i]}\n"
            mensagem += linha
        messagebox.showinfo("Produtos Comprados", mensagem + "\nTOTAL: {}".format('{:.2f}'.format(precoTotal)))
        nomeCarrinho.clear()
        precoCarrinho.clear()
        codigoCarrinho.clear()
        qtdCarrinho.clear()
        atualizarTabela()
        carrinho.delete(*carrinho.get_children()) 

def removerCarrinho():
    
    if len(codigoCarrinho) == 0:
        messagebox.showerror("Erro na compra","Seu carrinho está vazio, adicione produtos antes de comprar.")
    elif codigoRemover.get() == "" or quantRemover.get() == "":
        messagebox.showerror("Campos em branco", "Preencha os campos corretamente\nExistem campos em branco!")
    elif not codigoRemover.get().isdigit():
        messagebox.showerror("Código Invalido!", "O código, são apenas numeros!\nVerifique e tente novamente")
    elif int(codigoRemover.get()) not in codigoCarrinho:
        messagebox.showerror("Código Invalido!", "O Código digitado não está no seu carrinho!\nVerifique e tente novamente")
    elif not quantRemover.get().isdigit() or int(quantRemover.get()) == 0:
        messagebox.showerror("Quantidade Invalida!", "Você inseriu uma quantidade inválida\nVerifique e tente novamente")
    elif int(quantRemover.get()) > qtdCarrinho[codigoCarrinho.index(int(codigoRemover.get())) ]:
        messagebox.showerror("Quantidade Invalida!", "Você inseriu uma quantidade maior que a do seu carrinho\nVerifique e tente novamente")
    else:
        indice = codigoCarrinho.index(int(codigoRemover.get())) 
        remover(indice)

def remover(indice):
    if int(quantRemover.get()) == qtdCarrinho[indice]:
        del nomeCarrinho[indice]
        del precoCarrinho[indice]
        del codigoCarrinho[indice]
        del qtdCarrinho[indice]
        carrinho.delete(*carrinho.get_children())
        for i in range(len(codigoCarrinho)):
            carrinho.insert("",END,values=(str(codigoCarrinho[i]),str(nomeCarrinho[i]),str("R$ "+ str('{:.2f}'.format(precoCarrinho[i]))),str(qtdCarrinho[i]))) 
    else:
        qtdCarrinho[indice] -= int(quantRemover.get())
        carrinho.delete(*carrinho.get_children())
        for i in range(len(codigoCarrinho)):
            carrinho.insert("",END,values=(str(codigoCarrinho[i]),str(nomeCarrinho[i]),str("R$ "+ str('{:.2f}'.format(precoCarrinho[i]))),str(qtdCarrinho[i])))

def atualizarTabela():
    tabela.delete(*tabela.get_children()) 

    idProdutos = list(ct.bancoProdutos['ID_produto'].tolist())
    produtos = list(ct.bancoProdutos['Descrição_produto'].tolist())
    precoVendas = list(ct.bancoProdutos['preco_venda'].tolist()) 
    qtdEstoque = list(ct.bancoProdutos['qtd_produto'].tolist())
    for i in range(len(produtos)):
        tabela.insert("",END,values=(str(idProdutos[i]),str(produtos[i]),str("R$ "+ str('{:.2f}'.format(precoVendas[i]))),str(qtdEstoque[i])))

def adicionaCarrinho(codigo):
    carrinho.delete(*carrinho.get_children()) 
    nomeProduto = ct.buscarNomeProduto(codigo)
    preco = ct.buscarPrecoProduto(codigo)
    nomeCarrinho.append(nomeProduto)
    precoCarrinho.append(preco)
    codigoCarrinho.append(codigo)
    qtdCarrinho.append(int(quantAdicionar.get()))
    for i in range(len(codigoCarrinho)):
        carrinho.insert("",END,values=(str(codigoCarrinho[i]),str(nomeCarrinho[i]),str("R$ "+ str('{:.2f}'.format(precoCarrinho[i]))),str(qtdCarrinho[i])))

def telaDoUsuario():
    global codigoAdicionar,quantAdicionar,codigoRemover,quantRemover, tabela,carrinho

    telaUsuario = Tk()  
    telaUsuario.geometry("1300x700")
    telaUsuario.title("Tela do Usuário")
    telaUsuario.resizable(False,False)
    telaUsuario.config(bg="#6495ED",pady=50, padx =30)
   
    # --------Div adicionar
    divAdicionar = LabelFrame(telaUsuario,font = ("Arial", 16, "bold"),text="Adiciona ao carrinho", padx=20)
    divAdicionar.grid(column=1, row=0, padx=10, pady=10, sticky="nsew")


    codigoLabel = Label(divAdicionar,font = ("Arial", 12),text="Código do produto",)
    codigoLabel.grid(column=0,row=0, sticky="w",pady=4)
    codigoAdicionar = Entry(divAdicionar, width=50)
    codigoAdicionar.grid(column=0,row=1,pady=20)

    quantLabel = Label(divAdicionar,font = ("Arial", 12),text="Quantidade")
    quantLabel.grid(column=0,row=2, sticky="w",pady=4)
    quantAdicionar = Entry(divAdicionar, width=50)
    quantAdicionar.grid(column=0,row=3,pady=20)

    botaoadicionarCarrinho = Button(divAdicionar, text="Adicionar ao carrinho", command=carrinhoDeCompras)
    botaoadicionarCarrinho.config(background="#C0C0C0", font=("Arial",8))
    botaoadicionarCarrinho.grid(column=0,row=6,pady=10, sticky="e")

    # --------- Div tabela
    divTabela = LabelFrame(telaUsuario,font = ("Arial", 16, "bold"),text="Produtos", padx=20)
    divTabela.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")
    # --------- Tabela de estoque
    tabela = ttk.Treeview(divTabela, selectmode="browse", columns=("coluna1","coluna2","coluna3","coluna4"), show='headings')
    tabela.column("coluna1", width=200, minwidth=80, stretch=YES)
    tabela.heading("#1", text="Código")
    tabela.column("coluna2", width=200, minwidth=80, stretch=YES)
    tabela.heading("#2", text="Produto")
    tabela.column("coluna3", width=200, minwidth=80, stretch=YES)
    tabela.heading("#3", text="Preço")
    tabela.column("coluna4", width=200, minwidth=80, stretch=YES)
    tabela.heading("#4", text="Estoque")
    tabela.tag_configure("my_font", font=("Arial", 12))
    tabela.grid(column=0, row=0)
    atualizarTabela()

    #------Div Carrinho
    divCarrinho = LabelFrame(telaUsuario,font = ("Arial", 16, "bold"),text="Carrinho de Compras", padx=20)
    divCarrinho.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")
    carrinho = ttk.Treeview(divCarrinho, selectmode="browse", columns=("coluna1","coluna2","coluna3","coluna4"), show='headings')
    carrinho.column("coluna1", width=200, minwidth=80, stretch=YES)
    carrinho.heading("#1", text="Código")
    carrinho.column("coluna2", width=200, minwidth=80, stretch=YES)
    carrinho.heading("#2", text="Produto")
    carrinho.column("coluna3", width=200, minwidth=80, stretch=YES)
    carrinho.heading("#3", text="Preço")
    carrinho.column("coluna4", width=200, minwidth=80, stretch=YES)
    carrinho.heading("#4", text="Quantidade")
    carrinho.tag_configure("my_font", font=("Arial", 12))
    carrinho.grid(column=0, row=0)

    botaoComprar = Button(divCarrinho, text="COMPRAR", command=comprar)
    botaoComprar.config(background="#C0C0C0", font=("Arial",8))
    botaoComprar.grid(column=0,row=6,pady=10, sticky="e")

    #-------Div Remover carrinho
    divRemover = LabelFrame(telaUsuario,font = ("Arial", 16, "bold"),text="Remover do carrinho", padx=20)
    divRemover.grid(column=1, row=1, padx=10, pady=10, sticky="nsew")


    codigoRemoverLabel = Label(divRemover,font = ("Arial", 12),text="Código do produto",)
    codigoRemoverLabel.grid(column=0,row=0, sticky="w",pady=4)
    codigoRemover = Entry(divRemover, width=50)
    codigoRemover.grid(column=0,row=1,pady=20)

    quantRemoverLabel = Label(divRemover,font = ("Arial", 12),text="Quantidade")
    quantRemoverLabel.grid(column=0,row=2, sticky="w",pady=4)
    quantRemover = Entry(divRemover, width=50)
    quantRemover.grid(column=0,row=3,pady=20)

    botaoRemoverCarrinho = Button(divRemover, text="Remover do carrinho", command=removerCarrinho)
    botaoRemoverCarrinho.config(background="#C0C0C0", font=("Arial",8))
    botaoRemoverCarrinho.grid(column=0,row=6,pady=32, sticky="e")

    telaUsuario.mainloop()

