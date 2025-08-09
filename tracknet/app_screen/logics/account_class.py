import requests


class login:
    result = ''
    authorize = False

    def __init__(self, username, password):
        self.url = 'http://127.0.0.1:5000/api/accounts/login/'
        self.username = username
        self.password = password

    def authorization(self):
        data = {'username': self.username, 'password': self.password}
        rsp = requests.post(self.url, data)
        self.result = rsp.text
        if rsp.status_code == 200:
            self.authorize = True
        else:
            self.authorize = False
        return self.authorize
