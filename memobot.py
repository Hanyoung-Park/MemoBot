import discord
from discord.ext import commands
import json

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command()
async def memo(ctx, *, content):
    user_id = str(ctx.message.author.id)
    with open('memo.json', 'r') as f:
        data = json.load(f)
    if user_id not in data:
        data[user_id] = []
    data[user_id].append(content)
    with open('memo.json', 'w') as f:
        json.dump(data, f)
    await ctx.send('메모가 저장됨')

@client.command()
async def show_memo(ctx):
    user_id = str(ctx.message.author.id)
    with open('memo.json', 'r') as f:
        data = json.load(f)
    if user_id in data:
        memo_list = '\n'.join(data[user_id])
        await ctx.send(f'{ctx.message.author.name}의 메모:\n{memo_list}')
    else:
        await ctx.send('저장해둔 메모 없음')

# client.run('TOKEN')
