# Made by dot arc for Ultroid

from TigerX import *
from TigerX.lib import *
from time import sleep
from pyrogram import filters
import asyncio
from pyrogram.types import Message


async def frybot(client, message):
    reply = message.reply_to_message
    if not (reply and (reply.photo)):
        await message.reply_text("`Reply to a photo`")
        return
    
    file_id = reply.photo.file_id
    file_path = await client.download_media(file_id)
    CHAT = "image_deepfrybot"
    if args := message.text.split(None, 1)[1]:
        args = args.lstrip()
    try:
        get_reply = await client.send_message(CHAT, f"/deepfry {args}")
        await sleep(3)
        await client.send_photo(CHAT, photo=file_path, reply_to_message_id=get_reply.id)
        async for x in client.search_messages(CHAT, limit=1):
            if x.photo:
                send_param = await client.download_media(x)
                await client.send_photo(message.chat.id, photo=send_param)
            else:
                await client.send_message(message.chat.id, "Failed Error", reply_to_message_id=message.id)
    except Exception as e:
        await message.reply_text(f"Error request {e}")
