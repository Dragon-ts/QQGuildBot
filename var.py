from botpy.types.message import Reference

import os

class Event:
    channel_id = None
    client = None
    user_id = None
    message_id = None
    message = None


async def msg(
        content: str = None,
        channel_id=Event.channel_id,
        embed=None,
        ark=None,
        message_reference=None,
        image: str = None,
        file_image=None,
        msg_id: str = None,
        event_id: str = None,
        markdown=None,
        keyboard=None):
    print(channel_id) # None why?????
    await Event.client.api.post_message(
        channel_id=channel_id,
        content=content,
        embed=embed,
        ark=ark,
        message_reference=message_reference if embed or ark or image or file_image or markdown or keyboard == None else None,
        image=image,
        file_image=file_image,
        msg_id=msg_id,
        event_id=event_id,
        markdown=markdown,
        keyboard=keyboard
    )

async def send(content:str):
    await msg(content=content, channel_id=Event.channel_id)

class MessageSegment:
    async def reply(content: str):
        await msg(content=content, channel_id=Event.channel_id,
                   message_reference=Reference(message_id=Event.message_id, ignore_get_message_error=True))
        
    async def at(content:str, reply:bool = None, pic:str = None):
        '''
        reply: 可默认不写，默认为不引用

        pic: 图片路径,如果有图片将无法使用reply
        '''
        await msg(
            content = f'<@{Event.user_id}> {content}',
            channel_id = Event.channel_id,
            message_reference=Reference(message_id=Event.message_id) if reply == True and pic == None else None,
            file_image = pic if pic != None and os.path.isfile(pic) == True else None
        )
