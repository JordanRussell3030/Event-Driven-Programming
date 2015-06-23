from PyQt4.QtGui import *
from PyQt4.QtCore import *
from stack_widget import *
from main_window import *
from name_widget import *

class SecondWidget(QWidget):
    BackActivated = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.message = QLabel()
        self.button = QPushButton("Back")
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.message)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
        
        self.button.clicked.connect(self.submit_pushed)

    def submit_pushed(self):
        self.BackActivated.emit()
        print("Back")
        
