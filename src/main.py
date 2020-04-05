import sys

# import local files
from src import gui
from src import socketclient

host = '192.168.11.11'
port = 8080

if __name__ == "__main__":
    network = socketclient.SocketClient()

    app = gui.QApplication(sys.argv)
    ex = gui.App()
    sys.exit(app.exec_())
