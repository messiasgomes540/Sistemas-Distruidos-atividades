

import socket
import threading


ip ="0.0.0.0"

porta = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((ip, porta))

server.listen(5)

print ( "ouvindo cliente em %s : %d"  % (ip, porta))

def cliente (cliente_socket):

    resposta = cliente_socket.recv(1024)

    print ( "resposta %s" % resposta)


    cliente_socket.send("resposta  do servidor :  ok, conectado com sucesso!!!")

    cliente_socket.close()

while True:

    client, addr= server.accept()

    print ("recebendo conexao por : %s:%d" % (addr[0], addr[1]))

    cliente = threading.Thread(target=cliente, args=(client,))

    cliente.start()
