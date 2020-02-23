# economy module

import json

async def loadJson(self):
    try:
        with open('db/stonks.json') as json_file:
            data = json.load(json_file)
            self.stonksData = data
    except FileNotFoundError:
        print('not found')

async def writeJson(self):
    with open('db/stonks.json', 'w') as outfile:
        json.dump(self.stonksData, outfile)



async def createToken(self, msg, m):
    if ''.join(m) in self.stonksData:
        await msg.channel.send(':x: that token already exists.')
    else:
        m = ''.join(m)
        self.stonksData[m] = {msg.author.id: 100000}
        await msg.channel.send(':white_check_mark: token `{}` created!'.format(m))

async def sendToken(self, msg, m):
    if self.stonksData[m[2]][str(msg.author.id)] - float(m[1]) >= 0 and float(m[1]) > 0:
        try:
            self.stonksData[m[2]][str(msg.mentions[0].id)] += float(m[1])
        except:
            self.stonksData[m[2]][str(msg.mentions[0].id)] = float(m[1])
        self.stonksData[m[2]][str(msg.author.id)] += 0 - float(m[1])
        await msg.channel.send(':white_check_mark: sent!')
    else:
        await msg.channel.send(':x: invalid amount dummy thicc')

async def listTokens(self, msg, m):
    await msg.channel.send('the tokens that exist are: `'+'`, `'.join(list(self.stonksData.keys()))+'`.')

async def nuke(self, msg, m):
    t = m.pop(0)
    if self.stonksData[t][msg.author.id] == 100000:
        self.stonksData.pop(t)
        await msg.channel.send(':white_check_mark: removed!')
    else:
        await msg.channel.send(':x: you must own all of a token to delete it')

async def tokenBal(self, msg, m):
    if len(m) == 1:
        try:
            if m[0] == '*':
                a=''
                for i in [s for s in self.stonksData if str(msg.author.id) in self.stonksData[s]]:
                    a = a + "`{}`: `{}`, ".format(i, self.stonksData[i][str(msg.author.id)])
                await msg.channel.send('All your balances: {}'.format(a[:-2]))
                return
            await msg.channel.send('your balance of `{}` is `{}`.'.format(m[0], self.stonksData[m[0]][str(msg.author.id)]))
        except:
            await msg.channel.send('you have no `{}`.'.format(m[0]))
    else:
        try:
            await msg.channel.send("`{}`'s balance of `{}` is `{}`.".format(msg.mentions[0], m[1], self.stonksData[m[1]][str(msg.mentions[0].id)]))
        except:
            await msg.channel.send('`{}` has no `{}`.'.format(msg.mentions[0], m[1]))

cmds = {
    "create": createToken,
    "send": sendToken,
    "tip": sendToken,
    "tokens": listTokens,
    "bal": tokenBal,
    "balance": tokenBal,
    "nuke": nuke
}

async def parseCommand(self, msg, args):
    args = args.split()
    cmd = args.pop(0)
    if cmd in cmds:
        await loadJson(self)
        await cmds[cmd](self, msg, args)
        await writeJson(self)
    else:
        await msg.channel.send("available subcommands:\n create, send, tokens, balance")
    

async def init(self):
    await self.registerCommand(parseCommand, 'eco', 'eco help', 'a nice virtual economy to distribute virtual tokens')

