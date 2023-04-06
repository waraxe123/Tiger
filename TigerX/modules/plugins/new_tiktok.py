from TigerX import *
from TigerX.lib import *

from pykillerx.help import add_command_help

@randydev(command(["tt", "tiktok"], cmd) & owner)
async def tiktok_handler(client: Client, message: Message):
    await tiktok_downloader(client, message)
