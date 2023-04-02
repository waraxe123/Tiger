from TigerX import *
from TigerX.lib import *

from pykillerx.help import add_command_help

@randydev(command(["pat", "pats"], cmd) & owner)
async def pat_handler(c: Client, m: Message):
    await give_pats(c, m)

add_command_help(
    "pats",
    [
        [".pat | .pats", "Give pats."],
    ],
)
