from TigerX import *
from TigerX.lib.slp import truth_string_str, dare_string_str_2
from TigerX.lib import *

@randydev(command("truth", cmd) & owner)
async def truth_command(c: Client, m: Message):
    await truth_string_str(c, m)

@randydev(command("dare", cmd) & owner)
async def dare_command(c: Client, m: Message):
    await dare_string_str_2(c, m)

