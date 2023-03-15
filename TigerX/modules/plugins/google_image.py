from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command("img", cmd) & owner)
async def generate_image_command(c: Client, m: Message):
    await generate_image(c, m)
