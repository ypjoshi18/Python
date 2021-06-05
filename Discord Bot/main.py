import discord
import os
from dotenv import load_dotenv
import pandas_datareader as web

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def get_stock_price(ticker):
    data = web.DataReader(ticker, "yahoo")
    return data['Close'].iloc[-1]

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Abe jaldi bol...Kal subah panvel nikalna hai")
    if message.content == 'private':
        await message.author.send("ohh private")
    if message.content.startswith("Stockprice"):
        if len(message.content.split(" ")) == 2:
            ticker = message.content.split(" ")[1]
            price = get_stock_price(ticker)
            await message.channel.send(f"Stock price of {ticker} is {price} ")


@client.event
async def on_connect():
    print("Connected to Server!!")
    channel = client.get_channel(719148204326912093)
    await channel.send("Bhai aaya hai .... Batake Jayega!!")

@client.event
async def on_member_join(member):
    await member.send(f"Kya re {member} ...Tere baap ki shadi hai kya idhar")
    # await member.create_dm()
    # await member.dm_channel.send(f"Kya re {member} ...Tere baap ki shadi hai kya idhar")
    # await message.channel.send("Abe jaldi bol...Kal subah panvel nikalna hai")

client.run(TOKEN)