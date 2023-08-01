import logging
import botpy.message
from functions import on_fullmatch, on_startswith
import var


@on_fullmatch('nya')
async def func1():
    print('cool')
    await var.client.api.post_message(channel_id=var.channel_id, content='test finished! Nya!')


@on_startswith('/')
async def func2():
    print('')
    with open(r'C:\Users\DELL\Desktop\00000\123456.txt', 'w') as f:
        f.write('cool')

