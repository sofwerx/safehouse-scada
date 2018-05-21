# SCADA - Nerf Gun System
Using a PLC, a camera, and an AI computer trained with an AK-47 detection program, this project deploys a Sentry Nerf Gun and fires bullets upon positive object detection.
See the [wiki](https://github.com/sofwerx/safehouse-scada/wiki) for all the details on this SCADA implementaion of the Mad Jack project.

## The Prereqs
Assuming you've configured the system detailed on the [wiki](https://github.com/sofwerx/safehouse-scada/wiki) page:
* YOLO requires that you install [darknet](https://pjreddie.com/darknet/install/)
* The python program needs to speak to the PLC, so [install the pycomm library](https://github.com/ruscito/pycomm)

## The Files
* pyconnector.py - Python program that connects all pieces together
* yolov2 - AK-47 Trained Program
* RSLogix - Simple files to program the PLC

## To Run The Programs
* Start the Python program first. Open a new terminal and type below:
```cd safehouse-scada 
python pyconnector.py
```
* To start the YOLO program, open a second terminal and type below:
```cd safehouse-scada/yolov2/
ak47-detector
```

## Thanks
A special thanks to the one and only [bytemaster-0xff](https://github.com/bytemaster-0xff) for all the help in the project. Thanks in advance for any feedback as well.
