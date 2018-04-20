
from pycomm.ab_comm.clx import Driver as ClxDriver
import logging
import time
from multiprocessing import Process
import sys
from threading import Timer
from time import sleep



def motorFunc(t_end):
    print'motor on'
    while time.time() < t_end:
        c.write_tag([('nerfgun_position_fire',0,'BOOL'),('trigger_motor_on',1,'BOOL')])
        #c.write_tag(('trigger_bullet_fire',1,'BOOL'))
    c.write_tag(('trigger_bullet_fire',1,'BOOL'))

def fireBullets(t_end2):
    #c.write_tag([('trigger_bullet_fire',1,'BOOL')])

    print'Fire Bullets'
    while time.time() < t_end2:
        c.write_tag([('trigger_bullet_fire',1,'BOOL')])
    c.write_tag([('trigger_bullet_fire',0,'BOOL'),('trigger_motor_on',0,'BOOL')])


def hideGun(t_end3):
    print 'Hide Gun'
    time.sleep(1)
    c.write_tag(('nerfgun_position_fire',1,'BOOL'))

def userInput(arg):
    if arg is 'quit':
        exit(0)
        sleep(1)

def parseMessage(message,fp):
    t_end = time.time() + 60 * .02
    t_end2 = time.time() + 60 * .058
    t_end3 = time.time() + 60 * .16

    if "longgun" in message: 
        motorFunc(t_end)
        fireBullets(t_end2)
        hideGun(t_end3)    
        while "longgun" in message:
            message = fp.readline()

#sections = message.split(";")
    #Quit = input('Press Q to Quit')

    #for section in sections:
      #  pair = section.split('=')

       # if(len(pair) == 2):
           # print(pair[0] + " " + pair[1])
        #   if pair[0] is 'obj'
	#	print pair[1] 
	#	if pair[1] is 'longgun'
            
	 #       motorFunc()
          #      fireBullets()
           #     hideGun()
            #    continue
        #elif Quit == 'Q': 
         #   print 'User quit program'
         #   c.write_tag([('nerfgun_position_fire',1,'BOOL'),('trigger_motor_on',0,'BOOL')])
         #  c.write_tag([('trigger_bullet_fire',0,'BOOL')])
         # break
        #else:
         #   continue
    #sys.exit(0)

#def handleCh(ch):
#    if(ch == '\n'):
#        parseMessage(sample_message)
#        sample_message = ""
#    else:
#        sample_message += ch

def handleInput(incomingMessage):
    for ch in incomingMessage:
        handleCh(ch)

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
                    parseMessage(line,fp)
                   # fp.close()
                except Exception as e:
                    c.close()
                    print e
                    pass

        # r_array = c.read_array("TotalCount", 1750)
        # for tag in r_array:
        #     print (tag)

        c.close()
