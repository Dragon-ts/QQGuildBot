from functions import on_fullmatch, on_startswith
import var


@on_fullmatch('hello')  # 当消息只是hello时执行下边的函数
async def hello():
    await var.send('hello')  # 发送普通信息
    await var.MessageSegment.reply('hello')  # 发送回复信息
    await var.MessageSegment.at('hello')  # 发送@信息


@on_startswith('good')  # 当消息开头为good时执行下边的函数
async def good():
    await var.send(var.Event.channel_id)  # Event内置了一些消息变量可供使用
