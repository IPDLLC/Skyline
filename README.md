![Skyline](https://ipdllc.github.io/assets/skyline.png)

Skyline is a easy to use and customizable moderation bot for your discord server.

Don't forget to read the [license](LICENSE)

# Setup
## Use our bot
- go to this [oauth link](https://discordapp.com/oauth2/authorize?client_id=679066447942516760&scope=bot&permissions=8) to add it to your server!
## Self host our bot
- use linux windows bad
- download the latest stable release of Skyline (don't git clone, there may be bugs lurking!)
- make a config.py file with the content:
```
botToken="<your token here>"
botOwner=<your user ID>
blacklistedUsers=[<ids of people not allowed to use the bot>]
```
- install the dependencies, you need python, and some python librarys including discord.py
- do `./runBot.sh` to start the bot
## If we do make another stable release, just download the newest release and keep your config file.

