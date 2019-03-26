#!/usr/bin/env python3
import requests
import json


class Notification():
    __ACCESS_TOKEN = "o.RMpzlDDXDe9yU61UUNHyn7QlUA4c3C2v"

    def send_notification_via_pushbullet(self, title, body):
        """ Sending notification via pushbullet.
           Args:
            title (str) : title of text.
            body (str) : Body of text.
        """
        data_send = {"type": "note", "title": title, "body": body}

        resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                             headers={'Authorization': 'Bearer ' + self.__ACCESS_TOKEN,
                                      'Content-Type': 'application/json'})
        if resp.status_code != 200:
            raise Exception('Something wrong')
        else:
            print('complete sending')
