from TigerX import *
from TigerX.lib import *

@randydev(command("truth", cmd) & owner)
async def truth_command(c: Client, m: Message):
    await truth_string(c, m)

@randydev(command("dare", cmd) & owner)
async def dare_command(c: Client, m: Message):
    await dare_string(c, m)

