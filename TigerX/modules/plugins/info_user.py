from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command(["whois", "info"], cmd) & owner)
async def who_is_command(client: Client, message: Message):
    await who_is(client, message)

@randydev(command(["chatinfo", "cinfo", "ginfo"], cmd) & owner)
async def chatinfo_handler_ok(client: Client, message: Message):
    await chatinfo_handler(client, message)


add_command_help(
    "info",
    [
        [
            "info <username/userid/reply>",
            "get telegram user info with full description.",
        ],
        [
            "chatinfo <username/chatid/reply>",
            "get group info with full description.",
        ],
    ],
)
