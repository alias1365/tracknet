import requests
import json
import ast


class api_server:
    URL_BASE = 'https://tracknet.alias65.ir/'
    URL_LOGIN = 'api/accounts/login/'
    URL_CURRENT_USER_INFO = 'sa/api/current/user/info'
    URL_MISSSION_LIST = 'sa/api/mission/list'
    URL_MISSSION_POINT_INSERT = 'sa/api/mission/insert'
    TOKEN = None
    LAST_ERROR = ""
    session = None

    def __init__(self):
        self.session = requests.Session()

    def mUrl(self,url):
        return f"{self.URL_BASE}{url}"


    def login_run(self,username, password):
        data = {
            "username": username,
            "password": password,
        }
        rsp = self.session.post(self.mUrl(self.URL_LOGIN), json=data)
        if rsp.status_code == 200:
            self.TOKEN = json.loads(rsp.text)['key']
            return True
        else:
            self.LAST_ERROR = rsp.text
            return False

    def mession_list_run(self):
        rsp = self.session.get(f"{self.URL_BASE}{self.URL_MISSSION_LIST}")
        if rsp.status_code != 200:
            self.LAST_ERROR=rsp.text
        mission_list = json.loads(rsp.text)
        return mission_list

    def mission_point_insert_run(self,mission_id=None):
        if mission_id is None:
            self.LAST_ERROR = "There is no mission defined!"
            return False
        data = {
            "mission": mission_id,
            "lat": 12.5,
            "lon": 15.89,
        }
        csrftoken = self.session.cookies['csrftoken']
        headers = {
            'X-CSRFToken': csrftoken,
            'Referer': self.URL_BASE,
        }
        rsp = self.session.post(f"{self.URL_BASE}{self.URL_MISSSION_POINT_INSERT}", json=data, headers=headers)
        if rsp.status_code == 201:
            return True
        else:
            self.LAST_ERROR = rsp.text
            return False

