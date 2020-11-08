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
    switch_state = True
    
def load_modules():
    print('\nLoading modules...')
    cmds_dir = Path('./cmds').rglob('*.py')
    modules = [x for x in cmds_dir]
    for file in modules:
        print('Loaded module: {}'.format(file))
        
        
# this next section is dedicated for commands in 'cmds' directory

# Used in server hosting within private circles
# Disable this in the load section, if you don't want people to find out your public ip
@commands.command(
    name='ip',
    brief="- Displays the host computer's ip",
    description="If the bot's owner hosts servers, use this command to get his public ip"
    )
async def _ip(message):
    await ip(message)

@commands.command(
    name='millo',
    brief='- Displays time based information',
    description='answers one of the most important questions ever existed'
    )
async def _millo(message):
    await millo(message)
    
@commands.command(
    name='roll',
    brief='- Rolls A dice',
    description='Rolls a die depending on the number of parameter numbers [0-2]'
    )
async def _roll(message, *numbers):
    if len(numbers) == 0:
        await roll(message)
    elif len(numbers) == 1:
        await roll_max(message, numbers[0])
    elif len(numbers) == 2:
        await roll_min_max(message, numbers[0], numbers[1])
    else:
        await roll_error(message)
    
@commands.command(name='switch', brief='Flips the switch')
async def _switch(message):
    await switch(message, switch_state)
    
@commands.command(
    name='ping',
    brief="- Displays bot's latency",
    description='Rolls a die depending on the number of parameter numbers [0-2]'
    )
async def _ping(message):
    latency = 'The bot latency is {:d}ms'.format(int(client.latency*1000))
    await ping(message, latency)
    
def load_commands(client):
    
    client.add_command(_ip)
    client.add_command(_millo)
    client.add_command(_roll)
    #client.add_command(_switch)
    client.add_command(_ping)
    
load_settings()
client = commands.Bot(command_prefix=settings['prefix'])
load_commands(client)
client.run(settings['token'])

