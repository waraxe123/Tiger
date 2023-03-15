from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command("rmbg", cmd) & owner)
async def rmbg_command(c: Client, m: Message):
    await rmbg_background(c, m)
