import socket
import threading
import time

class SocketClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((host, port))
        self.response = ""
        t1 = threading.Thread(target=self.receiveThread)
        t1.start()

    def sendThread(self, msg):
        self.clientSocket.sendall(msg.encode('utf-8'))


    def receiveThread(self):
        while True:
            time.sleep(1)
            self.response += self.clientSocket.recv(2048).decode('utf-8') + '\n'
            print(self.response)


    def getres(self):
        print("returning")
        return self.response
