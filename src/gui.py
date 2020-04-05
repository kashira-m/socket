import sys
import time
import threading
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QLineEdit, QMessageBox, QTextEdit
from PyQt5.QtCore import pyqtSlot

from src import socketclient

host = '192.168.11.11'
port = 8080

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "PyQt5 textbox - pythonspot.com"
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 500
        self.initUI()

        self.network = socketclient.SocketClient(host, port)
        self.receiver = threading.Thread(target=self.updateTimeline)
        self.receiver.start()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 450)
        self.textbox.resize(280, 40)

        # Create timeline
        self.timeline = QTextEdit(self)
        self.timeline.move(20, 20)
        self.timeline.resize(280, 400)
        self.timeline.setReadOnly(False)
        self.timeline.setText("Timeline")

        # Create a button in the window
        self.button = QPushButton("send", self)
        self.button.move(300, 450)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        self.network.sendThread(textboxValue)
        self.textbox.setText("")


    def updateTimeline(self):
        while True:
            time.sleep(1)
            msg = self.network.getres()
            # self.timeline.setText(msg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()

    sys.exit(app.exec_())


