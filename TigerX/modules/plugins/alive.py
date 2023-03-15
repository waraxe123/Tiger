from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command(["alive"], cmd) & owner)
async def alive_command(client: Client, message: Message):
    await alive(client, message)

@randydev(command("id", cmd) & owner)
async def get_id_command(bot: Client, message: Message):
    await get_id(bot, message)

add_command_help(
    "misc",
    [
        ["alive", "Check if the bot is alive or not."],
        ["id", "Send id of what you replied to."],
        ["restart", "You are retarded if you do not know what this does."],
    ],
)
