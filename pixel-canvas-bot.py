''' 
Pixel Canvas Bot
Copyright (C) 2017

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import requests
import simplejson as json
import socket
import re
import time
from selenium import webdriver
from threading import Thread
import threading
from urllib.request import urlopen

fingerprint = None

# MAIN
def main():
	print('Pixel Canvas Bot has started!')
	# Start sniffing packets in search of the fingerprint
	t = Thread(target=sniffFingerprintPacket)
	t.start()

	# Open pixelcanvas.io in the browser. This is necessary to get the fingerprint, since it comes from actually acessing the website.
	openBrowser()

# PACKET SNIFFER
#	Sniffs packets passing through the network and gets the fingerprint number when an HTTP packet
#	containing the "fingerprint" passes by.
def sniffFingerprintPacket():
	print('Searching for fingerprint... Do not close the browser.')
	s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
	global fingerprint
	while fingerprint is None:
		data=s.recvfrom(65565) 
		pattern = r"fingerprint=[^\s]+"
		fingerprint_regex = (re.search(pattern, str(data[0])))
		if(fingerprint_regex is not None):
			fingerprint = fingerprint_regex.group().split('=')[1]
			print('Got the fingerprint! You can now close the browser if you want.')
			print('Fingerprint is: ' + fingerprint)
			# Programatically place the pixels in the map
			placePixel()



# OPEN PIXELCANVAS IN BROWSER.
# Necessary to get the fingerprint
def openBrowser():
	driver = webdriver.Firefox()
	driver.get('http://pixelcanvas.io/@-200,-473');
	time.sleep(20)
	#driver.quit()

# GET PIXEL COORDINATES AND COLOR FROM SERVER
def getPixel():
    url = "https://vault.linksolutions.co/pixel"
    r = urlopen(url)
    data = r.read().decode("UTF-8")
    j = json.loads(data) 
    return j

#SEND PLACE PIXEL HTTP POST PACKETS
def placePixel():
        # Pixel info from server
        pixel = getPixel()
        x = str(pixel['p'][0])
        y = str(pixel['p'][1])
        color = str(pixel['p'][2])
        online_clients = str(pixel['online_clients'])
        # Send pixel
        url = "http://pixelcanvas.io/api/pixel"
        data = {'x': x, 'y': y, 'color': color, 'fingerprint': fingerprint, 'token': 'null'}
        headers = {'Content-type': 'application/json', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.8,pt;q=0.6', 'Connection': 'keep-alive', 'Host':'pixelcanvas.io', 'Origin':'http://pixelcanvas.io', 'Referer':'http://pixelcanvas.io/@-172,-484', 'Save-Data':'on', 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}
        # Response
        r = requests.post(url, data=json.dumps(data), headers=headers)
        j = json.loads(r.text)
        wait_seconds = j['waitSeconds']
        success = j['success']
        # Print infos
        if(success):
            print('\n'+'Pixel colored successfuly! Position: ('+x+','+y+')!')
        else:
            print('\n'+'Failed to color pixel... I will try again soon.')
        default_wait_seconds = 120.0
        if(wait_seconds is None):
            wait_seconds = default_wait_seconds
        print('Wait seconds: ' + str(wait_seconds))
        print(online_clients + ' peole are connected to the bot server.') 
        # Place next pixel after 'wait_seconds'
        threading.Timer(wait_seconds, placePixel).start()

main()
