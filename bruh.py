import discord


client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("ping"):
        await message.channel.send("pong")

    if message.content.startswith("bruh"):
        if str(message.author) == "Blue Taffy#4218":
            await message.channel.send("fucking retard")
        if str(message.author) == 'bruin#4982':
            await message.channel.send("fucking retard")

    if str(message.channel) == "general" and message.content != "":
        await message.channel.purge(limit=1)


client.run('ODkwODEzNTIwNDc0Njc3Mjk5.YU1QvQ.rwfFKba9MgUF0x4hSAa_TMR-pXY')