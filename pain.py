import discord
token = "ODE5OTc5Njk2MTU4NjcwODgx.YEufmg.oWiiCeZKF3qJPkJo09sqSLyHQhc"
client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged on as {client.user}")

@client.event
async def on_message(message):
    if "neil" in message.content.lower() or await message.guild.fetch_member(436904563564347412) in message.mentions or "fake" in message.content.lower():
        await message.channel.send("https://cdn.discordapp.com/attachments/805527226161299527/819984791897505792/unknown.png")
    if "sam" in message.content.lower() or "horny" in message.content.lower() or await message.guild.fetch_member(487699426836742144) in message.mentions or await message.guild.fetch_member(761898330346618901) in message.mentions:
        await message.channel.send("https://cdn.discordapp.com/attachments/805527226161299527/822941891410001921/image0.jpg")
    if "triangle" in message.content.lower() or "alex" in message.content.lower() or await message.guild.fetch_member(421775792775888899) in message.mentions or await message.guild.fetch_member(697944038749241457) in message.mentions:
        await message.channel.send("https://cdn.discordapp.com/attachments/543115468718997524/819995620386668594/IMG_20210312_175329.jpg")
client.run(token)
