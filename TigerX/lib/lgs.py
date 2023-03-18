# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

import requests
from PIL import Image, ImageDraw, ImageFont
import glob
from random import choice 
from TigerX import *
from TigerX.lib import *

font_path = "/resources/fonts/Roboto-Bold.ttf" # this can replace other ttf : https://github.com/TeamKillerX/TigerX-Userbot/tree/test/resources/fonts
font_size = 60
font_color = (255, 255, 255)

URL_IMAGE = [
  "https://github.com/TeamkillerX/TigerX-Userbot/raw/test/resources/image/hd2.jpg",
  "https://github.com/TeamkillerX/TigerX-Userbot/raw/test/resources/image/images.jpeg",
  "https://github.com/TeamkillerX/TigerX-Userbot/raw/test/resources/image/peakpx.jpg",

]

async def logo_write(client, message):
    text = message.text.split(".logo_write ", 1)[1]
    response = requests.get(URL_IMAGE)
    img = Image.open(BytesIO(response.content))
    font = ImageFont.truetype(font_path, font_size)

    draw = ImageDraw.Draw(img)
    text_size = draw.textsize(text, font)
    text_position = ((img.width - text_size[0]) // 2, (img.height - text_size[1]) // 2)
    draw.text(text_position, text, font=font, fill=font_color)

    img.save("logo_with_text.png")
    await client.send_photo(chat_id=message.chat.id, photo="logo_with_text.png")
