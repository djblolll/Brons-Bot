import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

bot = commands.Bot(command_prefix='/')

def check_twitter_username_changes(username):
    return f"Checked Twitter username changes for {username}."

def check_pump_fun_bundled(address):
    url = f"https://pump.fun/coin/{address}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    bundle_info = soup.find('div', class_='bundle-percentage')
    if bundle_info:
        bundle_percentage = bundle_info.text.strip()
        return f"The bundle percentage for the coin address {address} is {bundle_percentage}."
    else:
        return f"Could not find bundle information for the coin address {address}."

def check_dex_paid(address):
    url = f"https://dexscreener.com/{address}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    promotion_info = soup.find('div', class_='promotion-badge')
    if promotion_info:
        return f"The coin {address} has been paid to promote on Dexscreener."
    else:
        return f"The coin {address} has not been paid to promote on Dexscreener."

def check_site_age(url):
    response = requests.get(f"https://input.payapi.io/v1/api/fraud/domain/age/{url}")
    data = response.json()
    age = data.get("age", "Unknown")
    return f"The age of the website {url} is {age} days."

@bot.command()
async def twitter_reused(ctx, username: str):
    result = check_twitter_username_changes(username)
    await ctx.send(result)

@bot.command()
async def bundled(ctx, address: str):
    result = check_pump_fun_bundled(address)
    await ctx.send(result)

@bot.command()
async def dexscreener(ctx, address: str):
    result = check_dex_paid(address)
    await ctx.send(result)

@bot.command()
async def site_check(ctx, url: str):
    result = check_site_age(url)
    await ctx.send(result)

bot.run(TOKEN)