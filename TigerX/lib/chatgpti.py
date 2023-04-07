# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# developer credits @xtsea

import requests
from io import BytesIO
import os
import json
import random
import asyncio
from pyrogram import *
from pyrogram.types import *

from TigerX import OPENAI_API

from TigerX import *
from TigerX.lib import *


# model text-davinci-003
# using rapidapi.com

async def new_model_chatgpt(client, message):
    ran = await message.reply_text("<code>Processing....</code>")
    APIKEY = "ce36c261f1mshb4a0a55aaca548ep12c9f3jsn3d6761cb63fb"
    asked = message.text.split(None, 1)[1] if len(message.command) != 1 else None
    if not asked:
        await ran.edit_text("question ask this chagpt")
        return
    url = "https://openai80.p.rapidapi.com/completions"
    payload = {"model": "text-davinci-003", "prompt": asked, "max_tokens": 7, "temperature": 0, "top_p": 1, "n": 1, "stream": False, "logprobs": None, "stop": None}
    headers = {"content-type": "application/json", f"X-RapidAPI-Key": APIKEY, "X-RapidAPI-Host": "openai80.p.rapidapi.com"}
    if not APIKEY:
        await ran.edit_text("Missing Api key: <code>rapidapi.com</code>")
        return
    if response.status_code == 200:
        data_model = response.json()
        try:
            text_davinci = data_model["choices"][0]["text"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        if text_davinci:
            await ran.edit(text_davinci)
        else:
            await ran.edit_text("Yahh, sorry i can't get your answer")
    else:
        await ran.edit_text("failed to api chatgpt")
    

# using original openai.com 

async def chatgpt_ask(c, m):
    question = (m.text.split(None, 1)[1] if len(m.command) != 1 else None)
    if not question:
       await m.reply(f"use command <code>.{m.command[0]} [question]</code> to ask questions using the API.")
       return
    if not OPENAI_API:
       await m.reply("missing api key : `OPENAI_API`")
       return
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {OPENAI_API}"}
    json_data = {"model": "text-davinci-003", "prompt": question, "max_tokens": 200, "temperature": 0}
    msg = await m.reply(f"Wait a moment looking for your answer..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception as e:
        await msg.edit_text(f"Yahh, sorry i can't get your answer: {e}")


# credits @xtsea

async def chatpgt_image_generator(c, m):
    A = "h"
    B = "t"
    C = "t"
    D = "p"
    E = "s"
    chatgpt_api_url = "api.openai.com"
    version = "v1"
    new_image = "images/generations"
    model = "image-alpha-001"
    new_link = A + B + C + D + E
    image_text = (m.text.split(None, 1)[1] if len(m.command) != 1 else None)
    if not image_text:
       await m.reply_text(f"example <code>+{m.command[0]} superhero<code> : to using the chatgpt api image")
       return
    if not OPENAI_API:
       await m.reply_text("Missing Api key: <code>OPENAI_API</code>")
       return
    headers={"Authorization": f"Bearer {OPENAI_API}"}
    json={"model": model, "prompt": image_text, "size": "1024x1024", "response_format": "url"}
    response = requests.post(f"{new_link}://{chatgpt_api_url}/{version}/{new_image}", headers=headers, json=json)
    try:
        image_url = response.json()['data'][0]['url']
    except Exception:
        pass
        return
    image_content = requests.get(image_url).content
    new_caption = f"Question: {image_text}"
    try:
        pro = await m.reply_text("<code>Uplading chatgpt image......</code>")
        await c.send_photo(m.chat.id, photo=BytesIO(image_content), caption=new_caption, reply_to_message_id=m.id)
    except Exception as e:
        await pro.edit_text(str(e))
    try:
        await pro.delete()
    except Exception:
        pass

# Credits @xtsea 
# DON'T REMOVE CREDITS THIS

# model gpt-3.5-turbo
# using rapidapi.com

async def new_chatgpt_turbo(client, message):
    ran = await message.reply_text("<code>Processing....</code>")
    APIKEY = "ce36c261f1mshb4a0a55aaca548ep12c9f3jsn3d6761cb63fb"
    ask_turbo = message.text.split(None, 1)[1] if len(message.command) != 1 else None
    if not ask_turbo:
        await ran.edit_text("for example the question asked this chatgpt")
        return
    if not APIKEY:
       await ran.edit_text("Missing Api key: rapidapi.com")
       return
    url = "https://openai80.p.rapidapi.com/chat/completions"
    payload = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": ask_turbo}]}
    headers = {"content-type": "application/json", f"X-RapidAPI-Key": APIKEY, "X-RapidAPI-Host": "openai80.p.rapidapi.com"}
    response = requests.request("POST", url, json=payload, headers=headers)
    if response.status_code == 200:
        data_turbo = response.json()
        try:
            message_text = data_turbo["choices"][0]["message"]["content"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        if message_text:
            await ran.edit_text(message_text)
        else:
            await ran.edit_text("Yahh, sorry i can't get your answer")
    else:
        await ran.edit_text("Failed to api chatgpt turbo")
