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

# you can get this api key : https://api-ninjas.com/profile

API_NINJA_DOG = "Pyp4hM0TJqb+ZZUpRBUSTQ==B1VFKxPVKSWbCVRZ" # don't share this,

async def api_ninja_dogs(client, message):
    pro = await message.reply_text("<code>Prossing.......</code>")
    term_param = message.text.split(None, 1)[1] if len(message.command) > 1 else None
    if not term_param:
        await message.reply_text("Example: <code>+dog golden retriever</code>")
        return

    if not API_NINJA_DOG:
        await message.reply_text("Missing api key: <code>API_NINJA_DOG</code>")
        return

    search_image = term_param
    api_url = f"https://api.api-ninjas.com/v1/dogs?name={search_image}"

    headers = {"X-Api-Key": API_NINJA_DOG}
    
    response = requests.get(api_url, headers=headers).json()
    send_image_url = response[0]["image_link"]
    real_name = response[0]["name"]
    try:
        this_ninja = await pro.edit("<code>Uploading ninja dog.....</code>")
        await client.send_photo(message.chat.id, photo=send_image_url, caption=real_name, reply_to_message_id=message.id)
    except Exception as e:
        await pro.edit_text(f"No results found: {e}")
    try:
        await this_ninja.delete()
    except Exception:
        pass
