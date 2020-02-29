alepsaFile = 'db/alepsa.txt'

import random

# community 8ball
async def alepsa(self, msg, args):
        f = open(alepsaFile, 'r')
        replies = f.readlines()
        f.close()
        for i in range(len(replies)):
            replies[i] = replies[i][:-1]
        ranReply = replies[int(random.uniform(0,len(replies)))]
        await msg.channel.send('Alepsa says **{}**'.format (ranReply))
async def addreply(self, msg, args):
        f = open(alepsaFile, 'a')
        f.write(args)
        f.close()
        await msg.channel.send('Sucessfully added **{}** to the list of replies!'.format (args))   
async def removereply(self, msg, args):
    if message.author.guild_permissions.kick_members:
        f.open(alepsaFile, 'rw')
        cleanReplies = []
        dirtyReplies = f.readlines()
        if len(args) < 2: # if the filter is too small assume they are trying to delete the entire database and stop them
            await msg.channel.send(':x: NO U how dare you try deleing the entire database thats not nice')
            return
        for i in dirtyReplies:
            if not args in i:
                cleanReplies.append(i)
        f.write(cleanReplies)
        f.close()
        await msg.channel.send('Removed **{}** replies containing **{}**'.format(len(dirtyReplies) - len(cleanReplies), args))

async def init(self):
    await self.registerCommand(alepsa, 'alepsa', 'alepsa <question>', '8ball but alexa with a lisp')
    await self.registerCommand(addreply, 'addalepsa', 'addalepsa <reply>', 'add your replies to alepsa!')
    await self.registerCommand(removereply, 'removealepsa', 'removealepsa <reply>', 'remove replies in alepsa!')
