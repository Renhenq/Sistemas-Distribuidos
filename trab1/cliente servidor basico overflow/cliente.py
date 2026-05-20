import socket, threading, sys, select

def receber_mensagem(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            break

with socket.socket() as s:
    s.connect(('localhost', 50007))

    thread_receber = threading.Thread(
        target=receber_mensagem,
        args=(s,)
    )

    thread_receber.start()

    while True:
        msg = input()
        s.send(msg.encode())

"""
with socket.socket() as s: # cria socket tcp
    s.connect(('localhost', 50007)) # conecta ao servidor na porta 50007
    while True:
        io_list = [sys.stdin, s] # lista de entradas monitoradas(teclado, socket)
        ready_to_read,ready_to_write,in_error = select.select(io_list , [], [])   # select espera entrada do teclado ou mensagem do servidor
        if s in ready_to_read: # se servidor enviou dados
            data = s.recv(1024) # recebe mensagem
            if(not data): # ex: caso o servidor se desligue, ou conexao perdida
                break
            print(data.decode())  # converte bytes para string
        else: # enviar msg
            msg = sys.stdin.readline() # capturar mensagem inserida no terminial, no command prompt
            s.send(msg.encode())  # convert string para bytes
            sys.stdout.flush()
"""