#!/usr/bin/env python
# Dont forget to install gpiozero import and requests
#
# sudo pip install gpiozero
# sudo pip install import
# sudo pip install requests
#
# The crontab that I'am using are: 
# */5 * * * * sudo /home/pi/rpitemp.py >/dev/null 2>&1
#
#
from gpiozero import CPUTemperature
import requests

cpu = CPUTemperature()

payload1 = {'svalue': int(cpu.temperature)}
requests.get('http://192.168.1.101:8080/json.htm?type=command&param=udevice&idx=80', params=payload1)
