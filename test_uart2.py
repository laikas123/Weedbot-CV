#import serial
#ser = serial.Serial ("/dev/ttys0")    #Open named port 
#ser.baudrate = 9600                     #Set baud rate to 9600
#ser.write("B")
#data = ser.read(1)                     #Read ten characters from serial port to data
#print(data)                         #Send back the received data
#ser.close() 

import serial
ser = serial.Serial("/dev/ttyS0", baudrate=115200,stopbits=serial.STOPBITS_ONE, timeout=1)
ser.baudrate = 115200                     #Set baud rate to 9600
while True:
#    ser.write(str.encode('t'))
    data = ser.read(1)                     #Read ten characters from serial port t>
    print(data)                         #Send back the received data
#    print(type(data))
ser.close()
