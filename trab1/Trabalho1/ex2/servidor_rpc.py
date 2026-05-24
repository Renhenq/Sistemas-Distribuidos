# Integrantes do grupo: Renan Henrique - 12311BCC036
#                       Sophia Ladir - 12311BCC004 

from xmlrpc.server import SimpleXMLRPCServer

catalogo = {
    "9788501012074": {"titulo": "Cem Anos de Solidão", "autor": "Gabriel García Márquez", "editora": "Record", "preco": 35.00},
    "9786556400785": {"titulo": "Bufo e Spallanzani", "autor": "Rubem Fonseca", "editora": "Nova Fronteira", "preco": 20.00},
    "9788535933925": {"titulo": "Capitães da Areia", "autor": "Jorge Amado", "editora": "Companhia das Letras", "preco": 28.00},
    "9788535910667": {"titulo": "Vidas Secas", "autor": "Graciliano Ramos", "editora": "Record", "preco": 24.90}
}

# função para retornar dados de um livro para o cliente
def dados(a):
    livro = catalogo.get(str(a))
    if livro:
        return f"ISBN: {a}, Autor: {livro['autor']}, Editora: {livro['editora']}, Preço: R$ {livro['preco']:.2f}"
    return "Erro: Livro não encontrado. Verifique o ISBN."

# função para calcular e retornar o valor total de uma compra do cliente
def compra(a, b):
    livro = catalogo.get(str(a))
    if livro:
        try:
            quantidade = int(b)
            total = livro['preco'] * quantidade
            return f"Cálculo da venda ({quantidade}x {livro['titulo']}): R$ {total:.2f}"
        except ValueError:
            return "Erro: A quantidade informada é inválida."
    return "Erro: Livro não encontrado. Verifique o ISBN."

# cria servidor XML-RPC
server = SimpleXMLRPCServer(("localhost", 8000))

print("Servidor RPC executando na porta 8000...")
# registra as funções do servidor para serem acessadas pelo cliente
server.register_function(dados, "dados")
server.register_function(compra, "compra")

# mantém servidor ativo
server.serve_forever()