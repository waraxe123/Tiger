# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Credits by : https://t.me/xtsea

from TigerX import app
from TigerX.lib import *

@app.on_message(filters.private)
async def take_channel(client: Client, message: Message):
    await ass_copy_link(client, message)
