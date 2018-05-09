'''
This app implements a GUI for user-friendly
manual control of the Nerf Gun System.
'''

from pycomm.ab_comm.clx import Driver as PLCDriver
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot
from gui import Ui_MainWindow

plc_ip = "192.168.0.203"

class AppGui(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(AppGui, self).__init__(parent)
        self.setupUi(self)
        self.positionBtn.setCheckable(True)
        self.motorBtn.setCheckable(True)
        self.triggerBtn.setCheckable(True)
        self.positionBtn.clicked[bool].connect(self.position_gun)
        self.motorBtn.clicked[bool].connect(self.motor)
        self.triggerBtn.clicked[bool].connect(self.trigger)
        self.resetBtn.clicked.connect(self.reset)

    def position_gun(self):
        c = PLCDriver()
        if c.open(plc_ip):
            tag = 'nerfgun_position_fire'
            r_tag = c.read_tag([str(tag)])
            value = int(r_tag[0][1])

            if (value == 0):
                w_tag = c.write_tag((tag, 1, 'BOOL'))
                self.positionBtn.setText(" Drop Gun ")

                print('Moving Up')
            elif (value == 1):
                w_tag = c.write_tag((tag, 0, 'BOOL'))
                self.positionBtn.setText(" Hide Gun ")

                print('Moving Down')
            else:
                print('Error!')
        c.close()

    def motor(self):
        c = PLCDriver()
        if c.open(plc_ip):
            tag = 'trigger_motor_on'
            r_tag = c.read_tag([str(tag)])
            value = int(r_tag[0][1])

            if (value == 0):
                w_tag = c.write_tag((tag, 1, 'BOOL'))
                self.motorBtn.setText(" Stop Motor ")
                print('Motor On')

            elif (value == 1):
                w_tag = c.write_tag((tag, 0, 'BOOL'))
                self.motorBtn.setText(" Start Motor ")
                print('Motor Off')
            else:
                print('Error!')
        c.close()

    def trigger(self):
        c = PLCDriver()
        if c.open(plc_ip):
            tag = 'trigger_bullet_fire'
            r_tag = c.read_tag([str(tag)])
            value = int(r_tag[0][1])

            if (value == 0):
                w_tag = c.write_tag((tag, 1, 'BOOL'))
                self.triggerBtn.setText(" Stop Firing ")
                print('Firing On')

            elif (value == 1):
                w_tag = c.write_tag((tag, 0, 'BOOL'))
                self.triggerBtn.setText(" Fire Bullets ")
                print('Firing Off')
            else:
                print('Error!')
        c.close()

    def reset(self):
        c = PLCDriver()
        if c.open(plc_ip):
            pos_tag = 'nerfgun_position_fire'
            motor_tag = 'trigger_motor_on'
            fire_tag = 'trigger_bullet_fire'

            c.write_tag((pos_tag, 1, 'BOOL'))
            c.write_tag((motor_tag, 0, 'BOOL'))
            c.write_tag((fire_tag, 0, 'BOOL'))

            print('Resetting Position')


            self.triggerBtn.setText(" Drop Gun ")
            self.motorBtn.setText(" Start Motor ")
            self.triggerBtn.setText(" Fire Bullets ")

        c.close()

if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    window = AppGui()
    window.show()

    sys.exit(app.exec_())
