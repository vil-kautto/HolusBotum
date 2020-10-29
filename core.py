import discord
from discord.ext import commands
from configparser import ConfigParser
from pathlib import Path
from cmds import *

settings = {}

# load settings amd print details to console
def load_settings():
    config = ConfigParser()
    config.read('options.ini')
    settings['token'] = config.get('settings','token')
    print('Token: {}'.format(settings['token']))
    settings['prefix'] = config.get('settings','prefix')
    print('Prefix: {}'.format(settings['prefix']))
    settings['volume'] = config.get('settings','default_volume')
    print('Volume: {}'.format(settings['volume']))
    
def load_modules():
    print('\nLoading modules...')
    cmds_dir = Path('./cmds').rglob('*.py')
    modules = [x for x in cmds_dir]
    for file in modules:
        print('Loaded module: {}'.format(file))
        
        
# this next section is dedicated for commands in 'cmds' directory
@commands.command(name='ip')
async def _ip(message):
    await ip(message)

    
@commands.command(name='millo')
async def _millo(message):
    await c_millo(message)
    
def load_commands(client):
    client.add_command(_ip)
    #client.add_command(_millo)
    
load_settings()
client = commands.Bot(command_prefix=settings['prefix'])
load_commands(client)
client.run(settings['token'])

