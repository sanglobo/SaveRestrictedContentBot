#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 27885485
API_HASH = "7dd9974c713787410beae4a295cc1e2d"
BOT_TOKEN = "6557904620:AAEhekYh5px21WiKYOmtUnTJu03xmKJTAR8"
SESSION = "AQGMcpgAq36NjCxzIrEnw5pOjm3jun3YXwKLT_eg-n7Rsi_uWT1AEWz-YBML3ypwCe5LNvgoyfGDfgw4PimBLCobXoWVRSmBGQ_nY7mq_SIsCR0eVB8niftcTvrt06g_43UDaexgOJeRgrhiHs5fjyCsECtjlpVGrc3_qqsbHwpiEEq9Pelm7VYSSq_SoQPnNjcU9sM-IMamTcI_egTSk1HKGnK5PgjYq4CtcS6gTS8aLLxEn0xmnHUsd2dNsXDAkbKzMflFWaH5pxjdoS6nhXBFH8-PbUvGWNiJXCWndhAUvXLXAwFsFmL-VTM1e-jRum8UsmGAlR2N4V6SDtHCHFedpXMW5AAAAAFeCZoYAA"
FORCESUB = "udiasu"
AUTH = 5872654872

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
