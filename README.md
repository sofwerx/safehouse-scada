# SCADA - Nerf Gun System
This project uses an Allen-Bradley PLC to control the Automated Nerf Gun System that detects AK47 objects.
This is the SCADA Lane implementaion of the Mad Jack project at SOFWERX.

## Tools
* Rockwell Automation Software RSLogix 5000
* Pycomm library - connect to PLCs & r/w tags

## Files
* PLC to Elasticsearch Python App for sending logs to elastic search
* rw-tags-plc - Python App for controlling the PLC through reading and writing global tags
* RSLogix5000 Program Files
    * - Door and hallway sensors
    * - Nerfgun mechanism
    
