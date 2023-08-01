import botpy
import yaml
from functions import on_startswith_options, on_fullmatch_options
from switch_case_decorator import SwitchCaseDecorator
from botpy.types.message import Message


class MyClient(botpy.Client):
    async def on_at_message_create(self, message: Message):
        talk = message.content
        talk = str(talk).replace(f'<@!{self.robot.id}> ', '')  # 去除@bot前缀
        print(talk)
        decorator = SwitchCaseDecorator(on_startswith_options, on_fullmatch_options)
        await decorator.match_sequence(talk)


with open('config.yml', 'r', encoding='utf-8') as f:
    data = f.read()
yml = yaml.load(data, yaml.FullLoader)['account']
appid = yml['app-id']
appkey = yml['app-key']
token = yml['token']

intents = botpy.Intents(public_guild_messages=True)
client = MyClient(intents=intents)
client.run(appid=appid, token=token)
