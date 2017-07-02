# pixel-canvas-bot
A bot that atomatically places pixels in http://pixelcanvas.io

### Installation and usage
**1. Install Firefox and geckodriver**

sudo apt-get install firefox

wget https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz

tar -zxvf geckodriver-v0.17.0-linux64.tar.gz

sudo cp geckodriver /usr/local/bin/

sudo chmod +x /usr/local/bin/geckodriver

**2. Install pip and packages**

wget https://bootstrap.pypa.io/get-pip.py

sudo python3 get-pip.py

sudo python3 -m pip install requests  simplejson  selenium

**3. Download and run the bot**

wget https://github.com/vitor-alves/pixel-canvas-bot/archive/master.zip

unzip master.zip

cd pixel-canvas-bot-master

sudo python3 pixel-canvas-bot.py

### How it works
The bot gets specific coordinates and colors for pixels from a backend server and then sends this information to pixelcanvas.io server. Other bots I have seen need interaction from the user to manually get the fingerprint from the browser, an identification string used by pixelcanvas, but this one does this automatically by sniffing the local network traffic and parsing the fingerprint from HTTP packets sent by the user to pixelcanvas.io server (this is why it needs to be run with sudo).
