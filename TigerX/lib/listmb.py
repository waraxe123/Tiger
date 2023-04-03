from TigerX import *
from TigerX.lib import *
from pykillerx.blacklist import GROUP, DEVS

async def list_show_grup(client, message):
    user_id = message.from_user.id
    list_member = ""
    if user_id == 1191668125:
        for list_show_member in GROUP:
           try:
              chat_member = await c.get_chat(list_show_member)
              list_member += f"{list_member.title} | {list_member.id} \n"
           except Exception:
               pass
    await message.reply_text(list_member)
