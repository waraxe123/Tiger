import os
from io import BytesIO
from TigerX import *
from TigerX.lib import *
from pyrogram import filters
from pyrogram.types import Message
from config import MAX_MESSAGE_LENGTH
from pykillerx.helper.clear_string import clear_string
from pykillerx.helper.check_size import get_directory_size

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))


async def list_directories(c, m):
    if len(m.text.split()) == 1:
        location = "."
    elif len(m.text.split()) >= 2:
        location = m.text.split(None, 1)[1]

    await m.edit_text("Fetching files...")

    location = os.path.abspath(location)
    if not location.endswith("/"):
        location += "/"
    OUTPUT = f"Files in <code>{location}</code>:\n\n"

    try:
        files = os.listdir(location)
        files.sort()
    except FileNotFoundError:
        await m.edit_text(f"No such file or directory {location}")
        return

    for file in files:
        OUTPUT += f"• <code>{file}</code> ({get_directory_size(os.path.abspath(location+file))})\n"

    if len(OUTPUT) > MAX_MESSAGE_LENGTH:
        OUTPUT = clear_string(OUTPUT)  # Remove the html elements using regex
        with BytesIO(str.encode(OUTPUT)) as f:
            f.name = "ls.txt"
            await m.reply_document(
                document=f,
                caption=f"{location} ({get_directory_size(os.path.abspath(location))})",
            )
        await m.delete()
    else:
        if OUTPUT.endswith("\n\n"):
            await m.edit_text(f"No files in {location}")
            return
        await m.edit_text(OUTPUT)

    return
