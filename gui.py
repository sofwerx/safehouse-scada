# import sys
# from PyQt4 import QtGui
#
#
# def window():
#     app = QtGui.QApplication(sys.argv)
#     w = QtGui.QWidget()
#     b = QtGui.QLabel(w)
#     b.setText("Hello World!")
#     w.setGeometry(100, 100, 200, 50)
#     b.move(50, 20)
#     w.setWindowTitle('PyQt')
#     w.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     window()


import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)



        layout = QVBoxLayout()
        self.b1 = QPushButton("Position Gun")
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.clicked.connect(lambda: self.whichbtn(self.b1))
        self.b1.clicked.connect(self.btnstate)
        layout.addWidget(self.b1)

        self.b1 = QPushButton("Trigger Motor")
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.clicked.connect(lambda: self.whichbtn(self.b1))
        self.b1.clicked.connect(self.btnstate)

        layout.addWidget(self.b1)


        self.b4 = QPushButton("&Fire Bullets")
        self.b4.setDefault(True)
        self.b4.clicked.connect(lambda: self.whichbtn(self.b4))
        layout.addWidget(self.b4)

        self.setLayout(layout)

        self.setWindowTitle("Sentry Gun Console")

    def btnstate(self):
        if self.b1.isChecked():
            print "button pressed"
        else:
            print "button released"

    def whichbtn(self, b):
        print "clicked button is " + b.text()


def main():
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()