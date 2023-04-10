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

@randydev(command("ask", cmd) & owner)
async def chatgpt_rapi_cmd(client: Client, message: Message):
    await new_model_chatgpt(client, message)

@randydev(command("askt", cmd) & owner)
async def chatgpt_rapi_turbo_cmd(client: Client, message: Message):
    await new_chatgpt_turbo(client, message)

@randydev(command(["dalle"], cmd) & owner)
async def chatgpt_image_cmd(client: Client, message: Message):
    await chatpgt_image_generator(client, message)

add_command_help(
    "openai",
    [
        ["ask [question]", "to ask questions using the api chatgpt openai"],
        ["askt [question]", "to ask questions using the api chagpt turbo"],
        ["dalle [question]", "to chatgpt image generator using the API."],

    ],
)
