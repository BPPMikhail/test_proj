import random


def get_used_letters_test():
    print(f'Te test of the method get_used_letters begin...')
    test_letters = ['a', 'c', 'b', 'a']
    game.guess_letter(test_letters[0])
    print('#Test 1 was successful.' if game.get_used_letters() == ['a'] else '#Test 1 failed.')
    game.guess_letter(test_letters[1])
    print('#Test 2 was successful.' if game.get_used_letters() == ['a', 'c'] else '#Test 2 failed.')
    game.guess_letter(test_letters[2])
    print('#Test 3 was successful.' if game.get_used_letters() == ['a', 'b', 'c'] else '#Test 3 failed.')
    game.guess_letter(test_letters[3])
    print('#Test 4 was successful.' if game.get_used_letters() == ['a', 'b', 'c'] else '#Test 3 failed.')

class Game:

    def __init__(self, allowed_attempts: int):
        self.__allowed_attempts = allowed_attempts
        self.__game_word = []
        self.__player_word = []

    def get_random_word(self):
        """
        The method reads data-file and returns hidden random word from data-file.
        :return: type:list; random word.
        """
        with open('data/WordsStockRus.txt', 'r', encoding='utf8') as file:
            lines = file.readlines()
        self.__game_word = list(lines[random.randint(0, 11650)].strip())
        return self.__game_word

    def guess_letter(self, letter: str):
        """
        The method gets a letter and checks for its presence in the hidden word.
        If player makes mistake, then the number of allowed attempts will decrease.
        :param letter: type:str; Player letter.
        """
        self.__player_word.append(letter)
        if letter not in self.__game_word:
            self.__allowed_attempts -= 1

    def get_used_letters(self):
        return sorted(set(self.__player_word))

    @property
    def allowed_attempts(self):
        return self.__allowed_attempts


difficult_games = int(input('Enter the number of available attempts: '))

game = Game(difficult_games)

if __name__ == '__main__':
    get_used_letters_test()
