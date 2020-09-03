

class Game:

    def __init__(self, allowed_attempts: int):
        self.__allowed_attempts = allowed_attempts

difficult_games = int(input('Enter the number of available attempts: '))

game = Game(difficult_games)
