import os
import datetime
from os import getenv
from pyrogram import Client
import pyromod
from pyromod import *
import asyncio
import logging
import sys
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Any, Dict
from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime as dt
from aiohttp import ClientSession
# from pytgcalls import GroupCallFactory
from config import *

StartTime = time.time()
START_TIME = dt.now()
CMD_HELP = {}
clients = []
ids = []

aiosession = ClientSession()

TEMP_SETTINGS: Dict[Any, Any] = {}
TEMP_SETTINGS["PM_COUNT"] = {}
TEMP_SETTINGS["PM_LAST_MSG"] = {}


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)

logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)

LOGS = logging.getLogger(__name__)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

if not BOT_TOKEN:
   print("PERINGATAN: BOT TOKEN TIDAK DITEMUKAN")

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="TigerX/modules/bot"),
    in_memory=True,
)

if STRING_SESSION1:
   print("Client1: Found.. Starting..")
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1, plugins=dict(root="TigerX/modules"))
   clients.append(client1)

if STRING_SESSION2:
   print("Client2: Found.. Starting..")
   client2 = Client(name="two", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION2, plugins=dict(root="TigerX/modules"))
   clients.append(client2)

if STRING_SESSION3:
   print("Client3: Found.. Starting..")
   client3 = Client(name="three", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION3, plugins=dict(root="TigerX/modules"))
   clients.append(client3)


# client = [client for client in[STRING_SESSION1, STRING_SESSION2, STRING_SESSION3]if client]
# for client in clients:
#    if not hasattr(client, "group_call"):
#        setattr(client, "group_call", GroupCallFactory(client).get_group_call())
