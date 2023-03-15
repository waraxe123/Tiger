from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command("restart", cmd) & owner)
async def restart_bot_command(_, message: Message):
    await restart_bot(_, message)

add_command_help(
    "system",
    [
        ["restart", "to restart userbot."],
    ],
)
