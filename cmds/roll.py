import random
import discord

async def roll(message):
    minimum = 1
    maximum = 20
    if minimum < maximum:
        rolled = discord.Embed(title='{} rolled {} on a scale of {}-{}'.format(message.author, random.randint(minimum, maximum), minimum, maximum))
        await message.channel.send(embed=rolled)
    else:
        await message.channel.send('Something went wrong.')

async def roll_max(message, maximum):
        minimum = 1
        maximum = int(maximum)
        if minimum < maximum:
            rolled = discord.Embed(title='{} rolled {} on a scale of {}-{}'.format(message.author, random.randint(minimum, maximum), minimum, maximum))
            await message.channel.send(embed=rolled)
        elif minimum >= maximum:
            await message.channel.send('The maximum number must be Larger than 1')
        else:
            await message.channel.send('Something went wrong.')

async def roll_min_max(message, minimum, maximum):
    minimum = int(minimum)
    maximum = int(maximum)
    if minimum < maximum:
        rolled = discord.Embed(title='{} rolled {} on a scale of {}-{}'.format(message.author, random.randint(minimum, maximum), minimum, maximum))
        await message.channel.send(embed=rolled)
    elif minimum >= maximum:
        await message.channel.send('The smaller number must be larger than maximum')
    else:
        await message.channel.send('Something went wrong.')
        
async def roll_error(message):
    await message.channel.send('Wrong amount of arguments. Give 0-2 numbers as arguments')