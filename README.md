# pixel-canvas-bot
A bot that automatically places pixels in http://pixelcanvas.io

### Installation and usage

**1. python3 (skip if you already have it installed)**

sudo apt-get install python3

**2. Download and run the bot**

wget https://github.com/vitor-alves/pixel-canvas-bot/archive/master.zip

unzip master.zip

cd pixel-canvas-bot-master

sudo python3 pixel-canvas-bot.py

### How it works
The bot gets specific coordinates and colors for pixels from a backend server and then sends this information to pixelcanvas.io server. Other bots I have seen need interaction from the user to manually get the fingerprint from the browser, an identification string used by pixelcanvas, but this one does this automatically by sniffing the network traffic and parsing the fingerprint from HTTP packets sent by the user to pixelcanvas.io server (this is why it needs to be run with sudo).
