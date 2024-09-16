class MeException(Exception):
    """Общий класс исключения для скриптов"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Товар не может быть с нулевым количеством.'

    def __str__(self):
        return self.message

class ShellScriptEmpty(MeException):
    """Класс исключения при отсутствии кода скрипта"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Товар не может быть с нулевым количеством.'