import requests
from time import sleep
import asyncio
import os
import json
from pyrogram import filters
from pyrogram.types import Message
from . import *

async def extract_user_peler(message: Message) -> (int, str):
    """extracts the user from a message"""
    user_id = None
    user_first_name = None

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        user_first_name = message.reply_to_message.from_user.first_name

    elif len(message.command) > 1:
        if len(message.entities) > 1:
            required_entity = message.entities[1]
            if required_entity.type == "text_mention":
                user_id = required_entity.user.id
                user_first_name = required_entity.user.first_name
            elif required_entity.type == "mention":
                user_id = message.text[
                    required_entity.offset : required_entity.offset
                    + required_entity.length
                ]
                user_first_name = user_id
        else:
            user_id = message.command[1]
            user_first_name = user_id

    else:
        user_id = message.from_user.id
        user_first_name = message.from_user.first_name

    return (user_id, user_first_name)


__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))

async def cas_check(c, m):
    user_id, user_first_name = extract_user_peler(m)
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
