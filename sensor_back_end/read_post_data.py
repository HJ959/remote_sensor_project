import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

while True: 
    if(ser.in_waiting >0):
        line = ser.readline()
        line = str(line) + '/n'
        break

with open('sensor_data.txt', 'a') as f:
    f.write(line)

