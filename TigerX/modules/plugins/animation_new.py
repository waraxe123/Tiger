from TigerX import *
from TigerX.lib import *

@randydev(command("santet", cmd) & owner)
async def santet_lu_fix(client: Client, message: Message):
    await typewriter(client, message)

@randydev(command("whatsapp", cmd) & owner)
async def wa_lu_fix(client: Client, message: Message):
    await whatsapp_hack(client, message)

@randydev(command("macos", cmd) & owner)
async def macos_lu_fix(client: Client, message: Message):
    await macos_animation(client, message)

@randydev(command("police", cmd) & owner)
async def police_lu_fix(client: Client, message: Message):
    await police_animation(client, message)

@randydev(command("linux", cmd) & owner)
async def linux_lu_fix(client: Client, message: Message):
    await linux_hacker(client, message)

@randydev(command("hack", cmd) & owner)
async def hacker_lu_fix(client: Client, message: Message):
    await hacker_user(client, message)

@randydev(command(["kontol", "dick"], cmd) & owner)
async def kontol_lu_fix(client: Client, message: Message):
    await penis_tolol(client, message)
