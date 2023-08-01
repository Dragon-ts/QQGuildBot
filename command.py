import logging
from botpy.types.message import Message
import botpy
from Program.Python.EnderDragonGuild.bot import MyClient
from botpy.client import BotAPI
from functions import on_fullmatch, on_startswith


@on_fullmatch('nya')
async def func1():
    print('cool')


@on_fullmatch('/test')
async def func3():
    print(123)
    await MyClient(intents=botpy.Intents(public_guild_messages=True)).api.post_message(
        channel_id=message.channel_id,
        content=f"test finished"
    )


@on_startswith('/')
async def func2():
    with open(r'C:\Users\DELL\Desktop\00000\123456.txt', 'w') as f:
        f.write('cool')
