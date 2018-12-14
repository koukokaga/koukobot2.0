
import discord
from discord.ext import commands
from discord.ext.commands import Bot


bot = commands.Bot(command_prefix='#')
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='#help'))
    print ("Bot reddy")


@bot.command()
async def ping(ctx):
    await ctx.send(':ping_pong:')
    print ("user has pinged")


@bot.command()
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="", color=0x00FFFF)
    embed.add_field(name='name', value=user.name)
    embed.add_field(name='id', value=user.id)
    embed.add_field(name="Status", value=user.status)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Did you need some help?", color=0x00FFFF)
    embed.add_field(name='help', value='shows this', inline=True)
    embed.add_field(name='info @user', value='shows information', inline=True)
    embed.add_field(name='ping', value='returns :ping_pong:', inline=True)
    embed.add_field(name='Purge',value='purges chat', inline=True)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)  
async def purge(ctx ,amount=100):
    await ctx.channel.purge(limit=int(amount) + 1)
    await ctx.send('Deleted message(s)')

    

bot.run("token")