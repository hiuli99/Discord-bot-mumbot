# imported libraries
import discord
import os
import asyncio
import youtube_dl

# Discord bot initialization
token = #add your token here
client = discord.Client()

voice_clients = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': "-vn"}

# Event happens when the bot gets run
@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

# Bot checks for messages that contain ?hi and responds to the user
@client.event
async def on_message(msg):
    if msg.author != client.user:
        if msg.content.lower().startswith("?hi"):
            await msg.channel.send(f"Hi, {msg.author.display_name}")


# Bot checks for messages that contain ?play command and starts playing music in a voice channel
@client.event
async def on_message(msg):
    if msg.content.startswith("?play"):

        try:
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except:
            print("error")


        try:
            url = msg.content.split()[1]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options, executable="C:\\ffmpeg\\ffmpeg.exe") #you'll need to download ffmpeg to your PC (https://ffmpeg.org/download.html) and place it in a location that's easy for you. this changes from person to person

            voice_clients[msg.guild.id].play(player)


        except Exception as err:
            print(err)


# Bot pauses the music with the command ?pause
    if msg.content.startswith("?pause"):
        try:
            voice_clients[msg.guild.id].pause()
        except Exception as err:
            print(err)          


# Bot stops the music with the command ?stop
    if msg.content.startswith("?stop"):
        try:
            voice_clients[msg.guild.id].stop()
            await voice_clients[msg.guild.id].disconnect()
        except Exception as err:
            print(err)    
            

# Bot resumes the music with the command ?resume            
    if msg.content.startswith("?resume"):
        try:
            voice_clients[msg.guild.id].resume()
        except Exception as err:
            print(err)           
                   

client.run(token)