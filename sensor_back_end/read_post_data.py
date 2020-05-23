##############################################################################
import serial
from time import sleep
from datetime import datetime
import re
import json
import ast
import pygame
import pygame.camera
from pygame.locals import *
##############################################################################
if __name__ == '__main__':
    # b'Temp: 34, Moisture: 1023\r\n'
    re_temp = re.compile(r'Temp: (.+?),') # group 1
    re_moist = re.compile(r'Moisture: ([0-9]+)') # group 1

    ser = serial.Serial('/dev/ttyACM0', 9600)
    
    now = datetime.now()
    today = now.strftime('%d_%m_%Y_%H%M')

    for i in range(0, 100):
        sleep(0.02)
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
    
    with open('sensor_data.json', 'r') as f:
        json_read = json.loads(f.read())
        json_read.update(io)
        print(json_read)

    # remove the example key
    try:
        del json_read['example_json']
    except:
        print('Json file exists')

    # write the data to a text file
    with open('sensor_data.json', 'w') as f:
        json.dump(json_read, f, sort_keys=True, indent=4)

    
    pygame.init()
    pygame.camera.init()
    camlist = pygame.camera.list_cameras()
    if camlist:
        cam = pygame.camera.Camera(camlist[0],(640,480))
        cam.start()
        image = cam.get_image()
        pygame.image.save(image, "spy_cam_" + today  + ".jpg")

