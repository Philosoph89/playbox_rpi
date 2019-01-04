def getVideoPath(rfidInput):
# Change the numbers with your RFID card IDs and the associated paths
    switcher = {
        "2519628649": "/home/pi/Videos/Farben.mp4",
        "2521701945": "/home/pi/Videos/Bagger.mp4",
        "2520381353": "/home/pi/Videos/Dino.mp4",
        "2519844985": "/home/pi/Videos/FWM_Sam.mp4",
        "2521528537": "/home/pi/Videos/Bobo.mp4"
    }
	# Return the videopath for the RFID card ID 
	return switcher.get(rfidInput, "Kein passendes Video gefunden.")
	
# Set the rfid reader device; is this doesn't work --> check if there is another HID in /dev/ 	
def getHID():
    return '/dev/hidraw0'
	
def getBackgroundPath():
	return "/home/pi/Pictures/Main.jpg"