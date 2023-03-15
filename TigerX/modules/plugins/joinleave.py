from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command(["joingc"], cmd) & owner)
async def join_command(client: Client, message: Message):
    await join_chat(client, message)

@randydev(command(["left"], cmd) & owner)
async def leave_command(client: Client, message: Message):
    await leave_chat(client, message)

@randydev(command(["leaveallgc"], cmd) & owner)
async def kickmeall_command(client: Client, message: Message):
    await kickmeall(client, message)

@randydev(command(["leaveallch"], cmd) & owner)
async def kickmeallch_command(client: Client, message: Message):
    await kickmeallch(client, message)

add_command_help(
    "joinleave",
    [
        [
            "kickme",
            "To leave!!.",
        ],
        ["leaveallgc", "to leave all groups where you joined."],
        ["leaveallch", "to leaveall channel where you joined."],
        ["join [Username]", "give an specific username to join."],
        ["left [Username]", "give an specific username to leave."],
    ],
)
