# HolusBotum
HolusBotum is a minimal discord bot with customizable commands.
This application project was started by Ville Kautto, who was tired of discord bots with too many unnecessary features an too little customization.

## About

*Developer note: This is a solo project, so there will no be regular updates.*

HolusBotum is a semi-modular self-hosted Discord music/utility bot written in Python using Rapptz's discord.py library.
This bot is not meant for regular users, as it requires at minimum the basic knowledge of python progamming language.

Libraries used
[Python](https://www.python.org "Python homepage") 3.5+,
[discord.py[voice]](https://github.com/Rapptz/discord.py) library.

The bot's main purpose is to play music, generate data or fetch data on command.
The bot also has other small utilities such as rolling a dice based on user input.

## TODO Features:
The following features are currently missing:
- Voice client commands (media player commands)
    - summon
    - leave
    - play
    - stop
    - volume control
    - skip
    - queue
- Add a setting for more dangerous commands (ip)
- Separate commands to their own files and remove unnecessary code form the core

## Usage:

**Options are found in /project-root/config**

Token must be added into options before starting the bot.

All necessary dependencies will be installed upon first startup.

You can run the bot as it is, or you can make custom commands yourself.

### Creating Custom Commands
Custom commands can easily be added to the bot, without messing much with the core code
The commands use discord.py's command framework, so knowing it's usage will greatly reduce the effort needed for adding new commands

**step by step guide:**
1. create a .py file in the cmds directory

2. write your command to the file

3. mark your new command in the __init__.py file so that the bot can access the command

4. add the following text for your command into core.py in the main directory, replace new_command with your custom command's name and add new parameters when needed

>@commands.command(name='new_command')
>async def _new_command(message):
>    await new_command(message)

5. add the folowing text to the load_commands() function
>client.add_command(_new_command)

Now you have a custom command, that can be used on a bot!

### Removing Custom Commands
Removing commands is also exremely easy.

If you want to remove commands from the bot, simply comment out the specific commands from core.py's load_commands function

