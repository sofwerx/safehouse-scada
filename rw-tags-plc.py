
from pycomm.ab_comm.clx import Driver as ClxDriver
import logging
import time
from multiprocessing import Process
import sys
from threading import Timer
from time import sleep


def motor_state(t_end):
    print'motor on'
    while time.time() < t_end:
        c.write_tag([('nerfgun_position_fire',0,'BOOL'),('trigger_motor_on',1,'BOOL')])
    c.write_tag(('trigger_bullet_fire',1,'BOOL'))


def fire_bullets(t_end2):
    print'Fire Bullets'
    while time.time() < t_end2:
        c.write_tag([('trigger_bullet_fire',1,'BOOL')])
    c.write_tag([('trigger_bullet_fire',0,'BOOL'),('trigger_motor_on',0,'BOOL')])


def hide_gun():
    print 'Hide Gun'
    time.sleep(1)
    c.write_tag(('nerfgun_position_fire',1,'BOOL'))


def parse_msg(message,fp):
    t_end = time.time() + 60 * .02
    t_end2 = time.time() + 60 * .058

    if "longgun" in message:
        motor_state(t_end)
        fire_bullets(t_end2)
        hide_gun()
        while "longgun" in message:
            message = fp.readline()


# def handleInput(incomingMessage):
#     for ch in incomingMessage:
#         handleCh(ch)

if __name__ == '__main__':

    # logging.basicConfig(
    #     filename="ClxDriver.log",
    #     format="%(levelname)-10s %(asctime)s %(message)s",
    #     level=logging.DEBUG
    # )

    c = ClxDriver()

    print c['port']
    print c.__version__

    filepath = "/home/nvidia/Documents/yolov2/capturedetect"
    if c.open('192.168.0.203'):

        with open(filepath) as fp:
            while 1:
                line = fp.readline()
                try:
                    parse_msg(line,fp)
                except ValueError as e:
                    c.close()
                    print e
                    pass

    c.close()
