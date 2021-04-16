import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


from animeAPI import get_anime_info

# Discord token
load_dotenv('.env')
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='!')


@bot.listen()
async def on_ready():
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game('Watching Anime :]')
    )
    
    print("Bot is ready!")


@bot.command()
async def ping(ctx):
    '''Displays the ping'''
    embed = discord.Embed(
        title=f'Pong! {round(bot.latency*1000)}ms',
        color=discord.Color.dark_purple()
    )

    await ctx.send(embed=embed)


@bot.command()
async def anime(ctx, *, anime_name):
    '''Get download links and useful information for the given anime'''
    async with ctx.typing():
        anime = get_anime_info(query=anime_name)
        if anime is None:
            embed = discord.Embed(description=f"Coudn't find **{anime_name}**",
                                  color=discord.Color.dark_green())
            return await ctx.send(embed=embed)

        embed = discord.Embed(color=discord.Color.dark_green())
        embed.set_author(name=anime.title, icon_url=ctx.author.avatar_url)
        embed.add_field(name='Episodes', value=anime.episodes, inline=False)
        embed.add_field(name='Duration', value=anime.duration, inline=False)
        embed.add_field(name='Genres', value=anime.genres, inline=False)
        embed.add_field(name='Rating', value=anime.rating, inline=False)
        embed.add_field(name='Aired', value=anime.aired, inline=False)
        
        embed.add_field(name="Link", 
                        value=f"**[Download anime from here]({anime.download})**", 
                        inline=False
                       )
        
        embed.set_image(url=anime.thumbnail)
        await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x: **`Argument missing`**")

    elif isinstance(error, commands.CommandError):
        await ctx.send(":x: **`Command does not exist`**")


if __name__=="__main__":
    bot.run(TOKEN)