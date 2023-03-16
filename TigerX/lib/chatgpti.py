import requests
import os
import json
import random
import asyncio
from pyrogram import *
from pyrogram.types import *

from TigerX import OPENAI_API

from TigerX import *
from TigerX.lib import *

async def chatgpt_ask(c, m):
    question = (
        m.text.split(None, 1)[1]
        if len(
            m.command,
        )
        != 1
        else None
    )
    if not question:
       await m.reply(f"use command <code>.{m.command[0]} [question]</code> to ask questions using the API.")
       return
    if not OPENAI_API:
       await m.reply("missing api key : `OPENAI_API`")
       return
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 200,
        "temperature": 0,
    }
    msg = await m.reply(f"Wait a moment looking for your answer..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception as e:
        await msg.edit_text(f"Yahh, sorry i can't get your answer: {e}")
