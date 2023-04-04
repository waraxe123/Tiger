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
import os

# you can get this api key : https://api-ninjas.com/profile

API_NINJA_NEW = "Pyp4hM0TJqb+ZZUpRBUSTQ==B1VFKxPVKSWbCVRZ" # don't share this,

async def api_ninja_dogs(client, message):
    term_param = message.text.split(None, 1)[1] if len(message.command) > 1 else None
    if not term_param:
        await message.reply_text("Example: <code>+dog golden retriever</code>")
        return

    if not API_NINJA_NEW:
        await message.reply_text("Missing api key: <code>API_NINJA_DOG</code>")
        return

    search_image = term_param
    api_url = f"https://api.api-ninjas.com/v1/dogs?name={search_image}"

    headers = {"X-Api-Key": API_NINJA_NEW}
    
    response = requests.get(api_url, headers=headers).json()
    send_image_url = response[0]["image_link"]
    real_name = response[0]["name"]
    try:
        await client.send_photo(message.chat.id, photo=send_image_url, caption=real_name, reply_to_message_id=message.id)
    except Exception as e:
        await client.send_message(message.chat.id, f"No results found: {e}", reply_to_message_id=message.id)


async def api_ninja_detect(client, message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.reply_text("Please reply to a message with a photo.")
        return

    if not API_NINJA_NEW:
        await message.reply_text("Missing api key: <code>API_NINJA_DOG</code>")
        return

    file_id = message.reply_to_message.photo.file_id
    photo_path = await client.download_media(file_id)

    api_url = "https://api.api-ninjas.com/v1/facedetect"
    with open(photo_path, "rb") as f:
        files = {"image": f}
        headers = {"X-Api-Key": API_NINJA_NEW}

        response = requests.post(api_url, files=files, headers=headers)

        if response.status_code == 200:
            data = response.json()

            annotated_url = data["annotated_image_link"]

            await client.send_photo(
                message.chat.id,
                photo=annotated_url,
                reply_to_message_id=message.id
            )

        else:
            await message.reply_text(
                "Sorry, there was an error processing your request. Please try again later."
            )

    os.remove(photo_path)
