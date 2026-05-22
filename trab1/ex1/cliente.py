import socket, threading, time

nickname = "user"

def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')

            print(message)
        except:
            print("Conexao perdida")
            break

def send_message(client_socket):
    global nickname

    while True:
        message = input()

        if message.startswith("/nick "):
            nickname = message.split(' ', 1)[1]

        elif message == '/sair':
            client_socket.close()
            break

        else:
            full_message = f"{nickname}: {message}"
            client_socket.send(full_message.encode('utf-8'))

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(('localhost', 8000))

    receive_thread = threading.Thread(target=receive_message, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_message, args=(client,))
    send_thread.start()


if __name__ == "__main__":
    start_client()