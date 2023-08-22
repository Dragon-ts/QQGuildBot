import asyncio
import traceback

from functions import on_fullmatch_options, on_startswith_options


class SwitchCaseDecorator:
    def __init__(self, on_startswith_options, on_fullmatch_options):
        self.startswith_options = on_startswith_options
        self.fullmatch_options = on_fullmatch_options

    def on_startwith_switch_case(self, on_startswith):
        async def decorator(func):
            self.startswith_options[on_startswith] = func
            return func

        return decorator

    def on_fullmatch_switch_case(self, on_fullmatch):
        async def decorator(func):
            self.fullmatch_options[on_fullmatch] = func
            return func

        return decorator

    async def match_sequence(self, sequence):
        matched = False
        # print(self.fullmatch_options)
        # print(self.startswith_options)
        if sequence in self.fullmatch_options:
            # print('sequence in self.fullmatch_options')
            await self.fullmatch_options[sequence]()
            matched = True
        if not matched:
            for on_startswith, func in self.startswith_options.items():
                # print('on_startswith, func in self.startswith_options.items()')
                if sequence.startswith(on_startswith):
                    await func()
                    matched = True
                    break
