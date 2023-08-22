from functions import on_fullmatch, on_startswith
import message
import random
from datetime import date


@on_startswith('nya')
async def func1():
	await message.send('hello')


@on_fullmatch('/')
async def func2():
	with open(r'C:\Users\DELL\Desktop\00000\123456.txt', 'w') as f:
		f.write('cool')


@on_fullmatch('/today')
async def _():
	rnd = random.Random()
	rnd.seed(int(date.today().strftime("%y%m%d")) + int(message.Event.user_id))
	lucknum = rnd.randint(0, 100)
	msg = f'您今日的幸运指数是{lucknum}'
	await message.send(msg)


@on_fullmatch('/reply')
async def reply():
	# await var.MessageSegment.at(content='123')
	await message.MessageSegment.at('nyaaaaa', pic=r'.\000.jpg')
	await message.MessageSegment.at('nyaa', True)
