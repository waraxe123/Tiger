import asyncio 
from pykillerx.helper.basic import *
from pykillerx.helper.hacking import *
from pykillerx.helper import *
from TigerX import *
from TigerX.lib import *

async def sangmata_check(client, message):
    args = await extract_user(message)
    lol = await message.reply_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await message.reply_text(f"`Please specify a valid user!`")
            return
    bot = "@SangMata_beta_bot"
    await client.send_message(bot, f"/search_id {user.id}")
    await asyncio.sleep(2)
    async for stalk in client.search_messages(bot, limit=0):
        if not stalk:
            await message.reply_text("**this person has never changed his name**")
            return
        elif stalk:
            await client.send_message(m.chat.id, stalk.text, reply_to_message_id=message.id)
    await lol.delete()
