'''
async def exhaust(message):
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('testing.mp3'), after=lambda e: print('done', e))
'''
#https://www.youtube.com/watch?v=_RfwNRf04Oo