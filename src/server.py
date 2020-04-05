import socket


host = '192.168.11.11'
port = 8080

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind((host, port))
ss.listen(2)

print("Waiting for connections")
client, addr = ss.accept()

while True:
    rcvmsg = client.recv(2048)
    print(rcvmsg.decode('utf-8'))
    if rcvmsg == '':
        break
    print('type message')
    s_msg = input()
    if s_msg == '':
        break

    client.sendall(s_msg.encode('utf-8'))

client.close()
