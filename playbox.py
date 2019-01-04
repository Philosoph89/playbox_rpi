import time
import platform
import subprocess
import os
import sys
import signal
import csv
from subprocess import call
import rfidInputLib
import config

lastInput = "0000"
videoPID = 0000
imageMain = subprocess.Popen(["feh","--fullscreen",config.getBackgroundPath()])

def showVideo(rfidInput):
	global lastInput
	global videoPID

	if(rfidInput == lastInput):
			print "Video wird bereits gezeigt..."
			return
		
	if(config.getVideoPath(rfidInput) != "Kein passendes Video gefunden."):
		print "Kein passendes Video zur Karte gefunden."
		return
				
	lastInput = rfidInput
	
	if(videoPID!=0000):
		os.kill(videoPID, signal.SIGTERM)
	videoProcess = subprocess.Popen(["vlc", config.getVideoPath(rfidInput), "-f"])
	videoPID = videoProcess.pid		
			
def waitingForInput():
		inputString = rfidInputLib.readRfidInput()
		showVideo(inputString)

if __name__ == '__main__':
	try:
		while(1):
			waitingForInput()
		
	except IndexError:
		print "Ups, da lief was schief"
