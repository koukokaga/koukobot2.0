
import discord
from discord.ext import commands
from discord.ext.commands import Bot


bot = commands.Bot(command_prefix='#')
bot.remove_command('help')


@bot.event
async def on_ready():
    print ("Bot reddy")


@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(':ping_pong:')
    print ("user has pinged")


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="", color=0x00FFFF)
    embed.add_field(name='name', value=user.name)
    embed.add_field(name='id', value=user.id)
    embed.add_field(name="Status", value=user.status)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Did you need soem help?", color=0x00FFFF)
    embed.add_field(name='help', value='shows this')
    await ctx.send(embed=embed)



bot.run("my token")