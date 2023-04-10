# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# COPYRIGHT https://github.com/TeamKillerX/DarkWeb
# CREATE CODING BY https://t.me/xtsea


import os
import asyncio
import cv2
import numpy as np
import requests
from io import BytesIO
from PIL import Image 
from pyrogram.types import *
from pyrogram import *

from TigerX import *
from TigerX.lib import *

from TigerX import DEEPAI_API

async def toonify(c, m):
    pro = await m.reply_text("`Whacking face cartoon.......`")
    file_id = None
    if m.reply_to_message and m.reply_to_message.photo:
       file_id = m.reply_to_message.photo.file_id
    if not file_id:
       await pro.edit("Please reply to a photo to convert to cartoon or comic style.")
       return
    if not DEEPAI_API:
       await pro.edit("missing api key: `DEEPAI_API`")
       return
    file_path = await c.download_media(file_id)
   
    with open(file_path, 'rb') as f:
        response = requests.post(
            "https://api.deepai.org/api/toonify",
            files={'image': f},
            headers={'api-key': DEEPAI_API}
        )
    result = response.json()
    if 'output_url' in result:
        await c.send_photo(m.chat.id, result['output_url'])
        await pro.delete()
    else:
        await pro.edit("Failed to toonify the image.")
    try:
        os.remove(file_path)
    except Exception:
        pass


async def fantasy_portrait(client, message):
    ran = await message.reply_text("<code>Processing.....</code>")
    search_text = message.text.split(" ", 1)[1] if len(message.command) > 1 else None
    if not search_text:
        await ran.edit_text("Example : <code>+fantasy god of war</code>")
        return
    headers = {"api_key": "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"}
    data_string = {"text": search_text}
    r = requests.post("https://api.deepai.org/api/fantasy-portrait-generator", data=data_string, headers=headers).json()
    if "output_url" in r:
         await client.send_photo(message.chat.id, r["output_url"])
         await ran.delete()
    else:
        await ran.edit_text("Failed to fantasy portrait the image.")
