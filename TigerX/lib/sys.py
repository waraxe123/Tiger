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
