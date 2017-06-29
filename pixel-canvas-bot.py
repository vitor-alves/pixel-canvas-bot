import requests
import simplejson as json
import socket
import re
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from threading import Thread
import threading

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



# OPEN PIXELCANVAS IN BROWSER
def openBrowser():
	driver = webdriver.Firefox()
	driver.get('http://pixelcanvas.io/@0,0');
	time.sleep(20)
	#driver.quit()

#SEND PLACE PIXEL HTTP POST PACKETS
def placePixel():
	url = "http://pixelcanvas.io/api/pixel"
	data = {'x': '2186', 'y': '-129', 'color': '5', 'fingerprint': fingerprint, 'token': 'null'}
	headers = {'Content-type': 'application/json', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.8,pt;q=0.6', 'Connection': 'keep-alive', 'Host':'pixelcanvas.io', 'Origin':'http://pixelcanvas.io', 'Referer':'http://pixelcanvas.io/@-172,-484', 'Save-Data':'on', 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}
	print(data)
	r = requests.post(url, data=json.dumps(data), headers=headers)
	print(r.text + "\n")
	print(r.headers)
	print(json.dumps(data))
	threading.Timer(120.0, placePixel).start()

main()