from TigerX.lib import *
from TigerX import * 

async def take_corret(client, message):
    caption = message.text.split(None, 1)[1] if message else None
    replied = message.reply_to_message
    take_this = replied.copy(m.chat.id, caption=caption) if replied else None
    if not caption or not replied:
        await message.reply_text("please reply to a message")
    else:
        try:
            await take_this
        except Exception as e:
            await message.reply_text(str(e))
