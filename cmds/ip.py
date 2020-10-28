import requests

async def ip(message):
    ip = requests.get("http://ipecho.net/plain?").text
    await message.channel.send(ip)