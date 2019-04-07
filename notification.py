# it is to send to users notification using pushbullet API
import requests
import json
import config
from App_Logging import SenseHatApp_logging
oo = SenseHatApp_logging()
# Most of this code is taken from week three tute sheet that for learning purposes


class Notification():

    def send_notification_via_pushbullet(self, title, body):
        """ Sending notification via pushbullet.
           Args:
            title (str) : title of text.
            body (str) : Body of text.
        """
        data_send = {"type": "note", "title": title, "body": body}

        resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                             headers={'Authorization': 'Bearer ' + config.ACCESS_TOKEN,
                                      'Content-Type': 'application/json'})
        if resp.status_code != 200:
            oo.logger.error('Something wrong')
        else:
            oo.logger.error('Notification sending')
