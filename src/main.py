from time import sleep
import requests
from bs4 import BeautifulSoup
import logging
import datetime



print("notifier active")

URL = "http://kreisgymnasium-halle.de/"
refresh_time = 60

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d; %H:%M:%S')


while True:

    page = requests.get(URL)
    old_page = BeautifulSoup(page.content, 'html.parser')
    old_content = old_page.find('div', attrs={'class': 'site-main'})

    sleep(refresh_time)

    page = requests.get(URL)
    new_page = BeautifulSoup(page.content, 'html.parser')
    new_content = new_page.find('div', attrs={'class': 'site-main'})

    if old_content == new_content:
        logging.warning(": nothing changed")
    else:
        logging.warning(": something changed")
