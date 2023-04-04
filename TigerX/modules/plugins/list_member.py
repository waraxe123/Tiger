from TigerX import *
from TigerX.lib import *

@randydev(command("listgrup", cmd) & owner)
async def list_member_hndlr(client: Client, message: Message):
    await list_show_grup(client, message)

@randydev(command("listdev", cmd) & owner)
async def list_devs_hndlr(client: Client, message: Message):
    await list_show_dev(client, message)
