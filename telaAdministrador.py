from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import controleEstoque as ct
import telasGerenciamento as tg

def exibirEstoqueGeral():
    estoqueGeral.delete(*estoqueGeral.get_children()) 

    idProdutos = list(ct.bancoProdutos['ID_produto'].tolist())
    produtos = list(ct.bancoProdutos['Descrição_produto'].tolist())
    fornecedores = list(ct.bancoProdutos['fornecedor'].tolist())  
    qtdEstoque = list(ct.bancoProdutos['qtd_produto'].tolist())
    precoCompra = list(ct.bancoProdutos['preco_produto'].tolist())
    precoVenda = list(ct.bancoProdutos['preco_venda'].tolist())
    validade = list(ct.bancoProdutos['validade'].tolist())
    numVendas = list(ct.bancoProdutos['num_vendas'].tolist())
    lucro = list(ct.bancoProdutos['Lucro'].tolist())

    for i in range(len(produtos)):
            estoqueGeral.insert("", END, values=(str(idProdutos[i]), str(produtos[i]), str(qtdEstoque[i]),str("R$ "+ str('{:.2f}'.format(precoCompra[i]))), str("R$ "+ str('{:.2f}'.format(precoVenda[i]))), str(fornecedores[i]),str(validade[i]), str(numVendas[i]), str("R$ "+ str('{:.2f}'.format(lucro[i])))))

def produtosPedidos():
    pedidos.delete(*pedidos.get_children()) 

    idProdutos = list(ct.bancoProdutos['ID_produto'].tolist())
    produtos = list(ct.bancoProdutos['Descrição_produto'].tolist())
    fornecedores = list(ct.bancoProdutos['fornecedor'].tolist())  
    qtdEstoque = list(ct.bancoProdutos['qtd_produto'].tolist())
    for i in range(len(produtos)):
        if int(qtdEstoque[i]) <=15:
            pedidos.insert("",END,values=(str(idProdutos[i]),str(produtos[i]),str(fornecedores[i]),str(qtdEstoque[i])))


def atualizarEstoque():
    estoque.delete(*estoque.get_children()) 

    idProdutos = list(ct.bancoProdutos['ID_produto'].tolist())
    produtos = list(ct.bancoProdutos['Descrição_produto'].tolist())
    precoVendas = list(ct.bancoProdutos['preco_venda'].tolist())  
    qtdEstoque = list(ct.bancoProdutos['qtd_produto'].tolist())
    for i in range(len(produtos)):
        estoque.insert("",END,values=(str(idProdutos[i]),str(produtos[i]),str("R$ "+ str('{:.2f}'.format(precoVendas[i]))),str(qtdEstoque[i])))

def criaGraficoVendas():
    fig = Figure(figsize=(13, 5), dpi=70)
    ax = fig.add_subplot(111)
    
    ct.bancoProdutos.plot(x="Descrição_produto", y="num_vendas", kind="barh", ax=ax)
    
    ax.set_title('Produtos mais vendidos')
    ax.set_xlabel('Vendas')
    ax.set_ylabel('Produto')
    
    canvasGrafico = FigureCanvasTkAgg(fig, master=graficoVendas)
    canvasGrafico.draw()
    canvasGrafico.get_tk_widget().pack()

def criaGraficoLucro():
    fig = Figure(figsize=(13, 5), dpi=70)
    ax = fig.add_subplot(111)
    
    ct.bancoProdutos.plot(x="Descrição_produto", y="Lucro", kind="barh", ax=ax)
    
    ax.set_title('Lucro por produto')
    ax.set_xlabel('Lucro')
    ax.set_ylabel('Produto')
    
    canvasGrafico = FigureCanvasTkAgg(fig, master=graficoLucro)
    canvasGrafico.draw()
    canvasGrafico.get_tk_widget().pack()

def atualizarPagina():
    telaAdm.destroy()
    telaDoAdministrador()

def telaDoAdministrador():
    global estoque,graficoVendas, graficoLucro, pedidos, telaAdm, estoqueGeral

    telaAdm = Tk()  
    telaAdm.geometry("1300x600")
    telaAdm.title("Tela do Administrador")
    telaAdm.resizable(False,False)
    telaAdm.config(bg="#6495ED",pady=50, padx =5)

    # --------- Div graficos

    divGraficos = LabelFrame(telaAdm, font=("Arial", 16, "bold"), text="Informações", padx=20)
    divGraficos.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")
    divGraficos.config(height=600)


    # --------- Notebook

    notebook = ttk.Notebook(divGraficos)
    notebook.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")

    # ------ aba grafico de vendas
    graficoVendas = Frame(notebook)
    notebook.add(graficoVendas, text=f"Gráfico de Vendas")
    criaGraficoVendas()

    # ------ aba de Lucro
    graficoLucro = Frame(notebook)
    notebook.add(graficoLucro, text=f"Gráfico de Lucro")
    criaGraficoLucro()

    # ------ aba Estoque
    estoque = ttk.Treeview(notebook, selectmode="browse", columns=("coluna1","coluna2","coluna3","coluna4"), show='headings')
    estoque.column("coluna1", width=200, minwidth=80, stretch=YES)
    estoque.heading("#1", text="Código")
    estoque.column("coluna2", width=200, minwidth=80, stretch=YES)
    estoque.heading("#2", text="Produto")
    estoque.column("coluna3", width=200, minwidth=80, stretch=YES)
    estoque.heading("#3", text="Preço")
    estoque.column("coluna4", width=200, minwidth=80, stretch=YES)
    estoque.heading("#4", text="Estoque")
    estoque.tag_configure("my_font", font=("Arial", 12))
    estoque.pack(fill="both", expand=True)
    atualizarEstoque()
    notebook.add(estoque,text=f"Estoque")

    # ------- produtos em pedidos

    pedidos = ttk.Treeview(notebook, selectmode="browse", columns=("coluna1","coluna2","coluna3","coluna4"), show='headings')
    pedidos.column("coluna1", width=200, minwidth=80, stretch=YES)
    pedidos.heading("#1", text="Código")
    pedidos.column("coluna2", width=200, minwidth=80, stretch=YES)
    pedidos.heading("#2", text="Produto")
    pedidos.column("coluna3", width=200, minwidth=80, stretch=YES)
    pedidos.heading("#3", text="Fornecedor")
    pedidos.column("coluna4", width=200, minwidth=80, stretch=YES)
    pedidos.heading("#4", text="Estoque")
    pedidos.tag_configure("my_font", font=("Arial", 12))
    pedidos.pack(fill="both", expand=True)
    produtosPedidos()
    notebook.add(pedidos,text=f"Pedidos em andamento")

    # -------- Email dos fornecedores

    estoqueGeral = ttk.Treeview(notebook, selectmode="browse", columns=("coluna1","coluna2","coluna3","coluna4","coluna5","coluna6","coluna7","coluna8","coluna9"), show='headings')
    estoqueGeral.column("coluna1", width=60,stretch=NO)
    estoqueGeral.heading("coluna1", text="Código")
    estoqueGeral.column("coluna2", width=150,stretch=NO)
    estoqueGeral.heading("coluna2", text="Produto")
    estoqueGeral.column("coluna3", width=80,stretch=NO)
    estoqueGeral.heading("coluna3", text="Quantidade")
    estoqueGeral.column("coluna4", width=100, minwidth=40, stretch=NO)
    estoqueGeral.heading("coluna4", text="Preço de Compra")
    estoqueGeral.column("coluna5", width=100, minwidth=40, stretch=NO)
    estoqueGeral.heading("coluna5", text="Preço de Venda")
    estoqueGeral.column("coluna6", width=150, minwidth=80, stretch=NO)
    estoqueGeral.heading("coluna6", text="Fornecedor")
    estoqueGeral.column("coluna7", width=150, minwidth=80, stretch=NO)
    estoqueGeral.heading("coluna7", text="Validade")
    estoqueGeral.column("coluna8", width=60, minwidth=40, stretch=NO)
    estoqueGeral.heading("coluna8", text="Vendas")
    estoqueGeral.column("coluna9", width=100, minwidth=80, stretch=NO)
    estoqueGeral.heading("coluna9", text="Lucro")
    estoqueGeral.tag_configure("my_font", font=("Arial", 12))
    estoqueGeral.pack(fill="both", expand=True)
    exibirEstoqueGeral()

    notebook.add(estoqueGeral,text=f"Informações gerais do estoque")

    # -------- Div gerenciamento

    divGerenciamento = LabelFrame(telaAdm, font=("Arial", 16, "bold"), text="Gerenciamento", padx=20)
    divGerenciamento.grid(column=1, row=0, padx=10, pady=10, sticky="nsew")

    labelAdd = Label(divGerenciamento,text="Adicionar produto ao estoque:",font=("Arial", 10))
    labelAdd.grid(column=0,row=0, pady=15)
    botaoAdd = Button(divGerenciamento, text="Adicionar", command=tg.telaAdicionar)
    botaoAdd.config(background="#509078", font=("Arial",8))
    botaoAdd.grid(column=0,row=1)
    botaoAdd.config(width=12)


    labelEditar = Label(divGerenciamento,text="Editar produto do estoque:",font=("Arial", 10))
    labelEditar.grid(column=0,row=2, pady=15)
    botaoEditar = Button(divGerenciamento, text="Editar", command=tg.telaDeEditar)
    botaoEditar.config(background="#FEEBD7", font=("Arial",8))
    botaoEditar.grid(column=0,row=3)
    botaoEditar.config(width=12)

    labelExcluir = Label(divGerenciamento,text="Remover produto do estoque:",font=("Arial", 10))
    labelExcluir.grid(column=0,row=4, pady=15)
    botarExcluir = Button(divGerenciamento, text="Remover", command=tg.telaRemover)
    botarExcluir.config(background="#FFA3A0", font=("Arial",8))
    botarExcluir.grid(column=0,row=5)
    botarExcluir.config(width=12)

    labelFornecedor  = Label(divGerenciamento,text="Entrar com contato fornecedor:",font=("Arial", 10))
    labelFornecedor.grid(column=0,row=6, pady=15)
    botaoFornecedor = Button(divGerenciamento, text="Enviar Email", command=tg.telaEnviarEmail)
    botaoFornecedor.config(background="#F0F0F0", font=("Arial",8))
    botaoFornecedor.grid(column=0,row=7)
    botaoFornecedor.config(width=12)

    labelAtualizar  = Label(divGerenciamento,text="Atualizar página de estoque:",font=("Arial", 10))
    labelAtualizar.grid(column=0,row=8, pady=15)
    botaoAtualizar = Button(divGerenciamento, text="Atualizar", command=atualizarPagina)
    botaoAtualizar.config(background="#888888", font=("Arial",8))
    botaoAtualizar.grid(column=0,row=9)
    botaoAtualizar.config(width=12)

    telaAdm.mainloop()