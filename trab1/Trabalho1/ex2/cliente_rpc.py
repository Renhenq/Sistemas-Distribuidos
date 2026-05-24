# Integrantes do grupo: Renan Henrique - 12311BCC036
#                       Sophia Ladir - 12311BCC004 

import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

print("--- Catálogo Remoto ---")
print("Livros disponíveis:")
print("ISBN: 9788501012074 | Cem Anos de Solidão")
print("ISBN: 9786556400785 | Bufo e Spallanzani")
print("ISBN: 9788535933925 | Capitães da Areia")
print("ISBN: 9788535910667 | Vidas Secas")

while True:
    print("\nOpções:")
    print("1 - Consultar dados do livro")
    print("2 - Calcular compra")
    print("3 - Sair")
    
    escolha = input("Escolha uma operação: ")

    if escolha == '1':
        a = input("Digite o ISBN do livro: ")
        resultado = proxy.dados(a)
        print("Resposta do Servidor:", resultado)

    elif escolha == '2':
        a = input("Digite o ISBN do livro: ")
        b = input("Digite a quantidade desejada: ")
        resultado = proxy.compra(a, b)
        print("Resposta do Servidor:", resultado)

    elif escolha == '3':
        print("Encerrando o cliente...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")