import nextcord
from nextcord.ext import commands
import os

from nhlpy import NHLClient
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


    class Hockey(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self._last_member = None

        @commands.command()
        async def games(self, ctx):
            games = client.schedule.daily_schedule()
            await ctx.send(games)

    class Greetings(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self._last_member = None

        @commands.Cog.listener()
        async def on_member_join(self, member):
            channel = member.guild.system_channel
            if channel is not None:
                await channel.send(f'Welcome {member.mention}!')

        @commands.command()
        async def hello(self,ctx, *, member: nextcord.Member = None):
            member = member or ctx.author
            if self._last_member is None or self._last_member != member.id:
                await ctx.send(f'Hello {member.mention}!')
            else:
                await ctx.send(f'Hello {member.mention}... This seems familiar.')
            self._last_member = member


    bot.add_cog(Greetings(bot))
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