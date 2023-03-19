from TigerX import *
from TigerX.lib import *

@randydev(command("cat", cmd) & owner)
async def cat_image_fixed(c: Client, m: Message):
    await cat_image(c, m)
