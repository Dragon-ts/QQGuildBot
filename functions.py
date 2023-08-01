on_fullmatch_options = {}
on_startswith_options = {}

class on_fullmatch:
    def __init__(self, option):
        self.option = option

    def __call__(self, func):
        on_fullmatch_options[self.option] = func
        return func


class on_startswith:
    def __init__(self, option):
        self.option = option

    def __call__(self, func):
        on_startswith_options[self.option] = func
        return func

custom_functions_globals = {}
exec(open("command.py").read(), custom_functions_globals)
for func_name, func in custom_functions_globals.items():
    if callable(func):
        custom_functions_globals[func_name] = func
