# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("PyQt Window")
        self.initUI()

    def initUI(self):
        # location of label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label")
        # label positioning
        self.label.move(140,50)

        #Buttons
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Submit")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You clicked the button.")
        self.adjustLabelSize()

    def adjustLabelSize(self):
        self.label.adjustSize()


def clicked():
    print("Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
#    win = QMainWindow()
    win = MyWindow()

# Move to __init__(self)
#    win.setGeometry(200, 200, 300, 300)
#    win.setWindowTitle("PyQt Window")

# move to initUI(self)
#    # location of label
#    label = QtWidgets.QLabel(win)
#    label.setText("Label")
#    # label positioning
#    label.move(140,50)

#    #Buttons
#    b1 = QtWidgets.QPushButton(win)
#    b1.setText("Submit")
#    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec())
