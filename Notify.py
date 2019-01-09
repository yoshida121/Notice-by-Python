import requests, sys

def notify(token, message):
    api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + token}
    requests.post(api, data=payload, headers=headers)


if __name__ == '__main__':
    notify()