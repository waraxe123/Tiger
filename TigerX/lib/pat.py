from TigerX import *
from TigerX.lib import *
import requests
import asyncio
import aiohttp

async def give_pats(c, m):
    URL = "https://some-random-api.ml/animu/pat"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no Pats for you :c")
            result = await request.json()
            url = result.get("link", None)
            await asyncio.gather(
                m.delete(),
                c.send_video(
                    m.chat.id, url, reply_to_message_id=m.id
                ),
            )
