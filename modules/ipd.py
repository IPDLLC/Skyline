

async def invite(self, msg, args):
    await msg.channel.send('Skyline would be more than happy to moderate your server! To invite the bot, click the link here: https://discordapp.com/oauth2/authorize?client_id=679066447942516760&scope=bot&permissions=8\nThe best part is, there is practically no setup! All you need to do is have staff roles that have permission to ban, kick and manage messages! :O')

async def init(self):
    await self.registerCommand(invite, 'invite', 'invite', 'get the invite link for the bot')

