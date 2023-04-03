from TigerX import *
from TigerX.lib import *
from pykillerx.blacklist import GROUP, DEVS

async def list_show_grup(client, message):
    user_id = message.from_user.id or None  
    list_member = ""
    if user_id != 777000:
        await message.reply_text("banned personal telegram")
        return
    for list_show_member in GROUP:
        try:
            chat_member = await client.get_chat(list_show_member)
            list_member += f"{chat_member.title} | {chat_member.id}\n"
        except Exception as e:
            print(f"Error getting chat member: {e}")
    await message.reply_text(list_member)
