# Created By @xtsea

from pyrogram import *
from pyrogram import Client as ren
from pyrogram.types import *
import os 
from os import getenv
from config import PREFIXES

handler = ["^"]

cmd = handler

if handler:
    cmd = ["!", "+"]
elif PREFIXES:
    cmd = [f"{PREFIXES}"]
else:
    cmd = None

command = filters.command
regex = filters.regex 
owner = filters.me
private = filters.private
randydev = ren.on_message
randydev_edited = ren.on_edited_message
