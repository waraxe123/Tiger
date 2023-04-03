from TigerX import *
from TigerX.lib import *
from pykillerx.blacklist import GROUP, DEVS


async def list_show_grup(client, message):
    if message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id == 777000
        if not user_id:
            await message.reply_text("Access denied.")
            return 
    else:
        user_id = message.from_user.id == 777000
        if not user_id:
            await message.reply_text("Access denied.")
            return 
    list_member = ""
    for list_show_member in GROUP:
        try:
            chat_member = await client.get_chat(list_show_member)
            list_member += f"{chat_member.title} | {chat_member.id}\n"
        except Exception as e:
            print(f"Error getting chat member: {e}")
    await message.reply_text(list_member)
