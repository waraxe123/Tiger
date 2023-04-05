from TigerX import *
from TigerX.lib import *

from pykillerx.help import add_command_help

@randydev(command("cat", cmd) & owner)
async def cat_image_fixed(client: Client, message: Message):
    await api_big_cat(client, message)

@randydev(command("dog2", cmd) & owner)
async def image_fixed(client: Client, message: Message):
    await api_ceo_dog(client, message)

@randydev(command("dog3", cmd) & owner)
async def image_fixed_2(client: Client, message: Message):
    await api_ceo_dog2(client, message)

@randydev(command("fox", cmd) & owner)
async def image_fixed_3(client: Client, message: Message):
    await api_fox_ca(client, message)

add_command_help(
    "apitools",
    [
        ["cat", "to using api cat."],
        ["dog2", "to using api dog."],
        ["dog3", "to using api dog versi 2."],
        ["fox", "to using api fox ."],
        ["ip", "to using api get trace ip address."],
    ],
)
