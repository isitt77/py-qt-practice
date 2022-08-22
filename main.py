# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow


def clicked():
    print("Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("PyQt Window")

    # location of label
    label = QtWidgets.QLabel(win)
    label.setText("Label")
    # label positioning
    label.move(140,50)

    #Buttons
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Submit")
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec())
