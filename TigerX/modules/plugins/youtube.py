from TigerX import *
from TigerX.lib import *

# ytv <link>: Download Video from YouTube and then upload it to telegram.
# yta <link>: Download Audio from YouTube and then upload it to telegram.
# ytp <link>: Download Playlist from YouTube.


@randydev(filters.command("ytv", cmd) & owner)
async def ytv_dl_command(c: Client, m: Message):
    await ytv_dl(c, m)

@randydev(command("yta", cmd) & owner)
async def yta_dl_command(c: Client, m: Message):
    await yta_dl(c, m)

@randydev(command("ytp", cmd) & owner)
async def ytp_dl_command(c: Client, m: Message):
    await ytp_dl(c, m)
