#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#           bh1750.py
#  Read data from a digital light sensor.
#
# Author : Matt Hawkins
# Date   : 15/04/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------
import smbus
import time
import os
# Define some constants from the datasheet

DEVICE     = 0x23 # Default device I2C address

POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value

# Start measurement at 4lx resolution. Time typically 16ms.
CONTINUOUS_LOW_RES_MODE = 0x13
# Start measurement at 1lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
# Start measurement at 0.5lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20
# Start measurement at 0.5lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_2 = 0x21
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_LOW_RES_MODE = 0x23

#bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number
  return ((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
  return convertToNumber(data)

def main():
    # while True:
    print
    "Light Level : " + str(readLight()) + " lx"
    #  time.sleep(0.5)
    # cu1 = 'curl -s -i -H "Accept: application/json" "http://192.168.1.141:8080/json.htm?type=command&param=udevice&idx=130&svalue='


cu1 = 'curl -s -i -H "Accept: application/json" "http://127.0.0.1:8080/json.htm?type=command&param=udevice&idx=21&svalue='
cu2 = str(readLight())
cu3 = '"'
cu = cu1 + cu2 + cu3
# retvalue = os.system('curl -s -i -H "Accept: application/json" "http://127.0.0.1:80/json.htm?type=command&param=udevice&idx=7&svalue=700"')
retvalue = os.system(cu)
print
retvalue
if __name__ == "__main__":
    main()
