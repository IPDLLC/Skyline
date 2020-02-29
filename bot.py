#!/usr/bin/env python3

import config, perms
import discord, traceback, asyncio, sys, os



class Bot(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        
        await asyncio.sleep(1)

        self.modules = {}
        self.cmd = {}
        self.rawMessages = []
        self.timeouts = []
        self.help = {}
        self.prefix = "!?"

        self.blacklistedUsers = config.blacklistedUsers       
        self.owners = config.botOwners

        print('loading modules...')

        await self.loadModules()
        self.timeoutBg = self.loop.create_task(self.timeoutLoop())
        
    async def loadModules(self):
        for i in [s for s in os.listdir('modules') if ".py" in s]:
            i = i[:-3]
            await self.loadModule(i)
        print('done loading modules!')

    async def loadModule(self, i):
        if not (i in self.modules):
            print('loading module',i)
            m = __import__("modules."+i)
            m = eval('m.'+i)
            await m.init(self)
            self.modules[i] = m
        else:
            return [1, 'module already loaded']

    async def registerCommand(self, e, c, u, d):
        self.cmd[c] = e # function to call on command
        self.help[c] = [u, d] # record help text and description

    async def registerRaw(self, c): # make a module receive all messages
        self.rawMessages.append(c)

    async def registerTimeout(self, e, s): # module will be called back in amount of time
        self.timeouts.append([s, e])

    async def timeoutLoop(self):
        await self.wait_until_ready()
        while not self.is_closed():
            if len(self.timeouts) > 0:
                for i in range(len(self.timeouts)):
                    self.timeouts[i][0] = self.timeouts[i][0] - 1
                    if self.timeouts[i][0] < 1:
                        await self.timeouts[i][1](self)
                        self.timeouts.pop(i)
            await asyncio.sleep(1)

    async def permCheck(self, user):
        return await perms.permCheck(self, user)

    async def on_message(self, message):
        if message.author.id in self.blacklistedUsers:
            return
        if message.content[0:len(self.prefix)] == self.prefix:
            args = message.content[len(self.prefix):].strip().split()
            try:
                cmd = args.pop(0)
            except:
                return
            args = ' '.join(args)
            if cmd in self.cmd:
                try:
                    await self.cmd[cmd](self, message, args)
                except BaseException as e:
                    await message.channel.send("invalid input, do {}help {} to see syntax".format(self.prefix, cmd))
                    print('error', e)
                    n = sys.exc_info()
                    print(n, "Inp:", message.content)
                    traceback.print_tb(n[2])

client = Bot()
client.run(config.botToken)


