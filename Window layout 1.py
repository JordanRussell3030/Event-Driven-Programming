from PyQt4.QtGui import *

class NameWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.username = QLineEdit()
        self.label = QLabel("Please enter your name: ")
        self.submit = QPushButton("Submit")

        self.layout = QHBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.username)
        self.layout.addWidget(self.submit)

        self.setLayout(self.layout)

if __name__ == "__main__":
    test = MainWidget()
