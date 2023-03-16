from TigerX import *
from TigerX.lib import *

@randydev(command(["sg", "sangmata"], cmd) & owner)
async def sangmata_command(client: Client, message: Message):
    await sangmata_check(client, message)
