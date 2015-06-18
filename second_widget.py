from PyQt4.QtGui import *

class SecondWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.username = QLineEdit()
        self.label = QLabel("Hello {0}".format(self.username.text()))
        self.submit = QPushButton("Back")
        NameEntered = pyqtSignal()

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.username)
        self.layout.addWidget(self.submit)

        self.setLayout(self.layout)
        self.submit.clicked.connect(self.submit_pushed)

    def submit_pushed(self):
        print("Back")
