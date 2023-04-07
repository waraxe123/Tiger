from TigerX import *
from TigerX.lib import *

@randydev(command("igdl", cmd) & owner)
async def instagram_handler(client: Client, message: Message):
    await instagram_downloader(client, message)
