import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
import keep_alive

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
#讀取Token
load_dotenv(dotenv_path="token.env")
TOKEN = os.getenv('DISCORD_TOKEN')
GUILDID_TOKEN = os.getenv('GUILDID_TOKEN')
#讀取字典
with open("item_dict.pkl", "rb") as tf:
  item_dict = pickle.load(tf)
wordlist = [word for word in item_dict]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)


# 當機器人完成啟動時
@bot.event
async def on_ready():
  print(f"目前登入身份 --> {bot.user}")


# 載入指令程式檔案
@bot.command()
async def load(ctx, extension):
  await bot.load_extension(f"cogs.{extension}")
  await ctx.send(f"Loaded {extension} done.")


# 卸載指令檔案
@bot.command()
async def unload(ctx, extension):
  await bot.unload_extension(f"cogs.{extension}")
  await ctx.send(f"UnLoaded {extension} done.")


# 重新載入程式檔案
@bot.command()
async def reload(ctx, extension):
  await bot.reload_extension(f"cogs.{extension}")
  await ctx.send(f"ReLoaded {extension} done.")


# 一開始bot開機需載入全部程式檔案
async def load_extensions():
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
  async with bot:
    await load_extensions()
    # 機器人的TOKEN
    await bot.start(TOKEN)


keep_alive.keep_alive()

# 確定執行此py檔才會執行
if __name__ == "__main__":
  asyncio.run(main())
