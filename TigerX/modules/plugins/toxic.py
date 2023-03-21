from TigerX import *
from TigerX.lib import *

from pykillerx.help import add_command_help

@randydev(command("war", cmd) & owner)
async def war_goblok(client: Client, message: Message):
    await toxic_1(client, message)

@randydev(command("dih", cmd) & owner)
async def dih_goblok(client: Client, message: Message):
    await toxic_2(client, message)

@randydev(command("gembel", cmd) & owner)
async def gembel_goblok(client: Client, message: Message):
    await toxic_3(client, message)

@randydev(command("sokab", cmd) & owner)
async def sokap_goblok(client: Client, message: Message):
    await toxic_4(client, message)

@randydev(command("ded", cmd) & owner)
async def ded_goblok(client: Client, message: Message):
    await toxic_5(client, message)

@randydev(command("caper", cmd) & owner)
async def caper_goblok(client: Client, message: Message):
    await toxic_6(client, message)

@randydev(command("lo", cmd) & owner)
async def lo_goblok(client: Client, message: Message):
    await toxic_7(client, message)

@randydev(command("woi", cmd) & owner)
async def woi_goblok(client: Client, message: Message):
    await toxic_8(client, message)

@randydev(command("ngatur", cmd) & owner)
async def ngatur_goblok(client: Client, message: Message):
    await toxic_9(client, message)

@randydev(command("ubot", cmd) & owner)
async def ubot_goblok(client: Client, message: Message):
    await toxic_10(client, message)

@randydev(command("d", cmd) & owner)
async def d_goblok(client: Client, message: Message):
    await toxic_11(client, message)

@randydev(command("e", cmd) & owner)
async def e_goblok(client: Client, message: Message):
    await toxic_12(client, message)

@randydev(command("f", cmd) & owner)
async def f_goblok(client: Client, message: Message):
    await toxic_13(client, message)

@randydev(command("i", cmd) & owner)
async def i_goblok(client: Client, message: Message):
    await toxic_14(client, message)

@randydev(command("q", cmd) & owner)
async def q_goblok(client: Client, message: Message):
    await toxic_15(client, message)

@randydev(command("t", cmd) & owner)
async def t_goblok(client: Client, message: Message):
    await toxic_16(client, message)

@randydev(command("u", cmd) & owner)
async def u_goblok(client: Client, message: Message):
    await toxic_17(client, message)

add_command_help(
    "toxic",
    [
        ["war", "usage: "],
        ["dih", "usage: "],
        ["gembel", "usage: "],
        ["sokap", "usage: "],
        ["ded", "usage: "],
        ["caper", "usage: "],
        ["lo", "usage: "],
        ["woi", "usage: "],
        ["ngatur", "usage: "],
        ["ubot", "usage: "],
        ["d", "usage: "],
        ["e", "usage: "],
        ["f", "usage: "],
        ["i", "usage: "],
        ["q", "usage: "],
        ["t", "usage: "],
        ["u", "usage: "],

    ],  
)

