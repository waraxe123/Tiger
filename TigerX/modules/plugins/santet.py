from TigerX import *
from TigerX.lib import *

@randydev(command("santet", cmd) & owner)
async def santet_lu_fix(client: Client, message: Message):
    await typewriter(client, message)

@randydev(command("whatsapp", cmd) & owner)
async def wa_lu_fix(client: Client, message: Message):
    await whatsapp_hack(client, message)
