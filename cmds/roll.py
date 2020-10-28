async def roll(ctx, number):
    minimum = 0
    try:
        maximum = int(number)
        if minimum < maximum:
            rolled = discord.Embed(title='{} rolled {} on a scale of {}-{}'.format(ctx.author, random.randint(minimum, maximum), minimum, maximum))
            await ctx.channel.send(embed=rolled)
        elif minimum >= maximum:
            await ctx.channel.send('The number must be larger than 1')
        else:
            await ctx.channel.send('Something went wrong.')
    except ValueError:
        await ctx.channel.send('Invalid argument: Try sending a number next time.')