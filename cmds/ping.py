
async def ping(message, latency):
    await message.channel.send(latency)