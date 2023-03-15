from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command(["lock", "unlock"], cmd) & owner)
async def locks_cmd(client: Client, message: Message):
    await locks_all_or_unlock_all(client, message)

@randydev(command("locks", cmd) & owner)
async def locktypes_cmd(client: Client, message: Message):
    await locktypes(client, message)

add_command_help(
    "locks",
    [
        ["lock [all or specific]", "restrict user to send."],
        [
            "unlock [all or specific]",
            "Unrestrict\n\nSupported Locks / Unlocks:` `msg` | `media` | `stickers` | `polls` | `info`  | `invite` | `webprev` |`pin` | `all`.",
        ],
    ],
)
