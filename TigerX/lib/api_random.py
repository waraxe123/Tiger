# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Developer Credits: @xtsea

import requests
from random import choice

async def api_ceo_dog(client, message):
    ran = await message.reply_text("<code>Uploading.......</code>")
    API_DOG = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(API_DOG)
    if response.status_code == 200:
        data_ceo = response.json()
        try:
            photo_dog_url = data_ceo["message"]
        except Exception as e:
            await ran.edit_text(f"Error requests: {e}")
            return
        if photo_dog_url:
            await client.send_photo(message.chat.id, photo=photo_dog_url, reply_to_message_id=message.id)
        else:
            await ran.edit_text("Not founds")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass

async def api_big_cat(client, message):
    ran = await message.reply_text("<code>Uploading.......</code>")
    API_BIG_CAT = "https://randombig.cat/roar.json"
    response = requests.get(API_BIG_CAT)
    if response.status_code == 200:
        data_cat = response.json()
        try:
            photo_cat_url = data_cat["url"]
        except Exception as e:
            await ran.edit_text(f"Error requests: {e}")
            return
        if photo_cat_url:
            await client.send_photo(message.chat.id, photo=photo_cat_url, reply_to_message_id=message.id)
        else:
            await ran.edit_text("Not founds")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass

async def api_ceo_dog2(client, message):
    ran = await message.reply_text("<code>Uploading.......</code>")
    API_CEO_DOG2 = "https://random.dog/woof.json"
    response = requests.get(API_CEO_DOG2)
    if response.status_code == 200:
        data_dog2 = response.json()
        try:
            photo_dog2_url = data_dog2["url"]
        except Exception as e:
            await ran.edit_text(f"Error requests: {e}")
            return
        if photo_dog2_url:
            await client.send_photo(message.chat.id, photo=photo_dog2_url, reply_to_message_id=message.id)
        else:
            await ran.edit_text("Not founds")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass

async def api_fox_ca(client, message):
    ran = await message.reply_text("<code>Uploading.......</code>")
    API_FOX_CA = "https://randomfox.ca/floof/"
    response = requests.get(API_FOX_CA)
    if response.status_code == 200:
        data_fox = response.json()
        try:
            photo_fox_url = data_fox["image"]
        except Exception as e:
            await ran.edit_text(f"Error requests: {e}")
            return
        if photo_fox_url:
            await client.send_photo(message.chat.id, photo=photo_fox_url, reply_to_message_id=message.id)
        else:
            await ran.edit_text("Not founds")
    else:   
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass


async def api_animechan_new(client, message):
    ran = await message.reply_text("<code>Processing anime quotes.......</code>")
    vercel_link = "https"
    vercel_name = "animechan.vercel.app"
    vercel_api = "api"
    vercel_random = "random"
    vercel_param = f"{vercel_link}://{vercel_name}/{vercel_api}/{vercel_random}"
    response = requests.get(vercel_param)
    if response.status_code == 200:
        data_animechan = response.json()
        try:
            anime_name = data_animechan["anime"]
            anime_character = data_animechan["character"]
            anime_quote = data_animechan["quote"]
        except Exception as e:
             await ran.edit_text(f"Error request {e}")
             return
        if anime_name and anime_character and anime_quote:
            animechan_full = f"<b>Anime name:</b> {anime_name}\n<b>Character:</b> {anime_character}\n<b>Quote:</b> {anime_quote}"
            await ran.edit_text(animechan_full)
        else: 
            await ran.edit_text("Not founds animechan")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")


async def api_waifu_main(client, message):
    ran = await message.reply_text("<code>Processing.......</code>")
    LIST_SFW_JPG = ["neko", "waifu", "megumin"]
    waifu_link = "https"
    waifu_api = "api.waifu.pics"
    waifu_types = "sfw"
    waifu_category = choice(LIST_SFW_JPG)
    waifu_param = f"{waifu_link}://{waifu_api}/{waifu_types}/{waifu_category}"
    response = requests.get(waifu_param)
    if response.status_code == 200:
        data_waifu = response.json()
        try:
            waifu_image_url = data_waifu["url"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        if waifu_image_url:
            await client.send_photo(message.chat.id, photo=waifu_image_url, reply_to_message_id=message.id)
        else:
            await ran.edit_text("Not founds animechan")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass

# DO NOT SHARE THIS MODULE 
# THIS DANGER IS TRACKED

async def hacker_lacak_target(client, message):
    apikey = "3D07E2EAAF55940AF44734C3F2AC7C1A"
    ran = await message.reply_text("<code>Processing.......</code>")
    ipddres = message.text.split(None, 1)[1] if len(message.command) != 1 else None)
    if not ipddres:
        await pro.edit("Example: <code>ip <your_ip_addres></code>")
        return

    if not apikey:
        await pro.edit_text("Missing apikey ip location")
        return

    location_link = "https"
    location_api = "api.ip2location.io"
    location_key = f"key={apikey}"
    location_search = f"ip={ipddres}"
    location_param = f"{location_link}://{location_api}/?{location_key}&{location_search}"
    location_target = ""
    response = requests.get(location_param)
    if response.status_code == 200:
        data_location = response.json()
        try:
            location_ip = data_location["ip"]
            location_code = data_location["country_code"]
            location_name = data_location["country_name"]
            location_region = data_location["region_name"]
            location_city = data_location["city_name"]
            location_zip = data_location["zip_code"]
            location_zone = data_location["time_zone"]
            location_card = data_location["as"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
         if location_ip and location_code and location_name and location_region and location_city and location_zip and location_zone and location_card:
             location_target += f"<b>IP Address:</b> {location_ip}\n"
             location_target += f"<b>Country code:</b> {location_code}\n"
             location_terget += f"<b>Country name:</b> {location_name}\n"
             location_target += f"<b>Region name:</b> {location_region}\n"
             location_target += f"<b>City name:</b> {location_city}\n"
             location_target += f"<b>Zip code:</b> {location_zip}\n"
             location_target += f"<b>Time Zone:</b> {location_zone}\n"
             location_target += f"<b>Data card:</b> {location_card}\n"
             await ran.edit_text(location_target)
         else:
             await ran.edit_text("Not data ip address")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
