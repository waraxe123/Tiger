from TigerX import *
from TigerX.lib.slp import slap_template_fixed, slap_funny_lol_fixed
from TigerX.lib import *

@randydev(command("slap", cmd) & owner)
async def slap_english_command(c: Client, m: Message):
    await slap_template_fixed(c, m)


@randydev(command("slape", cmd) & owner)
async def slap_english_command_2(c: Client, m: Message):
    await slap_funny_lol_fixed(c, m)
