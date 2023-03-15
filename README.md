## 🐯 TigerX-Userbot 🐯

![20230312_175518](https://user-images.githubusercontent.com/90479255/224540113-fe730120-64e1-44d4-90ca-000c23cd3796.jpg)

## 📝 Disclaimer 📝
```
️                       ⚠️ WARNING FOR YOU ️ ️⚠️
   TigerX is used to help your account activities on Telegram
   We are not responsible for what you misuse in this repository
   !  Be careful when using this repository!
   If one of the members misuses this repository, we are forced to ban you
   Never ever abuse this repository
```

## 🛠️ VPS 🛠️
```console
Rendy@Ubuntu~ $ sudo apt update && sudo apt upgrade -y
Rendy@Ubuntu~ $ git clone https://github.com/TeamKillerX/TigerX-Userbot && cd TigerX-Userbot
Rendy@Ubuntu~ $ bash install.sh
Rendy@Ubuntu~ $ pip3 install -r req *
Rendy@Ubuntu~ $ cp sample_config.env config.env
Rendy@Ubuntu~ $ nano config.env
Rendy@Ubuntu~ $ screen -S tiger
Rendy@Ubuntu~ $ python3 -m TigerX
# ctrl a + d 
```

## 💎 Example Plugins 💎
* this module plugins : [Click Here](https://github.com/TeamKillerX/TigerX-Userbot/tree/main/TigerX/modules/plugins)

```python
from TigerX import *
from TigerX.lib import * 

from pykillerx.help import add_command_help 

@randydev(command("example", cmd) & owner)
async def hello_world_command(client, Client, message: Message):
    await hello_world(client, message)
```


* this module lib : [Click Here](https://github.com/TeamKillerX/TigerX-Userbot/tree/main/lib)
* you can add <code>__init__.py</code>
* don't forget to add files `example.py`
* like example : `from .example import *`

```python
# your own : @example or https://t.me/xtsea

async def hello_world(client, message):
    await client.send_message(message.chat.id, "Hello World")
```
* Code : [pull requests](https://github.com/TeamKillerX/TigerX-Userbot/pulls)

## 📜 License 📜

[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
TeamKillerX is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

<h4 align="center">Copyright (C) 2020 - 2023 <a href="https://github.com/TeamKillerX">TeamKillerX</a></h4>

Project [TigerX-Userbot](https://github.com/TeamKillerX/TigerX-Userbot) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.


## 🧑‍💻 Credits 🧑‍💻
* [![TeamKillerX-Devs](https://img.shields.io/static/v1?label=TeamkillerX&message=devs&color=critical)](https://t.me/xtsea)
* [Dan](https://github.com/pyrogram/) for [Pyrogram.](https://github.com/pyrogram/pyrogram)
* [Zaid](https://github.com/ITZ-ZAID/) for [Zaid-Userbot](https://github.com/ITZ-ZAID/ZAID-USERBOT)
* [mrismanaziz](https://github.com/mrismanaziz/) for [Pyroman-Userbot](https://github.com/mrismanaziz/PyroMan-Userbot)
* [UsergeTeam](https://github.com/UsergeTeam/) for [Userge](https://github.com/UsergeTeam/Userge)
* [TeamDerUntergang](https://github.com/TeamDerUntergang/) for [Telegram-SedenUserbot](https://github.com/TeamDerUntergang/Telegram-SedenUserBot)
* [TeamUltroid](https://github.com/TeamUltroid/) for [Ultroid](https://github.com/TeamUltroid/Ultroid)
