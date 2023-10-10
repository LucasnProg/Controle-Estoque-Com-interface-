from pandas import *
import matplotlib.pyplot as plt
import smtplib
import email.message

def fazerPedido(remetente, corpo):
    mensagem = f'''
        Olá, gostariamos de efetivar um pedido de mais 100 unidades de {corpo} com urgencia por favor!
    '''
    msg = email.message.Message()
    msg['Subject'] = "Pedido!"
    msg['From'] = "email"
    msg['To'] = remetente
    senha = "senha"
    msg.set_payload(mensagem)
    
    conexao =smtplib.SMTP("smtp.gmail.com: 587") 
    conexao.starttls()
    conexao.login(msg['From'], senha)
    conexao.sendmail(msg['From'],msg['To'], msg.as_string().encode('utf-8'))

def enviarEmail(remetente,assunto,corpo):
    mensagem = corpo
    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = "lucasnprog@gmail.com"
    msg['To'] = remetente
    senha = "lwfeikyvsrejtfmy"
    msg.set_payload(mensagem)
    
    conexao =smtplib.SMTP("smtp.gmail.com: 587") 
    conexao.starttls()
    conexao.login(msg['From'], senha)
    conexao.sendmail(msg['From'],msg['To'], msg.as_string().encode('utf-8'))

def adicionarProduto(codigo, descricao,qtd,compra,venda,fornecedor, validade):  
    global bancoProdutos
    novoProduto = {"ID_produto" : codigo, 
                   "Descrição_produto": descricao,
                   "qtd_produto":qtd,
                   "preco_produto":compra,
                   "preco_venda":venda,
                   "fornecedor": fornecedor,
                   "validade": validade,
                   "num_vendas": 0,
                   "Lucro":0
                   }
    dfNovoProduto = DataFrame([novoProduto])
    bancoProdutos = concat([bancoProdutos, dfNovoProduto], ignore_index=False)
    bancoProdutos.to_excel('planilhaProdutos.xlsx', index=False,sheet_name='Estoque')

def editarProduto(codigo,produtoNovo,qtdNova,precoVendaNovo,fornecedorNovo):
    global bancoProdutos
    bancoProdutos.loc[bancoProdutos['ID_produto'] == codigo, 'Descrição_produto'] = produtoNovo
    bancoProdutos.loc[bancoProdutos['ID_produto'] == codigo, 'qtd_produto'] = qtdNova
    bancoProdutos.loc[bancoProdutos['ID_produto'] == codigo, 'preco_venda'] = precoVendaNovo
    bancoProdutos.loc[bancoProdutos['ID_produto'] == codigo, 'fornecedor'] = fornecedorNovo
    bancoProdutos.to_excel('planilhaProdutos.xlsx', index=False, sheet_name='Estoque')


def consultaId(consulta):
    return bancoProdutos['ID_produto'].isin([consulta]).any()

def consultaDescricao(consulta):
    return bancoProdutos['Descrição_produto'].isin([consulta]).any()

def consultaFornecedor(consulta):
    return bancoProdutos['fornecedor'].isin([consulta]).any()


def verificarQuantidade(id,quantidade):
    if quantidade <0:
        return False
    elif quantidade > bancoProdutos.loc[(bancoProdutos['ID_produto']==id),"qtd_produto"].values[0]:
        return False
    else:
        return True

def compra(id, quantidade):
    bancoProdutos.loc[bancoProdutos['ID_produto'] == id, 'qtd_produto'] -= quantidade 
    bancoProdutos.loc[bancoProdutos['ID_produto'] == id, 'num_vendas'] += quantidade
    bancoProdutos.loc[bancoProdutos['ID_produto'] == id, 'Lucro'] += ((bancoProdutos.loc[bancoProdutos['ID_produto'] == id, 'preco_venda'].values[0])*quantidade)

    bancoProdutos.to_excel('planilhaProdutos.xlsx', index=False,sheet_name='Estoque')

def buscarNomeProduto(codigo):
    nomeProduto = bancoProdutos.loc[bancoProdutos['ID_produto'] == codigo, 'Descrição_produto'].values[0]
    return nomeProduto
def buscarPrecoProduto(codigo):
    precoProduto = bancoProdutos.loc[bancoProdutos['ID_produto'] == codigo, 'preco_venda'].values[0]
    return precoProduto

def removerProduto(id):
    global bancoProdutos
    bancoProdutos = bancoProdutos.drop(bancoProdutos.loc[bancoProdutos['ID_produto'] == id].index)
    bancoProdutos.to_excel('planilhaProdutos.xlsx', index=False,sheet_name='Estoque')



bancoProdutos = read_excel('planilhaProdutos.xlsx', sheet_name='Estoque')
