async def millo(message):
    data = '{}, koht'.format(message.author.mention)
    await message.channel.send(data)
