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
import requests

async def facebook_downloader(client, message):
    ran = await message.reply_text("<code>Processing.....</code>")
    link = message.text.split(" ", 1)[1] if len(message.command) != 1 else None
    if not link:
        await ran.edit_text("Please provide a valid video link from Facebook.")
        return

    url = "https://facebook-video-and-reel-downloader.p.rapidapi.com/"
    querystring = {"url": link}

    headers = {"X-RapidAPI-Key": "ce36c261f1mshb4a0a55aaca548ep12c9f3jsn3d6761cb63fb", "X-RapidAPI-Host": "facebook-video-and-reel-downloader.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        data_facebook = response.json()
        try:
            facebook_hd = data_facebook["sd"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return

        facebook_url = requests.get(facebook_hd)
        if facebook_hd:
            if facebook_url:
                send_video_path = "tigerx_userbot.mp4"
                with open(send_video_path, "wb") as f:
                    f.write(facebook_url.content)
                await client.send_video(message.chat.id, video=send_video_path, reply_to_message_id=message.id)
                os.remove(send_video_path)   
            else:
                await ran.edit_text("Error please try again")
        else:
            await ran.edit_text("Error please try again facebook")
    else:
        await ran.edit_text(f"Failed to api facebook")
    try:
        await ran.delete()
    except Exception:
        pass
