from TigerX import *
from TigerX.lib import *

@randydev(command("sysinfo", cmd) & owner)
async def sysinfo_command(c: Client, m: Message):
    await sysinfo(c, m)


@randydev(command("sendr", cmd) & owner)
async def send_other_link(c: Client, m: Message):
    await send_photo_or_video(c, m)
