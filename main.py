from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()  # Invoke constructor from parent class "QMainWindow"
        self.setWindowTitle("Title of window")
        self.setGeometry(500, 300, 500, 500)

        self.main_text = QtWidgets.QLabel(self)  # Add some text into window field
        self.main_text.setText("Create new window")
        self.main_text.move(100, 100)

        self.accept_button = QtWidgets.QPushButton(self)
        self.accept_button.move(50, 450)
        self.accept_button.setText("ADD NEW TEXT")
        self.accept_button.setFixedWidth(200)
        self.accept_button.clicked.connect(self.add_label)

        self.new_text = QtWidgets.QLabel(self)

    def add_label(self):
        # print("Add text")
        self.new_text.setText("WILD CARD")
        self.new_text.move(100, 200)

def application():
        app = QApplication(sys.argv)  # Get PC local settings by 'sys.argv' meth
        window = Window()  # Run all steps from '__init__' meth (class constructor)

        # __________________________Move to '__init__' meth_______________________________
        # window.setWindowTitle("Title of window") Move to '__init__' meth
        # window.setGeometry(500, 300, 500, 500)  # set coords 'x,y' and window size 'h, w'

        # main_text = QtWidgets.QLabel(self)   # Add some text into window field
        # main_text.setText("Create new window") # Move to '__init__' meth
        # main_text.move(100, 100)

        # accept_button = QtWidgets.QPushButton(self) # Move to '__init__' meth
        # accept_button.move(50, 450)
        # accept_button.setText("Apply")
        # accept_button.setFixedWidth(200)
        # accept_button.clicked.connect(add_label)
        # ____________________________________________________________________________
        window.show()  # Window is displayed on screen
        sys.exit(app.exec_())  # Code is finished correctly after running

if __name__ == "__main__":  # If run cuurent file 'main.py'
    application()
