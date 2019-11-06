import serial

with serial.Serial('COM3') as ser:
	while True:
		line = ser.readline()
		print(line)
