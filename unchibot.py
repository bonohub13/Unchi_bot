#!/usr/bin/env python3

import requests
import time

class HelloLINE:
    def __init__(self, accessToken):
        self.url = 'https://notify-api.line.me/api/notify'
        self.headers = {'Authorization': 'Bearer '+accessToken}

    def send(self, message, image=None,
                            sticker_pkg_id=None,
                            sticker_id=None):
        payload = {'message': message,
                   'stickerPackageId': sticker_pkg_id,
                   'stickerId': sticker_id}
        files = {}
        if image != None:
            files = {'imgFile': open(image, 'rb')}

        request = requests.post(self.url, headers=self.headers,
                                          data=payload,
                                          files=files)

if __name__ == '__main__':
    access_token = 'insert token here'
    bot = HelloLINE(access_token)

    # default data
    past_time = time.ctime().split(' ')
    past_time[3] = past_time[3].split(':')
    
    while True:
        # catches current time in string data and formats it into list
        data = time.ctime()
        data_list = data.split(' ')
        data_list[3] = data_list[3].split(':')

        # debug
        # print(data)
        if int(data_list[3][0]) % 6 == 0 and past_time[3][0] != data_list[3][0]:
            message = 'うんちぶりぶり💩ﾃﾞ~ﾀﾖ~!\nFrom Python3 using LINE API: {}'.format(data)
            bot.send(message)
            past_time = data_list
