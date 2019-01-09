import requests

class Notify():
    def __init__(self, token):
        self.token = token
        self.api = 'https://notify-api.line.me/api/notify'

    def notify(self, message):
        payload = {"message": message}
        headers = {'Authorization': 'Bearer ' + self.token}
        requests.post(self.api, data=payload, headers=headers)