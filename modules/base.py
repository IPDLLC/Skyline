# base commands like help modules etc

async def help(self, msg, args):
    if args in self.help:
        await msg.channel.send("**Usage**: "+self.help[args][0]+"\n**Description**: "+self.help[args][1])
    else:
        await msg.channel.send("**Here are my available commands**:\n"+' '.join(list(self.help.keys())))

async def modules(self, msg, args):
    await msg.channel.send("**Here are my currently loaded modules**:\n"+' '.join(list(self.modules.keys())))

async def about(self, msg, args):
    await msg.channel.send("**About the bot**:\nwl-bot is the moderation bot for r/windowsloser's discord. the prefix is ? and you can find the source code at https://github.com/lickthecheese/wl-bot")

async def init(self):
    await self.registerCommand(help, 'help', 'help [command]', 'show how to use commands or list the commands')
    await self.registerCommand(modules, 'modules', 'modules', 'list the currently loaded modules.')
    await self.registerCommand(about, 'about', 'about', 'information about the bot')



