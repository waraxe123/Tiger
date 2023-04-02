from TigerX.lib import *
from TigerX import * 

async def take_corret(client, message):
    caption = (message.text.split(None, 1)[1] if len(message.command) != 1 else None)
    replied = message.reply_to_message
    take_this = replied.copy(message.chat.id, caption=caption) if replied else None
    if not caption or not replied:
        await message.reply_text("please reply to a message")
        return
    try:
        await take_this
    except Exception as e:
        await message.reply_text(str(e))
        return
