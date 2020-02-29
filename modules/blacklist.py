
async def addToBlacklist(self, msg, args):
    if not msg.author.id in self.owners:
        await msg.channel.send(':x: You do not have permission to do this.')
        return
    if not msg.mentions[0].id in self.blacklistedUsers:
        self.blacklistedUsers.append(msg.mentions[0].id)
        await msg.channel.send('Blacklisted **{}** from using the bot (to perm-blacklist them, put it in the config file)'.format(str(msg.mentions[0])))
        return
    await msg.channel.send(':x: user already blacklisted.')


async def removeFromBlacklist(self, msg, args):
    if not msg.author.id in self.owners:
        await msg.channel.send(':x: You do not have permission to do this.')
        return
    if msg.mentions[0].id in self.blacklistedUsers:
        self.blacklistedUsers.remove(msg.mentions[0].id)
        await msg.channel.send('Allowed **{}** to use the bot'.format(str(msg.mentions[0])))
        return
    await msg.channel.send(':x: user not blacklisted.')



async def listBlacklist(self,msg,args):
    if not msg.author.id in self.owners:
        await msg.channel.send(':x: You do not have permission to do this.')
        return
    await msg.channel.send('Blacklisted users: `{}`'.format(', '.join(self.blacklistedUsers)))

async def init(self):
    await self.registerCommand(addToBlacklist, 'ablacklist', 'ablacklist <mention>', 'blacklist a user from using the bot (bot owner only)')
    await self.registerCommand(listBlacklist, 'lblacklist', 'lblacklist', 'list blacklisted users (bot owner only)')
    await self.registerCommand(removeFromBlacklist, 'ublacklist', 'ulblacklist <mention>', 'remove users from blacklist (bot owner only)')
