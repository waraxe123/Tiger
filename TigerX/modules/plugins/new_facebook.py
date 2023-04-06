from TigerX import *
from TigerX.lib import *

@randydev(command("fbdl", cmd) & owner)
async def facebook_handler(client: Client, message: Message):
    await facebook_downloader(client, message)
