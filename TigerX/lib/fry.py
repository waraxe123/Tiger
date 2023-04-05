# Made by dot arc for Ultroid

from TigerX import *
from TigerX.lib import *
from time import sleep
from pyrogram import filters
import asyncio

from pyrogram.types import Message

def mediainfo(media: Message.media):
    if isinstance(media, Message.Photo):
        return "pic"
    elif isinstance(media, Message.Sticker):
        return "sticker"
    else:
        return None

async def frybot(client, message):
    reply = message.reply_to_message
    if not (reply and reply.media and mediainfo(reply.media) in ("pic", "sticker")):
        await message.reply_text("`Reply to a photo/sticker`")
        return

    eris = await message.reply_text("`frying...`")
    CHAT = await client.resolve_peer("image_deepfrybot")
    if args := message.text.split(None, 1)[1]:
        args = args.lstrip()
    try:
        async with client.conversation(CHAT, total_timeout=15) as conv:
            file = await conv.send_media(reply)
            if args and args.isdigit():
                await sleep(2)
                await conv.send_message(f"/deepfry {args}", reply_to_message_id=file.id)
            response = await conv.get_response()
            await asyncio.gather(
                reply.reply(file=response.media),
                eris.delete(),
                conv.mark_read(),
            )
    except UserIsBlocked:
        await eris.edit("`Sar, plox Unblock @image_deepfrybot`")
    except TimeoutError:
        await eris.edit("`Bot didn't respond in time..`")
    except Exception as exc:
        await eris.edit(f"**Error:** `{exc}`")
