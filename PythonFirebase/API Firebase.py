# Criar o projeto no Firebase

# Criar a Database (atenção as regras de segurança)
# Estrutura de árvore

# Interação com o database (REST API)
import requests
import json

link = "https://meuprojeto-ad02c-default-rtdb.firebaseio.com"

# Criar uma venda (POST)

#dados = {'cliente': 'fernando', 'preco': 150, 'produto': 'teclado'}
#requisicao = requests.post(f'{link}/Vendas/.json', data=json.dumps(dados))
#print(requisicao)
#print(requisicao.text)

# Criar um novo produto (POST)

#dados = {'nome': 'teclado', 'preco': 150, 'quantidade': '80'}
#requisicao = requests.post(f'{link}/Produtos/.json', data=json.dumps(dados))
#print(requisicao)
#print(requisicao.text)

# Editar a venda (PUT/PATCH)
#dados = {'cliente': 'mario'}
#requisicao = requests.patch(f'{link}/Vendas/-NJHjjSWV1ZgTYeTbBAk/.json', data=json.dumps(dados))
#print(requisicao)
#print(requisicao.text)

# Pegar uma venda específica ou todas as vendas (GET)
requisicao = requests.get(f'{link}/Vendas/.json')
print(requisicao)
dic_requisicao = requisicao.json()
id_mario = None
for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['cliente']
    if cliente == 'mario':
        print(id_venda)
        id_mario = id_venda

# Deletar uma venda (DELETE)
requisicao = requests.delete(f'{link}/Vendas/{id_mario}/.json')
print(requisicao)
print(requisicao.text)


# O que seria legal após isso?
# Autenticação
# Criar outras estruturas no seu banco de dados (vendedor, loja, cliente, estoque, etc.)