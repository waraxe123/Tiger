from TigerX import *
from TigerX.lib.cbn import make_carbon
from TigerX.lib.developer import shell_exec
import os
import asyncio

async def sysinfo(c, m):
    chat_id = m.chat.id
    install_system = os.system("apt-get install -y neofetch") if os else None
    if install_system:
         await install_system
    else:
         try:
             sysinfo = (await shell_exec("neofetch | sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g'"))[0]
             carbon = await make_carbon(sysinfo)
             await c.send_photo(chat_id, carbon, caption=f"Carbonised by {c.me.mention}")
         except Exception as e:
             await m.reply_text(str(e))
             return

async def send_photo_or_video(c, m):
    chat_id = m.chat.id
    link = (m.text.split(None, 1)[1] if len(m.command) != 1 else None)
    link_message = m.reply_to_message
    link_new = link_message.text
    if not link or not link_message:
        await m.reply_text("for example, this telegraph link can send mp4")
        return
    if link_new and link_new.endswith(".mp4"):
        send_func = c.send_video
        link_to_send = link_new
    elif link and link.endswith(".mp4"):
        send_func = c.send_video
        link_to_send = link
    else:
        send_func = c.send_photo
        link_to_send = link_new or link
    try:
        await send_func(chat_id, link_to_send)
    except Exception as e:
        await m.reply_text(str(e))
