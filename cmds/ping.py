
async def ping(ctx):
    ctx.channel.send('Bot Latency: ' + client.latency())