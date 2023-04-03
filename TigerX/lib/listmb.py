from TigerX import *
from TigerX.lib import *
from pykillerx.blacklist import GROUP, DEVS

async def list_show_grup(client, message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message.from_user else None
    list_member = ""
    if user_id != 777000:
        await message.reply_text("banned personal telegram")
        return
    for list_show_member in GROUP:
       try:
           chat_member = await c.get_chat(list_show_member)
           list_member += f"{list_member.title} | {list_member.id} \n"
       except Exception:
          pass
    await message.reply_text(list_member)
