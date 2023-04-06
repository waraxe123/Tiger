from TigerX import *
from TigerX.lib import *

@randydev(command("ip", cmd) & owner)
async def location_hanlder(client: Client, message: Message):
    await hacker_lacak_target(client, message)

@randydev(command("ipd", cmd) & owner)
async def domain_hanlder(client: Client, message: Message):
    await whois_domain_target(client, message)
