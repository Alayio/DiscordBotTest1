import discord
from discord.ext import commands
import datetime

#金幣島, 每三天發生一次, 離當前最近的五個時間(11,13,15,17,21,23)

# 定義名為 SetChannelTopic 的 Cog
class SetChannelTopic(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        if message.content == "虎":

            target_times = [11, 13, 15, 19, 21]  # 目標時間列表
            num_events = 5  # 事件數量

            # 計算最近的五個事件日期並生成時間戳
            timestamps = []
            current_date = datetime.date(2023, 9, 19)  # 起始日期

            while len(timestamps) < num_events:
                for target_time in target_times:
                    event_datetime = datetime.datetime.combine(current_date, datetime.time(target_time, 0))
                    if event_datetime >= datetime.datetime.now():
                        timestamps.append(event_datetime.timestamp())
                    if len(timestamps) >= num_events:
                        break
                current_date += datetime.timedelta(days=3)

            # 轉換時間戳為指定格式
            formatted_timestamps = '金幣島 ' + ' '.join(f'<t:{int(timestamp)}:R>' for timestamp in timestamps)

        channel = message.channel
        await channel.edit(topic=formatted_timestamps)


    

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(SetChannelTopic(bot))