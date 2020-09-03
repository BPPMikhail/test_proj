import random


def get_random_word_test():
    print(game.get_random_word())
    print(game.get_random_word())
    print(game.get_random_word())


def guess_letter_test():
    print('The test of the method guess_letter begin...')
    test_letter = game.get_random_word()[0]
    game.guess_letter(test_letter)
    print('#Test 1 was successful.' if game.allowed_attempts == difficult_games else '#Test 1 failed.')
    game.guess_letter('')
    print('#Test 2 was successful.' if game.allowed_attempts == difficult_games - 1 else '#Test 2 failed.')


class Game:

    def __init__(self, allowed_attempts: int):
        self.__allowed_attempts = allowed_attempts
        self.__game_word = []
        self.__player_word = []

    def get_random_word(self):
        """
        The method reads data-file and returns random word from data-file.
        :return: type:list; random word.
        """
        with open('data/WordsStockRus.txt', 'r', encoding='utf8') as file:
            lines = file.readlines()
        self.__game_word = list(lines[random.randint(0, 11650)].strip())
        return self.__game_word

    def guess_letter(self, letter: str):
        """
        The method gets a letter and checks for its presence in the hidden word.
        If player took mistake, then the number of allowed attempts will decrease.
        :param letter: type:str; Player letter.
        """
        self.__player_word.append(letter)
        if letter not in self.__game_word:
            self.__allowed_attempts -= 1

    @property
    def allowed_attempts(self):
        return self.__allowed_attempts


difficult_games = int(input('Enter the number of available attempts: '))

game = Game(difficult_games)


if __name__ == '__main__':
    get_random_word_test()
    guess_letter_test()
