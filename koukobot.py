
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


bot = commands.Bot(command_prefix='#')


@bot.event
async def on_ready():
    print ("Bot reddy")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong:")
    print ("user has pinged")


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="here is your information", color=0x00FFFF)
    await bot.say("name is: {}".format(user.name))
    await bot.say("users ID is: {}".format(user.id))
    await bot.say("highest role is: {}".format(user.top_role))
    await bot.say("joined at: {}".format(user.joined_at))
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="info about the bot", description="this is my description", color=0x00FFFF)
    embed.set_footer(text="this is my little project hehe")
    embed.set_author(name="kouko kaga")
    

bot.run("TOKEN")