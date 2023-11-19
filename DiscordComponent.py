import discord
from discord import app_commands
from discord.ext import commands
from ossapi import OssapiV1
from os import getenv
import TopPlayGrabber
import PlaylistCreator
from dotenv import load_dotenv

load_dotenv()


bot = commands.Bot(command_prefix="?", intents = discord.Intents.all())


@bot.event
async def on_ready():
   print("bot is logged in!")
   try:
      synced = await bot.tree.sync()
      print(f"Synced {len(synced)} commands!")
   except Exception as e:
      print(e)

@bot.tree.command(name="create_playlist")
@app_commands.describe(username="Your osu! username")
async def create_playlist(interaction: discord.Interaction, username: str):
   msg = await interaction.response.send_message(f"{username}, Pulling top plays!", ephemeral=False)
   songs = TopPlayGrabber.pullTopPlays(username)
   spotComp = PlaylistCreator.SpotifyComponent()
   #TODO: Add handling of incorrect/nonexistant usernames
   # if songs == None:
   #    await interaction.followup("No plays found. Maybe the wrong username was given?")
   

bot.run(getenv('DISCORD_API'))