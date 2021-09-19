import discord
token = ""
client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged on as {client.user}")

@client.event
async def on_message(message):
    if "" in message.content.lower()
        await message.channel.send("")
client.run(token)