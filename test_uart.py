import time
import serial

ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.SEVENBITS)
counter=0
while True: 
    ser.write(str(f'This is number {counter}').encode('ascii')) 
    time.sleep(1) 
    counter += 1
