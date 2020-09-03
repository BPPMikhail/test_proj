import random


def get_random_word_test():
    print(game.get_random_word())
    print(game.get_random_word())
    print(game.get_random_word())


class Game:

    def __init__(self, allowed_attempts: int):
        self.__allowed_attempts = allowed_attempts
        self.__game_word = []

    def get_random_word(self):
        """
        The method reads data-file and returns random word from data-file.
        :return: type:list; random word.
        """
        with open('data/WordsStockRus.txt', 'r', encoding='utf8') as file:
            lines = file.readlines()
        self.__game_word = list(lines[random.randint(0, 11650)].strip())
        return self.__game_word


difficult_games = int(input('Enter the number of available attempts: '))

game = Game(difficult_games)


if __name__ == '__main__':
    get_random_word_test()
