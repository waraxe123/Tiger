# original pyrogram 
# made by @xtsea

from TigerX import *
from TigerX.lib import *
from bs4 import BeautifulSoup as bs
import requests

async def pinterest_downloader(client, message):
    ran = await message.reply_text("<code>Processing.....</code>")
    link = message.text.split(" ", 1)[1] if len(message.command) > 1 else None
    if not link:
        await ran.edit_text("Example: <code>.pintr</code> <i>link</i>")
        return
    url = "https://www.expertstool.com/download-pinterest-video/"
    data = {"url": link}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        soup = bs(response.content, "html.parser")
        soup_str = None
        try: 
            soup_str = soup.find("table").tbody.find_all("tr")
        except Exception as e:
            await ran.edit_text(f"Error: {e}")
            return
        if soup_str:
            file = soup_str[1] if len(soup_str) > 1 else soup_str[0]
            file = file.td.a["href"]
            try:
                await client.send_video(message.chat.id, video=file)
            except Exception:
                await client.send_photo(message.chat.id, photo=file)
                return 
        else:
            await ran.edit_text("Unable to find Pinterest video")
    else:
        await ran.edit_text("Failed to api pinterest")
    try:
        await ran.delete()
    except Exception:
        pass
