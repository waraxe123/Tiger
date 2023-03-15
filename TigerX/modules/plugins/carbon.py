from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command("carbon", cmd) & owner)
async def carbon_func_command(client: Client, message: Message):
    await carbon_func(client, message)
