from bs4 import BeautifulSoup
import requests
import os
import asyncio
from telegram import Bot



os.system("clear")

logo = """
  ____ _              _    
 |  _ \ | ___   ___ | | __
 | | | |/ _ \ / _ \| |/ /
 | |_| | (_) | (_) |   < 
 |____/ \___/ \___/|_|\_\\
 
                           
"""

print(logo)


while True:
	url = 'https://dolarhoje.com/'

	response = requests.get(url)

	soup = BeautifulSoup(response.content, "html.parser")

	element_estrangeiro = soup.find(id="estrangeiro")

	value_do_elemento = element_estrangeiro.get("value")

	element_nacional = soup.find(id="nacional")

	value_nacional = element_nacional.get("value")

	print(f"US${value_do_elemento} = R${value_nacional}")



	bot_token = '6058434875:AAEQjig2ynddrD2VyXNuUXRghv_4R_8fdp8'
	chat_id = -1001897186254  # Substitua pelo ID do seu canal

	async def send_telegram_message(bot_token, chat_id, message):
	    bot = Bot(token=bot_token)
	    await bot.send_message(chat_id=chat_id, text=message)

	asyncio.run(send_telegram_message(bot_token, chat_id, f"US${value_do_elemento} = R${value_nacional}"))
