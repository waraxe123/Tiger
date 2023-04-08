from TigerX import *
from TigerX.lib import *

from pykillerx.help import add_command_help

@randydev(command(["tt", "tiktok"], cmd) & owner)
async def tiktok_handler(client: Client, message: Message):
    await tiktok_downloader(client, message)

@randydev(command(["tt2", "tiktok2"], cmd) & owner)
async def tiktok_handler2(client: Client, message: Message):
    await tiktok_downloader_2(client, message)
