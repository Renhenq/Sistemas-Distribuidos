from socket import *
import time
import threading

def cuida_cliente(conexao, endereco):
    print('Server conectado a', endereco)
    aberto = True

    while aberto:
        data = b''

        while b'\n' not in data:
            newdata = conexao.recv(1024)
            if not newdata:
                print("Cliente fechou")
                data = b''
                aberto = False
                break
            data += newdata

        if not data:
            break

        msg = b'Eco=>' + data + b'\n'
        while msg:
            enviado = conexao.send(msg)
            if enviado <= 0:
                print("Cliente fechou")
                aberto = False
                break
            msg = msg[enviado:]

    conexao.close()
    return

meuHost = ''
minhaPort = 50007
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((meuHost, minhaPort))
sockobj.listen(5)
while True:
    conexao, endereco = sockobj.accept()
    t = threading.Thread(target=cuida_cliente, args=(conexao, endereco))
    t.start()