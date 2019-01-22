# coding: utf-8
# (C) 2019 yoshida121. All rights reserved.

import requests

class Notify():
    def __init__(self, token, token_path=None):
        if token_path is not None:
            with open(token_path) as token_file:
                token = token_file.read()
        self.token = token
        self.api = 'https://notify-api.line.me/api/notify'

    def notify(self, message):
        payload = {"message": message}
        headers = {'Authorization': 'Bearer ' + self.token}
        requests.post(self.api, data=payload, headers=headers)
