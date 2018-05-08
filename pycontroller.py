'''
------------------------------------------------------
Overview:
 This program serves as a hub of communication
 b/w the PLC & the TX2.

 PLC - SCADA System that controls the Nerf Gun
 TX2 - NVIDIA System w/ the AK47 Detection Program
------------------------------------------------------
More Info:
 Visit the Sofwerx GitHub at devwerx.org
------------------------------------------------------
'''

from pycomm.ab_comm.clx import Driver as ClxDriver
import logging
import time
import re
from multiprocessing import Process
import sys
from threading import Timer
from time import sleep

# Turns Motor On or Off
def motor_state(t_end):
    print('motor on')
    while time.time() < t_end:
        c.write_tag([('nerfgun_position_fire',0,'BOOL'),('trigger_motor_on',1,'BOOL')])
    c.write_tag(('trigger_bullet_fire', 1, 'BOOL'))

# Turns Trigger On or Off
def fire_bullets(t_end2):
    print('Fire Bullets')
    while time.time() < t_end2:
        c.write_tag([('trigger_bullet_fire',1,'BOOL')])
    c.write_tag([('trigger_bullet_fire',0,'BOOL'),('trigger_motor_on',0,'BOOL')])

# Positions Gun, Hidden or showing
def hide_gun():
    print('Hide Gun')
    time.sleep(1)
    c.write_tag(('nerfgun_position_fire',1,'BOOL'))

# Takes output of ak47 program as message
# Fires when 'longgun' appears in message
def parse_msg(message,fp):
    t_end = time.time() + 60 * .02
    t_end2 = time.time() + 60 * .058

    if "longgun" in message:
        motor_state(t_end)
        fire_bullets(t_end2)
        hide_gun()
        while "longgun" in message:
            message = fp.readline()


if __name__ == '__main__':

    c = ClxDriver()

    print('PLC Port Number: ' + str(c['port']))
    print('Driver Version: ' + str( c.__version__))

    # Path for AK47 Detection Program
    filepath = "/home/nvidia/Documents/yolov2/capturedetect"

    # IP address for PLC
    if c.open('192.168.0.203'):

        with open(filepath) as fp:
            while 1:
                line = fp.readline()
                try:
                    print(line.rstrip())
                    parse_msg(line,fp)
                except Exception as e:
                    c.close()
                    fp.close()

    c.close()
