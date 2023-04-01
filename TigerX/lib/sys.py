from TigerX import *
from TigerX.lib.cbn import make_carbon
from TigerX.lib.developer import shell_exec
import os
import asyncio

async def sysinfo(c, m):
    chat_id = m.chat.id
    pro = await m.reply_text("`Prossing....`")
    sleep_seconds = asyncio.sleep(5) if asyncio.sleep(2) else None
    install_system = os.system("apt-get install -y neofetch") if os else None
    try:
        await install_system
        await sleep_seconds
        sysinfo = (await shell_exec("neofetch | sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g'"))[0]
    except Exception:
        pass
        return
    carbon = await make_carbon(sysinfo)
    try:
        await c.send_photo(chat_id, carbon, caption=f"Carbonised by {c.me.mention}")
        await pro.delete()
    except Exception as e:
        await pro.edit_text(str(e))
        return 
