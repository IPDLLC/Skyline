
import discord

async def rlStat(self):
    watching = discord.Activity(name='the behaviour of members on {} guilds'.format(len(self.guilds)), type=discord.ActivityType.watching)
    await self.change_presence(status=discord.Status.dnd, activity=watching)

async def statCommand(self, msg, args):
    if msg.author.id in self.owners:
        await rlStat(self)
    else:
        await msg.channel.send(':x: you do not have permission to do that')

async def init(self):
    await rlStat(self)
    await self.registerCommand(statCommand, 'rlstat', 'rlstat', 'reloads status message, bot owners only')

