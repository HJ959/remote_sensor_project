##############################################################################
import serial
from time import sleep
from datetime import datetime
import re
import json
##############################################################################
if __name__ == '__main__':
    # b'Temp: 34, Moisture: 1023\r\n'
    re_temp = re.compile(r'Temp: (.+?),') # group 1
    re_moist = re.compile(r'Moisture: ([0-9]+)') # group 1

    ser = serial.Serial('/dev/ttyACM0', 9600)
    
    now = datetime.now()
    today = now.strftime('%d_%m_%Y_%H%M')

    for i in range(0, 100):
        sleep(0.01)
        if(ser.in_waiting >0):
            line = str(ser.readline())
   
    # clean up the text line
    temp = re.search(re_temp, line)
    moist = re.search(re_moist, line)

    io = {}
    if temp and moist:
        temp = temp.group(1)
        moist = moist.group(1)
        
        io[today] = {'Celsius': temp, 'Moisture_level': moist}
        output_json = str(json.dumps(io, sort_keys=True, indent=4))

    # write the data to a text file
    with open('sensor_data.txt', 'a') as f:
        f.write(output_json)

