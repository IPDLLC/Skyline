

async def ping(self, msg, args):
    await msg.channel.send(':white_check_mark: pong')

async def init(self):
    await self.registerCommand(ping, 'ping', 'ping', 'test if the bot is responding')

