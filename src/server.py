import socket
import threading


host = '192.168.11.11'
port = 8080

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind((host, port))
ss.listen(2)


def sendThread(socket):
    while True:
        print("type messages")
        msg = input()
        socket.sendall(msg.encode('utf-8'))


def receiveThread(socket):
    while True:
        res = socket.recv(2048)
        print("Received -> %s" % res.decode('utf-8'))


print("Waiting for connections")
client, addr = ss.accept()

t1 = threading.Thread(target=sendThread, args=(client, ))
t2 = threading.Thread(target=receiveThread, args=(client, ))

t1.start()
t2.start()
t1.join()
t2.join()

client.close()
