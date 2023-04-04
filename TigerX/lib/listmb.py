# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#


from TigerX import *
from TigerX.lib import *
from pykillerx.blacklist import GROUP, DEVS

async def list_show_grup(client, message):
    ADMINS_TELEGRAM = [1191668125, 777000] # don't edit you get banned 
    user_id = message.from_user.id in ADMINS_TELEGRAM
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

async def list_show_dev(client, message):
    ADMINS_TELEGRAM = DEVS # don't edit you get banned 
    user_id = message.from_user.id in ADMINS_TELEGRAM
    if not user_id:
        await message.reply_text("Access denied.")
        return 
    list_devs = ""
    for list_show_devs in DEVS:
        try:
            from_user_dev = await client.get_chat(list_show_devs)
            list_devs += f"{from_user_dev.first_name} | {from_user_dev.id}\n"
        except Exception as e:
            print(f"Error getting from user devs: {e}")
    await message.reply_text(list_devs)
