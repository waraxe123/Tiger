import requests
from time import sleep
import asyncio
import os
import json
from pyrogram import filters
from pyrogram.types import Message
from . import *

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))

async def cas_check(c, m):
    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
        user_first_name = m.reply_to_message.from_user.first_name
    results = requests.get(f"https://api.cas.chat/check?user_id={user_id}").json()
    offenses_cas = results["result"]["offenses"]
    offense_msg = results["result"]["messages"]
    cas_ban_time = results["result"]["time_added"]
    try:
        text = (
            f"**User ID:** `{user_id}`\n"
            f"**Name:** `{user_first_name}`\n"
            f"**Offenses:** `{offenses_cas}`\n"
            f"**Messages:** `\n{offense_msg}`\n"
            f"**Time Added:** `{cas_ban_time}`"
        )
    except:
        text = "`Not banned in CAS`"
    await m.edit_text(text, parse_mode="markdown")
    return
