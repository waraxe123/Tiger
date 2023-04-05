from TigerX import *
from TigerX.lib import *

@randydev(command("ip", cmd) & owner)
async def location_hanlder(client: Client, message: Message):
    await hacker_lacak_target(client, message)
