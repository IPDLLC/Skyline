
async def permCheck(self, user):
    admRoles = [user.guild.get_role(655093753706709012)]
    return any(item in admRoles for item in user.roles)


