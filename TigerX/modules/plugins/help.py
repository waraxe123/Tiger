from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command(["help", "helpme"], cmd) & owner)
async def module_help_cmd(client: Client, message: Message):
    await module_help(client, message)

@randydev(command(["plugins"], cmd) & owner)
async def module_helper_cmd(client: Client, message: Message):
    await module_helper(client, message)
