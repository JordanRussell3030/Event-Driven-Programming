from PyQt4.QtGui import *
from PyQt4.QtCore import *
from main_window import *
from name_widget import *
from second_widget import *

class StackWidget(QWidget):
    NameEntered = pyqtSignal()
    def __init__(self):
        super().__init__()

    #create stack layout
        self.stack = QStackedLayout()
        
        self.stack.addWidget(self.name_widget)
        self.stack.addWidget(self.second_widget)

    #add stack to central widget
        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

        self.submit.clicked.connect(self.submit_pushed)

    def name_provided(self):
        self.stack.setCurrentIndex[1]
        name = self.name_widget.username.text()
        self.hello_widget.label.setText(name)


if __name__ == "__main__":
    new_widget = StackWidget()

