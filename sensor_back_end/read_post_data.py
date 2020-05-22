##############################################################################
import serial
from time import sleep
from datetime import date
import re
##############################################################################
if __name__ == '__main__':
    # b'Temp: 34, Moisture: 1023\r\n'
    re_temp = re.compile(r'Temp: (.+?),') # group 1
    re_moist = re.compile(r'Moisture: ([0-9]+)') # group 1

    ser = serial.Serial('/dev/ttyACM0', 9600)
    
    today = date.today()

    for i in range(0, 100):
        sleep(0.1)
        if(ser.in_waiting >0):
            line = str(ser.readline()) + '\n'
   
    # clean up the text line
    temp = re.search(re_temp, line)
    moist = re.search(re_moist, line)

    if temp and moist:
        temp = temp.group(1)
        moist = moist.group(1)

        output_json = '''
"{today}" : {
             "Celsius": "{temp}",
             "Moisture_Level": "{moist}"
            }
'''

    # write the data to a text file
    with open('sensor_data.txt', 'a') as f:
        f.write(output_json)

