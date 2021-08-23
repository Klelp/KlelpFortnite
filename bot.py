import discord
import requests
from discord.ext import commands
from discord.ext import tasks

bot = commands.Bot(command_prefix='!')

@bot.command()
async def shop(ctx):
    embed = discord.Embed(title="Магазин Предметов")
    embed.set_image(url="https://fortool.fr/cm/assets/shop/ru.png")
    await ctx.send(embed=embed)

@bot.command()
async def news (ctx):
    r = requests.get("https://fortnite-api.com/v2/news/br")
    data = r.json()
    embed = discord.Embed(title="Новости")
    embed.add_field(name="Date", value=data["data"]["date"])
    embed.set_image(url=data["data"]["image"])
    await ctx.send(embed=embed);

