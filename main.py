import asyncio
import cordic
from cordic import Client, Intents

client = Client(intents=Intents.all())


@client.event
async def on_ready(event):
    print("Bot is ready")


@client.event
async def message_create(msg: cordic.Message):

    if msg.content.startswith("test"):
        await msg.send("it works fine")

client.run("TOKEN")

