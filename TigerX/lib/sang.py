import asyncio 
from pykillerx.helper.basic import *
from pykillerx.helper.hacking import *
from pykillerx.helper import *
from TigerX import *
from TigerX.lib import *

async def sangmata_check(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
        args = message.text
        try:
            user = await client.get_users(args)
        except Exception:
            await message.reply_text(f"`Please specify a valid user!`")
            return
    bot = "@SangMata_beta_bot"
    if user_id:
        await client.send_message(bot, f"/search_id {user_id}")
    elif user:
        await client.send_message(bot, f"/search_id {user}")
    else: 
        return 
    await asyncio.sleep(2)
    try:
        async for stalk in client.search_messages(bot, limit=1, timeout=5):
            if not stalk:
                await message.reply_text("**this person has never changed their name**")
                return
            elif stalk:
                await client.send_message(message.chat.id, stalk.text, reply_to_message_id=message.id)
                return
    except asyncio.TimeoutError:
        await message.reply_text("**Timed out while searching for messages**")

# end this
