import os
from discord.ext import commands
from summarizer import Summarizer
from dotenv import load_dotenv


load_dotenv()
DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def oneline(ctx, arg):
    limit_number = int(arg) + 1
    messages = await ctx.history(limit=limit_number).flatten()
    message_contents = list(reversed([message.content for message in messages]))[:-1]

    summarizer = Summarizer()
    summarized_str = summarizer.summarize(message_contents)

    await ctx.send(f'한 줄 요약: `{summarized_str}`')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        
    	await ctx.send("잘못된 명령어 입니다. `!oneline <현재 메시지로부터 한줄 요약하기 위해 불러올 메시지 수>` 으로 한 줄 요약을 시작하세요.")

bot.run(DISCORD_BOT_TOKEN)
