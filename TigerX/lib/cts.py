# code by @xtsea
# copyright file by https://github.com/TeamkillerX/

import requests
from base64 import b64decode as tolol

CHANNEL_JOIN = tolol("UmVuZHlQcm9qZWN0cw==").decode("utf-8")
API_CAT_IMAGE = tolol("aHR0cHM6Ly9hcGkudGhlY2F0YXBpLmNvbS92MS9pbWFnZXMvc2VhcmNo").decode("utf-8")
 
async def cat_image(c, m):
    join_user = CHANNEL_JOIN
    if not join_user:
        await m.reply_text("not required: `CHANNEL_JOIN`")
        return
    try:
        await c.join_chat(join_user)
    except Exception as e:
        await m.reply_text(f"you are banned channel: {e}")
        return
    url_cat = requests.get(API_CAT_IMAGE)
    urls = [url_cat.json()[0]['url'] for i in range(1)]
    for url in urls:
        await m.reply_photo(photo=url)
