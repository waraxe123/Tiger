# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command("askd", cmd) & owner)
async def chatgpt_cmd(c: Client, m: Message):
    await chatgpt_ask(c, m)

@randydev(command("askd2", cmd) & owner)
async def chatgpt_rapi_cmd(client: Client, message: Message):
    await new_model_chatgpt(client, message)

@randydev(command("askt", cmd) & owner)
async def chatgpt_rapi_turbo_cmd(client: Client, message: Message):
    await new_chatgpt_turbo(client, message)

@randydev(command(["aimage", "dalle"], cmd) & owner)
async def chatgpt_image_cmd(c: Client, m: Message):
    await chatpgt_image_generator(c, m)

add_command_help(
    "chatgpt",
    [
        [f"ask [question]", "to ask questions using the API."],
        [f"aimage [question]", "to chatgpt image generator using the API."],
    ],
)
