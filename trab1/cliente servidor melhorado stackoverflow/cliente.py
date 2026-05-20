from socket import *
import time

serverHost = 'localhost'
serverPort = 50007

# Adotei o caractere \n como fim de mensagem
mensagem = [b'Ola mundo da internet!\n', b'bla\n', b'ble\n']

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

for linha in mensagem:
    time.sleep(1)

    while linha:
        enviado = sockobj.send(linha)
        if enviado == 0:
            print("Servidor fechou")
            break
        # corta parte da linha ja enviada
        linha = linha[enviado:]

    data = b''
    # Adotei o caractere \n como fim de mensagem
    while b'\n' not in data: 
         newdata = sockobj.recv(1024)
         if not newdata:
             print('Servidor fechou conexao')
             break
         data += newdata
    print('Cliente recebeu:', data)

sockobj.close()