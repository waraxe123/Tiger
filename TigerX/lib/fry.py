# Made by dot arc for Ultroid

from TigerX import *
from TigerX.lib import *
from time import sleep
from pyrogram import filters
import asyncio
from pyrogram.types import Message


async def frybot(client, message):
    reply = message.reply_to_message
    if not (reply and (reply.photo or reply.sticker)):
        await message.reply_text("`Reply to a photo/sticker`")
        return
    
    file_id = reply.photo.file_id if reply.photo else reply.sticker.file_id
    file_path = await client.download_media(file_id)
    CHAT = await client.resolve_peer("image_deepfrybot")
    if args := message.text.split(None, 1)[1]:
        args = args.lstrip()
    try:
        await client.send_message(CHAT, f"/deepfry {args}")
        await sleep(3)
        send = client.send_photo(CHAT, photo=file_path) or client.send_document(CHAT, file_path)
        if send:
            async for x in client.search_messages(CHAT, limit=1):
                file_id = x.photo.file_id
                send_param = await client.download_media(file_id)
                send_other = client.send_photo(message.chat.id, photo=send_param) or client.send_document(message.chat.id, send_param)
                if send_other:
                    await send_other
                    break
                else:
                    await client.send_message(message.chat.id, "Failed Error", reply_to_message_id=message.id)
        else:
            await client.send_message(message.chat.id, "Failed Error", reply_to_message_id=message.id)
    except Exception as e:
        await message.reply_text(f"Error request {e}")
