from TigerX import *
from TigerX.lib.cbn import make_carbon
from TigerX.lib.developer import shell_exec
import os

async def sysinfo(c, m):
    chat_id = m.chat.id
    pro = await m.reply_text("`Prossing....`")
    try:
        sysinfo = (await shell_exec("neofetch | sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g'"))[0]
    except Exception:
        await os.system("apt-get install -y neofetch")
        return
    carbon = await make_carbon(sysinfo)
    try:
        await c.send_photo(chat_id, carbon, caption=f"Carbonised by {c.me.mention}")
        await pro.delete()
    except Exception as e:
        await pro.edit_text(str(e))
        return 
