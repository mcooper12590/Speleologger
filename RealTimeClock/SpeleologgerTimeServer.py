import serial, glob
from time import asctime, gmtime
from calendar import timegm
from os.path import exists

pick = 0

# List of USB to Serial Devices
# Mac only right now... replace with a function that detects OS
rawresult = glob.glob('/dev/tty.usb*')

# If there are more than one device select one, if not the only
# avaliable device is selected.

if(len(rawresult) < 1):
	print "Check connections to Speleologger."
	exit(0)

if(len(rawresult) > 1):
	i=0
	for ser in rawresult:
		i+=1
		print str(i) + ": " + str(ser)

	choice = 0
	print "More than one USB to Serial device found!"

	while not choice:
		try: pick = int(input("Choose which device to use [1/2/..]: "))
		except KeyboardInterrupt:
			print ""
			exit(0)
		except: print "Input not a valid choice!."

		if pick > len(rawresult) or pick <= 0:
			print str(pick), "is not a valid choice!"
		else: choice = 1

	print "Picked " + str(rawresult[pick-1]) + "."

device = str(rawresult[pick-1])

# Connect to device
try: ser = serial.Serial(device)
except EnvironmentError:
	print "Error occured. Is Speleologger connected?"
	exit(0)

# Set time once a minute, check time every ten seconds
with ser:
	i=0
	try:
		while(True):
			if not exists(device):
				print "Device disconnected?"
				exit(0)

			if (i%6==0):
				utc = timegm(gmtime())
				st = "W" + str(utc)
				ser.write(st.encode())
				suc = ser.read()
				if (suc == "!"): print "Time set to", asctime(gmtime(utc)) 

			else:
				st = "R"
				ser.write(st.encode())
				cur = ser.read(10)
				utc = gmtime(float(cur))
				utc_str = asctime(utc)
				print "RTC time:", str(utc_str)
			i+=1
			time.sleep(10)

	except KeyboardInterrupt:
		print "\nShutting down time server."
		pass

