
warnFile = 'db/warns.txt'

async def noPerms(self, msg):
    await msg.channel.send(':x: **You do not have permission to do that**.')

async def infractions(self, msg, args):
    if await self.permCheck(msg.author):
        patt = str(msg.mentions[0].id)+"\t"
        f = open(warnFile, 'r')
        inf = f.readlines()
        uInf = ''
        f.close()
        for i in inf:
            if patt in i:
                uInf = uInf+i[len(patt):]
        await msg.channel.send(str(msg.mentions[0])+"'s **infractions**:\n"+uInf)
    else:
        await noPerms(self, msg)

async def warn(self, msg, args):
    if msg.author.guild_permissions.kick_members:
        args = args.split()
        try:
            toWarn = self.get_user(msg.mentions[0].id)
        except:
            toWarn = ''
        args = ' '.join(args)
        if not args:
            args = 'Unspecified'
        if toWarn:
            await toWarn.send('You were warned in **{}** for **{}**'.format(msg.author.guild.name, args))
            await msg.channel.send(':white_check_mark: **Warning** {} **for** {}'.format(toWarn, args))
            f = open(warnFile, 'a')
            f.write("\n"+str(toWarn.id)+"\t "+args)
            f.close()
        else:
            await msg.channel.send(':x: Sorry, **I cannot find that user**.') # we will try do this for everything soon dw peoples
    else:
        await noPerms(self, msg)

async def kick(self, msg, args):
    if msg.author.guild_permissions.kick_members:
        resp = msg.mentions[0]
        args = "{} ({})".format(args, str(msg.author))
        await resp.send('You were kicked in **{}** for **{}**'.format(msg.guild.name, args))
        await msg.guild.kick(resp, reason=args)
        await msg.channel.send(":white_check_mark: {} **has been kicked**.".format(str(resp)))
    else:
        await noPerms(self, msg)

async def ban(self, msg, args):
    if msg.author.guild_permissions.ban_members:
        resp = msg.mentions[0]
        args = "{} ({})".format(args, str(msg.author))
        await resp.send('You were banned in **{}** for **{}**'.format(msg.guild.name, args))
        await msg.guild.ban(resp, reason=args, delete_message_days=0)
        await msg.channel.send(":white_check_mark: {} **has been banned**.".format(str(resp)))
    else:
        await noPerms(self, msg)

async def gtfo(self, msg, args):
    if msg.author.guild_permissions.ban_members:
        resp = msg.mentions[0] 
        args = "{} ({})".format(args, str(msg.author))
        await resp.send('You were warned in **{}** for **{}**'.format(msg.guild.name, args))
        await msg.guild.ban(resp, reason=args, delete_message_days=7)
        await msg.channel.send(":white_check_mark: {} **has been banned and rolled back**.".format(str(resp)))
    else:
        await noPerms(self, msg)

async def purge(self, msg, args):
    if msg.author.guild_permissions.manage_messages:
        await msg.delete()
        if args:
            dell = await msg.channel.purge(limit=int(args))
        else:
            dell = await msg.channel.purge()
        await msg.channel.send(":white_check_mark: **Purged **{}** messages**.".format(str(len(dell))))
    else:
        await noPerms(self, msg)



async def init(self):
    await self.registerCommand(warn, 'warn', 'warn <user> [reason]', 'warn someone')
    await self.registerCommand(infractions, 'infractions', 'infractions <user>', 'see someones warnings')
    await self.registerCommand(kick, 'kick', 'kick <user> [reason]', 'kick a user from the server')
    await self.registerCommand(ban, 'ban', 'ban <user> [reason]', 'ban a user from the server')
    await self.registerCommand(gtfo, 'gtfo', 'gtfo <user> [reason]', 'ban and rollback for 1 day a user from the server')
    await self.registerCommand(purge, 'purge', 'purge [amount]', 'purge a text channel')


