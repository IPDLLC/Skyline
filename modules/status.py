
import discord

async def init(self):
    watching = discord.Activity(name='the behaviour of members on {} guilds'.format(len(self.guilds)), type=discord.ActivityType.watching)
    await self.change_presence(status=discord.Status.dnd, activity=watching)
