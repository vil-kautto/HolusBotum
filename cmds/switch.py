import discord
async def switch(message, switch_state):
    switch_state = not switch_state
    if switch_state:
        on = discord.Embed(title='{} turned the switch on'.format(message.author))
        await message.channel.send(embed=on)
    else:
        off = discord.Embed(title='{} turned the switch off'.format(message.author))
        await message.channel.send(embed=off)