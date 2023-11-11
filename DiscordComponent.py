import discord
from discord import app_commands
from discord.ext import commands
from ossapi import OssapiV1
import TopPlayGrabber

api = OssapiV1("f320af2b16dbfcb597973d754e1ca39dabeaf7ab")

bot = commands.Bot(command_prefix="?", intents = discord.Intents.all())


@bot.event
async def on_ready(self):
   print(f"Logged in as {self.user}")
   try:
      synced = await bot.tree.sync()
      print(f"Synced {len(synced)} commands!")
   except Exception as e:
      print(e)

@bot.tree.command(name="create_playlist")
@app_commands.describe(username="Your osu! username")
async def create_playlist(interaction: discord.Interaction, username: str):
   await interaction.response.send_message(f"{username}, Pulling top plays!", ephemeral=False)
   TopPlayGrabber.pullTopPlays(username)
   

bot.run('MTA4NDAxNTE0MzE0ODU4NTAyMA.GoJaFN.fQVLfITpOwDpcYfrGhYwa7GAGAnxwj4xSyF4ag')