import serial
import keyboard
import csv
import pandas as pd
#
# Note 1: This python script was designed to run with Python 3.
#
# Note 2: The script uses "pyserial" which must be installed.  If you have
#         previously installed the "serial" package, it must be uninstalled
#         first.
#
# Note 3: While this script is running you can not re-program the Arduino.
#         Before downloading a new Arduino sketch, you must exit this
#         script first.

#
# Set the name of the serial port.  Determine the name as follows:
#	1) From Arduino's "Tools" menu, select "Port"
#	2) It will show you which Port is used to connect to the Arduino
#
# For Windows computers, the name is formatted like: "COM6"
# For Apple computers, the name is formatted like: "/dev/tty.usbmodemfa141"
#
arduinoComPort = "COM7"

#
# Set the baud rate
# NOTE1: The baudRate for the sending and receiving programs must be the same!
# NOTE2: For faster communication, set the baudRate to 115200 below
#        and check that the arduino sketch you are using is updated as well.
#
baudRate = 9600

# open the serial port
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)
# initialize various lists
dataList = []
panAngle = []
tiltAngle = []
voltage = []
# main loop to read data from the Arduino, then display it#
while True:
  # ask for a line of data from the serial port, the ".decode()" converts the
  # data from an "array of bytes", to a string
  lineOfData = serialPort.readline().decode()
  # check if data was received
  if len(lineOfData) > 0:
    # split the data up by type and put it in its own list
    dataList = lineOfData.split( ) 
    if len(dataList) == 3:
      panAngle.append(dataList[0])
      tiltAngle.append(dataList[1])
      voltage.append(dataList[2])   

  # 20*25 points is the number of points for a full scan across the letter
  if len(panAngle) > 20*25:
    break  

# save the data in dataframe and export it
data_dict =  {'Pan Angle': panAngle, 'Tilt Angle': tiltAngle, 'Voltage': voltage}  
df = pd.DataFrame(data_dict)
df.to_csv('full_scan3.csv') 
