import logging
import os
import yaml

import requests
from celery import Celery

from telegram import TelegramClient


celery_broker_uri = os.getenv('CELERY_BROKER_URI')
app = Celery('tasks', broker=celery_broker_uri)

app.conf.beat_schedule = {
    'check-product-availability': {
        'task': 'task.check_product_availability',
        'schedule': 600.0
    }
}


def get_products():
    with open('products.yaml', 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as error:
            logging.error(error)


@app.task
def check_product_availability():
    logging.info('Checking product availability')
    products = get_products()
    for model, url in products.items():
        response = requests.get(url)

        if response.status_code == 200 and 'Publicación pausada' not in response.text:
            TelegramClient().send_message(f'{model}: Hay stock {url}')
