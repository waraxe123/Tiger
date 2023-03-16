# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#


from TigerX import *
from ..lib import *

from random import choice

SLAP_FUNNY_ENGLISH = [ 
    "I'm sorry, did my hand accidentally slap your face?",
    "Oh, I'm sorry. I thought you were a mosquito.",
    "You know you deserved that, right?",
    "I didn't slap you. I just high-fived your face!",
    "It's not a slap, it's a wake-up call!",
    "If I slapped you any harder, Google would've found your next of kin.",
    "You're lucky I didn't headbutt you!",
    "Don't worry, I'm a professional slapper.",
]

SLAP_LUCU_INDONESIA = [
    "pertanyaan apa ini?",
]

async def slap_funny_lol(c, m):
    if m.reply_to_message and m.reply_to_message.from_user.username:
        username = m.reply_to_message.from_user.username
        slap_text = choice(SLAP_FUNNY)
        await c.send_message(m.chat.id, f"@{username}, {slap_text}")
    else:
        await m.reply_text("Please reply to a message to slap someone!")
