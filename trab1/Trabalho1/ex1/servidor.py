# Integrantes do grupo: Renan Henrique - 12311BCC036
#                       Sophia Ladir - 12311BCC004 

import socket, threading

# lista com todos clientes conectados
clientes = []
# variável para evitar concorrência
lock = threading.Lock()

# função para tratar um cliente
def handle_client(conn, addr):
    print(f"{addr} se conectou ao servidor")

    # recebe nickname
    nickname = conn.recv(1024).decode('utf-8')

    # cria mensagem incial e envia para o cliente
    wellcome_msg = (
        f"Bem vindo, {nickname}.\n"
        "Comandos:\n" 
        "\t/nick - alterar seu nome de usuário\n"
        "\t/sair - encerrar conexão com o servidor\n"
    )
    conn.send(wellcome_msg.encode('utf-8'))

    with lock:
        clientes.append(conn)

    try:
        # loop infinito para ficar esperando uma mensagem do cliente
        while True:
            # recebe mensagem e decodifica de bytes para string
            message = conn.recv(1024).decode('utf-8')
            
            if not message:
                break
            # mostra mensagem do cliente no terminal do servidor
            print(f"Messagem de {addr}: {message}")

            # retransmite a mensagem para todos clientes
            broadcast(message, conn)
            
    # se ocorrer erro (cliente fechar), o programa continua
    except:
        pass

    finally:
        # remove o cliente da lista de clientes conectados
        with lock:
            if conn in clientes:
                clientes.remove(conn)
        # fecha conexão com o cliente desconectado
        conn.close()
        print(f"conexao de {addr} encerrada")

# função para retransmitir mensagem em broadcast
def broadcast(message, conn):
    # acessa lista de clientes conectados e retransmite a messagem para todos os outros
    with lock:
        for cliente in clientes:
            if cliente != conn:
                cliente.send(message.encode('utf-8'))

# função para inicializar servidor
def start_server():
    # cria socket do servidor com endereço ipv4 e protocolo tcp
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # cria o servidor na porta 8000
    # 0.0.0.0 para aceitar conexões de qualquer ip
    server.bind(('0.0.0.0', 8000))

    # servidor espera conexões
    server.listen()

    print("Servidor iniciado na porta 8000")

    # loop infinito para servidor permanecer ativo
    while True:
        # aceita cliente
        conn, addr = server.accept()

        # criar thread para lidar com esse cliente
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start_server()