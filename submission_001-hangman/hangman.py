#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    files = open(file_name, 'r')
    list = files.readlines()
    return list


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].replace("\n", '')
    word_as_list = list(word)
    random_index_letter = random.randint(0, len(word_as_list))
    letter = word_as_list[random_index_letter]
    print("Guess the word: " + word.replace(letter, '_'))
    return word



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    guess = input("\nGuess the missing letter: ")
    return guess
    return 'TODO'


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

