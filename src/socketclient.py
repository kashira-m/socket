import socket


host = '192.168.11.11'
port = 8080

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.connect((host, port))

while True:
    print('type massage')
    msg = input()
    ss.send(msg.encode('utf-8'))
    res = ss.recv(2048)

    print(res.decode('utf-8'))
