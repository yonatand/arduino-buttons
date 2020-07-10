from pynput.keyboard import Key, Controller
import serial
import serial.tools.list_ports

keyboard = Controller()

ports = list(serial.tools.list_ports.comports())
matching = [s for s in ports if "Arduino Uno" in str(s)]

ardCom = str(matching[0]).split(' ', 1 )[0]
ser = serial.Serial(ardCom)
ser.flushInput()

print("connected to " + str(matching[0]), flush=True)

keyhold = 0

while True:
	try:
		ser_bytes = ser.readline()
		decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
		if decoded_bytes == 1 and keyhold != 1:
			keyboard.press(Key.f13)
			keyboard.release(Key.f13)
			keyhold = 1
		elif decoded_bytes == 2 and keyhold != 2:
			keyboard.press(Key.f14)
			keyboard.release(Key.f14)
			keyhold = 2
		elif decoded_bytes == 3 and keyhold != 3:
			keyboard.press(Key.f15)
			keyboard.release(Key.f15)
			keyhold = 3
		elif decoded_bytes == 4 and keyhold != 4:
			keyhold = 2
			keyboard.press(Key.f16)
			keyboard.release(Key.f16)
		elif decoded_bytes == 0:
			keyhold = 0
	except:
		print("Program stopped!")
		break