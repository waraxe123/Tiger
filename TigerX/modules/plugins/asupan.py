# DON'T REMOVE CREDITS

# code by @pySmartDL
# Create by @xtsea

from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command(["asupan"], cmd) & owner)
async def asupan_command(client: Client, message: Message):
    await asupan_channel(client, message)
    
@randydev(command("ayang", cmd) & owner)
async def ayang_command(client: Client, message: Message):
    await ayang_channel(client, message)

@randydev(command("ppcp", cmd) & owner)
async def ppcp_command(client: Client, message: Message):
    await ppcp_channel(client, message)

@randydev(command("ppanime", cmd) & owner)
async def ppanime_command(client: Client, message: Message):
    await ppanime_channel(client, message)

add_command_help(
    "asupan",
    [
        ["asupan", "to send random asupan videos."],
        ["bokep", "to send random porno videos."],
        ["ayang", "Mencari Foto ayang kamu /nNote: Modul ini buat cwo yang jomblo."],
        ["ppcp", "Mencari Foto PP Couple Random."],
        ["ppanime", "Mencari Foto PP Couple Anime."],
    ],
)
