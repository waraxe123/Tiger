import sys
from os import environ, execle, remove
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren
from pyrogram import Client

from TigerX import *
from TigerX.lib import *

from pykillerx.helper.basic import *
from pykillerx import *
from pykillerx.helper import *


async def restart_bot(_, message):
    try:
        msg = await edit_or_reply(message, "`Restarting bot...`")
        LOGGER("TigerX").info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER("TigerX").info(f"{err}")
        return
    await msg.edit_text("✅ Bot has restarted !\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "TigerX"]
        execle(sys.executable, *args, environ)
