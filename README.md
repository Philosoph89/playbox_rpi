# playbox-rpi
Code for the playbox-rpi project. Project is at early stage so the repository is updated frequently.

This project aims to give kids a simple, self-determined but controllable access to their favorite videos.

# Hardware
- Raspberry Pi 3 B+
- Waveshare 7inch LCD for Pi
- RFID Reader 13,56 MHz (for Mifare S50,S70 cards)
- Power adapter with 5,1V/2,5A

# Software
- Raspbian OS
- VLC
- FEH
- Python

# Usage
- Install FEH, VLC and Python to your RPi (if this wasn't done before)
  - "sudo apt-get install feh"
  - "sudo apt-get install vlc"
  - "sudo apt-get install python"
- Copy this repository to your RPi (e.g. /home/pi/Playbox)
- Copy the videos you want to show at the playbox to your RPi
- Configure the map.py to your needs (RFID card IDs, video mapping, input device, ...) and save
  - "sudo nano /home/pi/Playbox/map.py"
- Change location to the Playbox path
- Run the playbox.py script to start the application
