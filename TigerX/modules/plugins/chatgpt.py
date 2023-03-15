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
async def chatgpt_cmd(c: Client, m: Message):
    await chatgpt_ask(c, m)

add_command_help(
    "chatgpt",
    [
        [f"ask [question]", "to ask questions using the API."],
    ],
)
