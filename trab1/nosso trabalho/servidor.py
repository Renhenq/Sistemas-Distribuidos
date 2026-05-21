import socket, threading

clientes = []
lock = threading.Lock()

def handle_client(conn, addr):
    print(f"{addr} se conectou ao servidor")

    wellcome_msg = (
        "Bem vindo.\n"
        "Comandos:\n" 
        "\t/nick - alterar seu nome de usuário\n"
        "\t/sair - encerrar conexão com o servidor\n"
    )
    conn.send(wellcome_msg.encode('utf-8'))

    with lock:
        clientes.append(conn)

    try:
        while True:
            message = conn.recv(1024).decode('utf-8')
            
            if not message:
                break
        
            print(f"Messagem de {addr}: {message}")

            broadcast(message, conn)
            
    except:
        pass

    finally:
        with lock:
            if conn in clientes:
                clientes.remove(conn)
        
        conn.close()
        print(f"conexao de {addr} encerrada")

    
def broadcast(message, conn):
    with lock:
        for cliente in clientes:
            if cliente != conn:
                cliente.send(message.encode('utf-8'))


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(('0.0.0.0', 8000))

    server.listen()

    print("Servidor iniciado na porta 8000")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start_server()