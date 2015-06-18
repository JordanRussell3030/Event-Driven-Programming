from PyQt4.QtGui import *
from PyQt4.QtCore import *
from name_widget import *
from second_widget import *

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.name_widget = NameWidget()
        self.setCentralWidget(self.name_widget)
        self.name_widget.NameEntered.connect(self.name_provided)
        self.second_widget = SecondWidget()
        self.setCentralWidget(self.second_widget)
        name = self.name_widget.username.text()
        print(name)
        self.name_widget.label.setText(name)

    def name_provided(self):
        print("Got here")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
