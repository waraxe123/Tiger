from TigerX import *
from TigerX.lib import *

@randydev(command("update", cmd) & owner)
async def update_handler_fixed(client: Client, message: Message):
    await upstream(client, message)

@randydev(command("goupdate", cmd) & owner)
async def update_handler(client: Client, message: Message):
    await updatees(client, message)
