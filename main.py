import discord
import requests
import urllib
import json
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=".", intents=intents)
client.remove_command('help')
i = 1

index = "."
version = "1.0.0"
emico = "https://cdn.discordapp.com/app-icons/1016393360669429820/47dae0ec6191614278642cb8ec525a44.png?size=64"
name = "CringeAnimeBot"



# activity
@client.event
async def on_ready():
    print("bot runing....")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(f"{index}help"))


async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("missing arguments try .help")


async def on_perms_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("you don't have perms for this command!")


# help
@client.command(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="help", description="help with commands", color=discord.colour.Color.dark_magenta())
    em.set_author(name="CringeAnimeBot",
                  icon_url= emico)
    em.add_field(name="Moderation",
                 value="`.kick <user> <reason>`, `.ban <user> <reason>`, `.clear <msgcount>`")
    em.add_field(name="fun", value="`.ping`, `.meme`")
    em.add_field(name="weeb", value="`.waifu`, `.slap`, `.fox_girl`, `.animegif`, `.animewallpaper`")
    em.add_field(name="other", value="`.changelog`, `.help`, `.about`")
    em.set_footer(text=f"{name} v{version}")
    await ctx.send(embed=em)


# about
@client.command(invoke_without_command=True)
async def about(ctx):
    em = discord.Embed(title="about", description="informace o botovi", color=discord.colour.Color.dark_magenta())
    em.set_author(name="CringeAnimeBot",
                  icon_url= emico)
    em.add_field(name="`Created by Marosak#1867` ", value="`© Marosak#1867 2022`")
    em.set_footer(text=f"{name} v{version}")
    await ctx.send(embed=em)


# changelog
@client.command(invoke_without_command=True)
async def changelog(ctx):
    em = discord.Embed(title="changelog", description=f"{name} v{version}", color=discord.colour.Color.dark_magenta())
    em.set_author(name="Sakura咲良",
                  icon_url= emico)
    em.add_field(name="Moderation", value="`small changes in kick and ban command`")
    em.add_field(name="Bot", value="`changed .help command`")
    em.set_footer(text=f"{name} v{version}")
    await ctx.send(embed=em)


# pingpong
@client.command()
async def ping(ctx):
    await ctx.send("pong!")

# meme
@client.command()
async def meme(ctx):
    memeAPI = urllib.request.urlopen("https://meme-api.herokuapp.com/gimme")

    memeData = json.load(memeAPI)

    memeUrl = memeData["url"]
    memeName = memeData["title"]
    memePoster = memeData["author"]
    memeSub = memeData["subreddit"]
    memeLink = memeData["postLink"]

    em = discord.Embed(title=memeName, color=discord.colour.Color.dark_magenta())
    em.set_image(url=memeUrl)
    em.set_footer(text=f"created by: {memePoster},  subreddit: {memeSub},  post: {memeLink}")
    await ctx.send(embed=em)


# waifu
@client.command()
async def waifu(ctx):
    r = requests.get("https://nekos.life/api/v2/img/waifu")
    res = r.json()
    url = res['url']
    em = discord.Embed(title="Waifu", color=discord.colour.Color.dark_magenta())
    em.set_image(url=url)
    await ctx.send(embed=em)


# tapeta
@client.command()
async def animewallpaper(ctx):
    r = requests.get("https://nekos.life/api/v2/img/wallpaper")
    res = r.json()
    url = res['url']
    em = discord.Embed(title="wallpaper", color=discord.colour.Color.dark_magenta())
    em.set_image(url=url)
    await ctx.send(embed=em)


# slap
@client.command()
async def slap(ctx):
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    url = res['url']
    em = discord.Embed(title="slap", color=discord.colour.Color.dark_magenta())
    em.set_image(url=url)
    await ctx.send(embed=em)


# fox girl
@client.command()
async def fox_girl(ctx):
    r = requests.get("https://nekos.life/api/v2/img/fox_girl")
    res = r.json()
    url = res['url']
    em = discord.Embed(title="fox girl", color=discord.colour.Color.dark_magenta())
    em.set_image(url=url)
    await ctx.send(embed=em)


# animegif
@client.command()
async def animegif(ctx):
    r = requests.get("https://nekos.life/api/v2/img/ngif")
    res = r.json()
    url = res['url']
    em = discord.Embed(title="gif", color=discord.colour.Color.dark_magenta())
    em.set_image(url=url)
    await ctx.send(embed=em)


# kick
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, reason: str):
    await member.kick(reason=reason)


# ban
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, reason: str):
    await member.ban(reason=reason)
    await ctx.send(f"user {member.mention} baned")


# clear
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send("messages deleted")



client.run('TOKEN')
