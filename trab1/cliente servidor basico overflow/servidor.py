import socket, threading
# uma thread da função para cada cliente
def handle_client(client_conn): # client_conn: socket do client especifico
    while True: # espera mensagem continuamente
        try:
            data = client_conn.recv(1024) #recebe 1024 bytes
            if (not data): # sem data, cliente desconectou
                print(client_conn.getpeername(), 'desconectou')
                return
            client_conn.send(b'Eco=>' + data) # envia mensagem resposta
        except:
            print("cliente fechou conexao abruptamente")
            break
    client_conn.close()

with socket.socket() as s: # cria socket tcp/ip
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reutilizar porta logo após servidor terminal, evita a excepcao 'OSError: [Errno 98] Address already in use'
    s.bind(('', 50007)) # localhost por default no primeiro elemento do tuple; 
                        # associa IP porta
    s.listen(5) 
    while True: # aceitar todas as conexoes que possam vir
        conexao, endereco = s.accept() # espera alguem conectar
        print('Server conectado por', endereco)
        threading.Thread(target=handle_client, args=(conexao,)).start() # para cada cliente, cria thread e executa handle_client => varios clientes simultaneamente