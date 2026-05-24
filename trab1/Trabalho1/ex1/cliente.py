# Integrantes do grupo: Renan Henrique - 12311BCC036
#                       Sophia Ladir - 12311BCC004 

import socket, threading, time

# variável global para o nome do usuário a ser mostrado 
nickname = "user"

# função para receber uma mensagem do servidor
def receive_message(client_socket):
    # loop infinito para ficar esperando uma mensagem
    while True: 
        try:
            # reecebe dados do socket e converte de bytes para string
            message = client_socket.recv(1024).decode('utf-8')
            # mostra a mensagem para o cliente
            print(message)
        except:
            # caso ocorra erro
            print("Conexao perdida")
            break

# função para receber mensagem do cliente e enviar para o servidor
def send_message(client_socket):
    global nickname

    # loop infinito para ficar esperando uma mensagem do usuário
    while True: 
        # recebe mensagem do cliente
        message = input()

        # se começar com /nick, é para alterar o nick do usuário
        if message.startswith("/nick "):
            nickname = message.split(' ', 1)[1]

        # se começar com /sair, encerra conexão
        elif message == '/sair':
            client_socket.close()
            break

        # envia mensagem para o servidor
        else:
            full_message = f"{nickname}: {message}"
            # converte mensagem de string para bytes e envia para o servidor
            client_socket.send(full_message.encode('utf-8'))

# função para inicializar cliente
def start_client():
    global nickname

    nickname = input("Digite seu nickname: ")

    # cria socket do cliente com endereço ipv4 e protocolo tcp
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # conecta ao servidor na porta 8000
    client.connect(('localhost', 8000))

    # envia o nickname do cliente para o servidor
    client.send(nickname.encode('utf-8'))

    # cria uma thread executando a função receive message
    # passa o socket do cliente como argumento
    receive_thread = threading.Thread(target=receive_message, args=(client,))
    receive_thread.start()

    # cria uma thread executando a função send message
    # passa o socket do cliente como argumento
    send_thread = threading.Thread(target=send_message, args=(client,))
    send_thread.start()


if __name__ == "__main__":
    start_client()