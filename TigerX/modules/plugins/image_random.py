from TigerX import *
from TigerX.lib import *

@randydev(command("cat", cmd) & owner)
async def cat_image_fixed(client: Client, message: Message):
    await api_big_cat(client, message)

@randydev(command("dog2", cmd) & owner)
async def image_fixed(client: Client, message: Message):
    await api_ceo_dog(client, message)

@randydev(command("dog3", cmd) & owner)
async def image_fixed_2(client: Client, message: Message):
    await api_ceo_dog2(client, message)
