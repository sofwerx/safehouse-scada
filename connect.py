from pycomm.ab_comm.clx import Driver as ClxDriver
import logging

from time import sleep

if __name__ == '__main__':

    logging.basicConfig(
        filename="ClxDriver.log",
        format= "%(levelname)s %(asctime)s",
        # format="%(levelname)s %(asctime)s %(message)s %(filename)s",
        level=logging.DEBUG
    )
    c = ClxDriver()

    print (c['port'])
    print (c.__version__)


    if c.open('192.168.0.203'):
        while 1:
            try:
                print(c.read_tag(['TESTTAG']))

                print(c.write_tag('TESTTAG', 30, 'DINT'))
            
                sleep(1)
            except Exception as e:
                c.close()
                print (e)
                pass

        c.close()
