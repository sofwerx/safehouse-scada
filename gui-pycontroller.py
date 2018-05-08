'''
This app implements a GUI for user-friendly
manual control of the Nerf Gun System.
'''

from pycomm.ab_comm.clx import Driver as PLCDriver
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot
from gui import Ui_MainWindow

class AppGui(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(AppGui, self).__init__(parent)
        self.setupUi(self)
        self.positionBtn.clicked.connect(self.position_gun)

    def position_gun(self):
        c = PLCDriver()
        if c.open('192.168.0.203'):
            tag = 'nerfgun_position_fire'
            readtag = c.read_tag([str(tag)])
            value = int(readtag[0][1])

            if (value == 0):
                writetag = c.write_tag((tag, 1, 'BOOL'))
                print('Moving Up')
            elif (value == 1):
                writetag = c.write_tag((tag, 0, 'BOOL'))
                print('Moving Down')
            else:
                print('Error!')
        c.close()


if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    window = AppGui()
    window.show()

    sys.exit(app.exec_())
