from TigerX import *
from TigerX.lib import *

@randydev(command("facedetect2", cmd) & owner)
async def ninja_detect(client: Client, message: Message):
    await api_ninja_detect(client, message)

@randydev(command(["dog", "dogs"], cmd) & owner)
async def ninja_dog_handler(client: Client, message: Message):
    await api_ninja_dogs(client, message)
