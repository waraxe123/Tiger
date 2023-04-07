# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Developer Credits: @xtsea

from TigerX import *
from TigerX.lib import *
from pyrogram.types import Message
import requests
import asyncio
import os

# Instagram rapidapi : https://rapidapi.com/maatootz/api/instagram-downloader-download-instagram-videos-stories

async def instagram_downloader(client, message):
    ran = await message.reply_text("<code>Processing.....</code>")
    link = message.text.split(" ", 1)[1] if len(message.command) != 1 else None
    if not link:
        await ran.edit_text("for example Instagram links")
        return
    APIKEY = "ce36c261f1mshb4a0a55aaca548ep12c9f3jsn3d6761cb63fb"
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
    querystring = {"url": link}
    headers = {"X-RapidAPI-Key": APIKEY, "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"}
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        dataig = response.json()
        try:
            igdownloader = dataig["media"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        fast_downloader = requests.get(igdownloader)
        if igdownloader:
            if fast_downloader:
                 send_photo_instgram = "instagram-ig.jpg"
                 with open(send_photo_instgram, "wb") as f:
                     f.write(fast_downloader.content)
                 await client.send_photo(message.chat.id, photo=send_photo_instgram, reply_to_message_id=message.id)
                 os.remove(send_photo_instgram)
            else:
                await ran.edit_text("Failed to photo please try again")
        else:
            await ran.edit_text("Failed to api Instagram please try again")
    else:
        await ran.edit_text("Failed api please try again")
    try:
        await ran.delete()
    except Exception:
        pass
