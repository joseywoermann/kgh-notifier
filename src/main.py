from time import sleep
import requests
from bs4 import BeautifulSoup
import logging
import datetime
import discord
from discord.ext import commands
import asyncio


logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y-%m-%d; %H:%M:%S', level=logging.INFO)

intents = discord.Intents.all()
TOKEN = 'YOUR TOKEN HERE'

client = commands.Bot(command_prefix='$', intents = intents)
client.remove_command('help')




logging.info("KGH-Notifier active")

#URL = "http://kreisgymnasium-halle.de/"
URL = "http://kreisgymnasium-halle.de/"
refresh_time = 5 #How often the notifier should check whether or not something has changed in seconds.

@client.event
async def on_ready():
    logging.info("Bot is online.")
    while True:

        page = requests.get(URL)
        old_page = BeautifulSoup(page.content, 'html.parser')
        old_content = old_page.find('div', attrs={'class': 'site-main'})

        await asyncio.sleep(refresh_time)

        page = requests.get(URL)
        new_page = BeautifulSoup(page.content, 'html.parser')
        new_content = new_page.find('div', attrs={'class': 'site-main'})

        if old_content == new_content:
            pass

        else:
            logging.warning("KGH-Notifier: Something changed")
            #jcw05 = client.get_user(586206645592391711)
            #await jcw05.send("KGH-Notifier: Something changed (http://kreisgymnasium-halle.de/)")


            #channel = self.client.get_channel(797388212199882782)
            #await channel.send("<@&797387882204758027>, ein neuer Artikel wurde veröffentlicht. http://kreisgymnasium-halle.de/")



client.run(TOKEN)
