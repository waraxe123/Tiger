import requests
import spotify_token as st
from pyrogram import Client, enums, filters
from TigerX import *
from TigerX.lib import *

async def lyrics(client, message):
    if len(message.command) == 1:
        await message.reply("Usage: `.lyrics <song>`")
    else:
        query = message.text[1+6+1:]

    if not SP_DC and not SP_KEY:
        await message.reply("Missing api key: `SP_DC` and `SP_KEY`")
        return 

        spotify = st.start_session(SP_DC, SP_KEY)
        access_token = spotify[0]
        r_spotify = requests.get("https://api.spotify.com/v1/search?q=" + query + "&type=track", headers={"Authorization": "Bearer " + access_token})

        if r_spotify.status_code == 200:
            track_url = r_spotify.json()['tracks']['items'][0]['external_urls']['spotify']
            artist = r_spotify.json()['tracks']['items'][0]['artists'][0]['name']
            title = r_spotify.json()['tracks']['items'][0]['name']
            album = r_spotify.json()['tracks']['items'][0]['album']['name']
            album_year = r_spotify.json()['tracks']['items'][0]['album']['release_date'][:4]

            r_lyrics = requests.get("https://spotify-lyric-api.herokuapp.com/?url=" + track_url)

            if r_lyrics.status_code == 200:
                lyrics_message = f"**{artist}\n{title}**\nFrom __{album}__ ({album_year}) ([listen]({track_url}))\n\n"

                for lines in r_lyrics.json()['lines']:
                    lyrics_message += lines['words'] + "\n"
                
                await message.reply(lyrics_message)
            else:
                await message.reply("No lyrics found")
        else:
            await message.reply("The server returned an error")
