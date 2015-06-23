from PyQt4.QtGui import *
from PyQt4.QtCore import *
from stack_widget import *
from main_window import *

class NameWidget(QWidget):
    NameEntered = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.username = QLineEdit()
        self.label = QLabel("Please enter your name: ")
        self.submit = QPushButton("Submit")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.username)
        self.layout.addWidget(self.submit)

        self.setLayout(self.layout)

        self.submit.clicked.connect(self.submit_pushed)
    

    def submit_pushed(self):
        name = self.username.text()
        print(name)
        self.NameEntered.emit()


