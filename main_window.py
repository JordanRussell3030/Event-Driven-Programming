from PyQt4.QtGui import *
from PyQt4.QtCore import *
from name_widget import *
from second_widget import *
from stack_widget import *

import sys

class MyWindow(QMainWindow):
    NameEntered = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.name_widget = NameWidget()
        self.second_widget = SecondWidget()

        self.stack = QStackedLayout()
        
        self.stack.addWidget(self.name_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

        self.name_widget.NameEntered.connect(self.name_provided)
        self.second_widget.BackActivated.connect(self.BackActivated)

    def name_provided(self):
        self.stack.setCurrentIndex(1)
        name = self.name_widget.username.text()
        self.second_widget.message.setText("Hello " + name)

    def BackActivated(self):
        self.stack.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
