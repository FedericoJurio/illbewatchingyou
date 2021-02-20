import os

import requests


class TelegramClient:
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    username = os.getenv('TELEGRAM_USERNAME')
    password = os.getenv('TELEGRAM_PASSWORD')
    url = f'https://api.telegram.org/{username}:{password}'

    def send_message(self, message):
        requests.post(self.url + f'/sendMessage?chat_id={self.chat_id}&text=' + message)
