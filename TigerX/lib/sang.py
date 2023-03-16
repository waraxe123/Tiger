import asyncio 
from pykillerx.helper.basic import *
from pykillerx.helper.hacking import *
from pykillerx.helper import *
from TigerX import *
from TigerX.lib import *

async def sangmata_check(client, message):
    args = await extract_user(message)
    lol = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            return await lol.edit(f"`Please specify a valid user!`")
    bot = "@SangMata_beta_bot"
    await client.send_message(bot, f"/search_id {user.id}")
    await asyncio.sleep(1)
    async for stalk in client.search_messages(bot, limit=2):
        if not stalk:
            await message.edit_text("**this person has never changed his name**")
            return
        elif stalk:
            await message.edit(stalk.text)
            await stalk.delete()
            await lol.delete()
