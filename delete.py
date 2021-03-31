import discord
import time
import os

client = discord.Client()


@client.event
async def on_ready():
  print(client.user.name)
  print('ready')
  game = discord.Game("사랑")
  await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
  if message.content.startswith('!청소'):
    await message.channel.purge(limit=50)
    time.sleep(1)
    embed = discord.Embed(colour=discord.Colour(0x7a92e2))
    embed.set_footer(text="After 5 seconds this message will be cleared automatically.")
    embed.add_field(name="Clear Bot", value="```50 messages have been deleted successfully.```")
    name = await message.channel.send(embed=embed)
    time.sleep(5)
    await name.delete()

access_token = os.environ['BOT_TOKEN']
client.run("Nzk2MDI4MjE0MTg3MTMwOTMx.X_R9Cw.YzG0EPyK2cCFJ1ORf0sla5yOVJY")
