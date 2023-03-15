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

from config import RMBG_API
from pyrogram.types import *
from pyrogram import *
from base64 import b64decode as hack

from TigerX import *
from TigerX.lib import *

from pykillerx.helper.basic import *
from pykillerx.helper.tools import *
import os
import requests
import shutil

async def rmbg_background(c, m):
    api_key = RMBG_API
    photo_id = None
    if m.reply_to_message and m.reply_to_message.photo:
        photo_id = m.reply_to_message.photo.file_id
    if not photo_id:
       await m.reply("**please reply to photo messages**")
       return
    if not api_key:
       await m.reply("missing api key : `RMBG_API`")
       return
    temp_file = await c.download_media(photo_id)

    endpoint = "https://api.remove.bg/v1.0/removebg"
    payload = {"size": "auto"}

    with open(temp_file, "rb") as image_file:
        response = requests.post(endpoint, data=payload, headers={"X-Api-Key": api_key}, files={"image_file": image_file}, stream=True)

    with open("output.png", "wb") as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    await m.reply_document("output.png")
    try:
       clear_file = "ran.webp"
       clear_file2 = "output.png"
       os.system("cp *.png ran.webp")
       await c.send_sticker(m.chat.id, "ran.webp")
       os.remove(clear_file)
       os.remove(clear_file2)
    except BaseException:
        pass
