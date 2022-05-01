class Enemydown(Exception):
    def __init__(self, message, arg):
        self.arg = arg
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class GameOver(Exception):
    def __init__(self, message, *args):
        super().__init__(message)
        super().__init__(*args)
        self.message = message

    def __str__(self):
        return self.message
