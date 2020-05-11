# base commands like help modules etc

async def help(self, msg, args):
    if args in self.help:
        await msg.channel.send("**Usage**: "+self.help[args][0]+"\n**Description**: "+self.help[args][1])
    else:
        await msg.channel.send("**Here are my available commands**:\n"+' '.join(list(self.help.keys())))

async def modules(self, msg, args):
    await msg.channel.send("**Here are my currently loaded modules**:\n"+' '.join(list(self.modules.keys())))

async def about(self, msg, args):
    await msg.channel.send("**About the bot**:\nSkyline is a basic moderations bot which is very lightweight and easy to use, to list all commands, type !?help. To invite the bot, type !?invite. Join the official discord server here at: **https://discord.gg/nDgYsha**")

async def init(self):
    await self.registerCommand(help, 'help', 'help [command]', 'show how to use commands or list the commands')
    await self.registerCommand(modules, 'modules', 'modules', 'list the currently loaded modules.')
    await self.registerCommand(about, 'about', 'about', 'information about the bot')



