# Unchi bot on LINE

## This is the Unchi bot using the API in different platforms written in Python3
1. you'll need the token from the API to use this.
	- get the token for LINE from:
		- https://notify-bot.line.me
			- insert the token to the variable <i>access_token</i> in the python file
	- get the token for Twitter from:
		https://developer.twitter.com/en/apps
			- import the unchibot.py
			- insert the 4 keys into the <i>Unchibot</i> class

2. move the unchibot.py file under <i>/opt</i>

3. insert the .service file under the directory <i>/etc/systemd/system</i>
	- activate with the command:
		- <i>sudo systemctl enable unchibot.service</i>
		- <i>sudo systemctl start unchibot.service</i>

## Updates
	- added the Twitter version of the Unchibot under Twitter directory[Feb 3, 2020]
