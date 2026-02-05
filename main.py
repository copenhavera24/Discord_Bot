import nextcord
from nextcord.ext import commands
import os

from dotenv import load_dotenv
from nextcord.ext import commands

load_dotenv()


if(os.getenv("TARGET_ENV") == "dev"):
    TESTING_GUILD_ID = os.getenv('TESTING_GUILD_ID')
    DISCORD_KEY = os.getenv("DISCORD_KEY")

    print(TESTING_GUILD_ID)
    print(DISCORD_KEY)

    intents = nextcord.Intents.default()
    intents.members = True
    intents = nextcord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='$', intents=intents)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')

    @bot.slash_command(description='this should be my command', guild_ids=[TESTING_GUILD_ID])
    async def test(interaction: nextcord.Interaction):
        await interaction.send("This should run through my program not the test program")

    @bot.command()
    async def test(ctx, args):
        await ctx.send(args)

    bot.run(DISCORD_KEY)
elif(os.getenv("TARGET_ENV") == "prod"):
    TESTING_GUILD_ID = os.getenv('TESTING_GUILD_ID')
    DISCORD_KEY = os.getenv("DISCORD_KEY")

    print(TESTING_GUILD_ID)
    print(DISCORD_KEY)

    intents = nextcord.Intents.default()
    intents.members = True
    intents = nextcord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='$', intents=intents)


    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')


    @bot.slash_command(description='this should be my command', guild_ids=[TESTING_GUILD_ID])
    async def test(interaction: nextcord.Interaction):
        await interaction.send("This should run through my program not the test program")


    @bot.command()
    async def test(ctx, arg):
        await ctx.send(arg)


    bot.run(DISCORD_KEY)