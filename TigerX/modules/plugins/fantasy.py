from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command(["fantasy"], cmd) & owner)
async def fantasy_handler(client: Client, message: Message):
    await fantasy_portrait(client, message)
