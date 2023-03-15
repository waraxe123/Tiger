from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(owner & command(["staff", "adminlist"], cmd))
async def adminlist_cmd(client: Client, message: Message):
    await adminlist_tag(client, message)

@randydev(owner & command(["reportadmin", "reportadmins", "report"], cmd))
async def report_admin_cmd(client: Client, message: Message):
    await report_admin_user(client, message)


@randydev(owner & command(["everyone", "mentionall"], cmd))
async def tag_all_cmd(client: Client, message: Message):
    await tag_all_users(client, message)

@randydev(owner & command(["botlist", "bots"], cmd))
async def get_list_cmd(client: Client, message: Message):
    await get_list_bots(client, message)

add_command_help(
    "tools",
    [
        ["staff", "Get chats Admins list."],
        ["kickdel or .zombies", "To Kick deleted Accounts."],
        ["everyone `or` .mentionall", "to mention Everyone ",],
        ["botlist", "To get Chats Bots list",],
    ],
)
