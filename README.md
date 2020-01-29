# Unchi bot on LINE

## This is the Unchi bot for LINE using the LINE API written in Python3
1. you'll need the token from the LINE API to use this.
	- get the token from:
		- https://notify-bot.line.me
	- insert the token to the variable <i>access_token</i> in the python file

2. move the unchibot.py file under <i>/opt</i>

3. insert the .service file under the directory <i>/etc/systemd/system</i>
	- activate with the command:
		- <i>sudo systemctl enable unchibot.service</i>
		- <i>sudo systemctl start unchibot.service</i>
