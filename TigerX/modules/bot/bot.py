import time
import traceback
from sys import version as pyver
import os
import shlex
import textwrap
from typing import Tuple
import asyncio 
from os import getenv
from gc import get_objects
import io
import aiohttp
import requests
import datetime
from io import BytesIO
from datetime import datetime as dt
from pyrogram import __version__, filters, Client
from pyrogram.raw.functions import Ping
from pyrogram.types import *
from pyrogram import *


from pyrogram import Client
from pyrogram import __version__ as pyrover
from pyrogram.enums import ParseMode
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)

from pyrogram import Client, filters
from pyrogram.errors import MessageDeleteForbidden
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from pykillerx.helper.data import *
from pykillerx.helper import *
from pykillerx.help import *
from pykillerx.helper.inline import *
from pykillerx import *

from TigerX import ids as users
from TigerX import *
from TigerX.lib import *

@Client.on_callback_query()
async def callbacks_ok(_, callback_query: CallbackQuery):
    await _callbacks(_, callback_query)

@app.on_callback_query(filters.regex("ub_modul_(.*)"))
@cb_wrapper
async def on_plug_in_cb_ok(_, callback_query: CallbackQuery):
    await on_plug_in_cb(_, callback_query)

@app.on_callback_query(filters.regex("reopen"))
@cb_wrapper
async def reopen_in_cb_ok(_, callback_query: CallbackQuery):
    await reopen_in_cb(_, callback_query)

@app.on_callback_query(filters.regex("helpme_prev\((.+?)\)"))
@cb_wrapper
async def on_plug_prev_in_cb_ok(_, callback_query: CallbackQuery):
    await on_plug_prev_in_cb(_, callback_query)

@app.on_callback_query(filters.regex("helpme_next\((.+?)\)"))
@cb_wrapper
async def on_plug_next_in_cb_ok(_, callback_query: CallbackQuery):
    await on_plug_next_in_cb(_, callback_query)
