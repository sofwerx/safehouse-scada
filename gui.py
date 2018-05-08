# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manualctrl.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        MainWindow.setMaximumSize(QtCore.QSize(400, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/sfg/nerf-gun/GUIAssests/swx-logo.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.horizontalGroupBox.setFont(font)
        self.horizontalGroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.horizontalGroupBox.setFlat(False)
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.positionBtn = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.positionBtn.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.positionBtn.setObjectName("positionBtn")
        self.verticalLayout_4.addWidget(self.positionBtn)
        self.motorBtn = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.motorBtn.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.motorBtn.setObjectName("motorBtn")
        self.verticalLayout_4.addWidget(self.motorBtn)
        self.triggerBtn = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.triggerBtn.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.triggerBtn.setObjectName("triggerBtn")
        self.verticalLayout_4.addWidget(self.triggerBtn)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.listView = QtWidgets.QListView(self.horizontalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.horizontalGroupBox)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetBtn.sizePolicy().hasHeightForWidth())
        self.resetBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.resetBtn.setFont(font)
        self.resetBtn.setStyleSheet("font: 11pt \"DejaVu Sans\";\n"
"background-color: rgb(245, 121, 0);\n"
"color: rgb(0, 0, 0);")
        self.resetBtn.setFlat(False)
        self.resetBtn.setObjectName("resetBtn")
        self.verticalLayout_2.addWidget(self.resetBtn)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.horizontalGroupBox.setTitle(_translate("MainWindow", "System Controls"))
        self.positionBtn.setText(_translate("MainWindow", " Drop Gun "))
        self.motorBtn.setText(_translate("MainWindow", " Start Motor"))
        self.triggerBtn.setText(_translate("MainWindow", "Start Trigger"))
        self.resetBtn.setText(_translate("MainWindow", "Reset All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

