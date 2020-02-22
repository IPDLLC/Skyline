
import discord

async def init(self):
    await self.change_presence(status=discord.Status.dnd)
