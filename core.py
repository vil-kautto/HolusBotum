import discord
from discord.ext import commands
from configparser import ConfigParser
from pathlib import Path
from cmds import *

settings = {}

# load 
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
        
    
@commands.command()
async def ip(message):
    await c_ip(message)

    
@commands.command()
async def millo(message):
    await c_millo(message)
    
def setup(client):
    client.add_command(ip)
    client.add_command(millo)
    

async def on_ready(self):
    print('\nLogged in as', self.user)
    print('Prefix: {}'.format(settings['prefix']))
    print('Volume: {}'.format(int(settings['volume'])*100))
    await self.load_modules()
    
load_settings()
client = commands.Bot(command_prefix=settings['prefix'])
setup(client)
client.run(settings['token'])

