alepsaFile = 'db/alepsa.txt'

import random

# community 8ball essentially, add whatever the hell u want, unless its racism or bad words etc etc this is a kids show :)
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
        f.write(args + '\n')
        f.close()
        await msg.channel.send('Sucessfully added **{}** to the list of replies!'.format (args))   


async def init(self):
    await self.registerCommand(alepsa, 'alepsa', 'alepsa <question>', '8ball but alexa with a lisp')
    await self.registerCommand(addreply, 'addalepsa', 'addalepsa <reply>', 'add your replies to alepsa!')
