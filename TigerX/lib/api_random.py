# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Developer Credits: @xtsea

import requests



async def api_ceo_dog(client, message):
    API_DOG = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(API_DOG)
    if response.status_code == 200:
        data_ceo = response.json()
        
        photo_dog_url = response[0]["message"]
        ran = await message.reply_text("<code>Uploading.......</code>")
        await client.send_photo(message.chat.id, photo=photo_dog_url, reply_to_message_id=message.id)
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
