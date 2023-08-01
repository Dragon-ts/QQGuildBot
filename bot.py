import botpy
import yaml
from functions import on_startswith_options, on_fullmatch_options
from switch_case_decorator import SwitchCaseDecorator
from botpy.types.message import Message
import var


class MyClient(botpy.Client):
    async def on_at_message_create(self, message: Message):
        talk = message.content
        var.channel_id = message.channel_id
        var.client = self
        talk = str(talk).replace(f'<@!{self.robot.id}> ', '')  # 去除@bot前缀
        decorator = SwitchCaseDecorator(on_startswith_options, on_fullmatch_options)
        await decorator.match_sequence(talk)


with open('config.yml', 'r', encoding='utf-8') as yml:
    yml = yaml.load(yml, yaml.FullLoader)['account']
    appid = yml['app-id']
    token = yml['token']
client = MyClient(intents=botpy.Intents(public_guild_messages=True))
client.run(appid=appid, token=token)
print(123)
