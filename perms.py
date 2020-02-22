
async def permCheck(self, user):
    admRole = user.guild.get_role(680757446821937297)
    return admRole in user.roles


