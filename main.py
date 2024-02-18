import discord, os , alive , asyncio , datetime ,pytz


from discord.ext import tasks, commands

client = commands.Bot(intents=discord.Intents.all() , command_prefix= "!" , description='test')



# name = for your status and url = for your twitch link
@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = 
  "status", url = "https://twitch.tv/paogah"))



alive.alive()
client.run(os.getenv("TOKEN"), bot=False)
