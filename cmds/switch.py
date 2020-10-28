
async def switch(ctx):
    global theSwitch
    theSwitch = not theSwitch
    if theSwitch:
        on = discord.Embed(title='{} turned the switch on'.format(ctx.author))
        await ctx.channel.send(embed=on)
    else:
        off = discord.Embed(title='{} turned the switch off'.format(ctx.author))
        await ctx.channel.send(embed=off)