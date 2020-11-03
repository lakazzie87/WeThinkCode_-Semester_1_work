import random


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    try:
       return input("Guess the missing letter: ")
    except:
        EOFError


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name

def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = str(words[random_index]).strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    x = random.randint(0, len(word)-1)
    letter = word[x]
    new_list = list()
    for i in word:
        if i == letter:
            new_list.append(i)
        else:
            new_list.append('_')
    return ''.join(new_list)
    #return(new_list)    



# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):

    if char in str(original_word) and str(char) not in str(answer_word):
        return True
    else:    
        return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    list_original_word = list(original_word)
    #print(list_original_word)
    count = 0
    for x in range(len(original_word)):
        if answer_word[x] == "_" and original_word[x] == char:
            answer_word = answer_word.replace(answer_word[x], char, 1)
    #for x in list_original_word:
    #   if x == char:
    #        x = answer_word[count].replace(answer_word[x], char,1)
    #        print(x)
        count = count + 1
    return answer_word  


def do_correct_answer(original_word, answer, number_guesses):
    answer = fill_in_char(original_word, answer, number_guesses)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    pass
    if number_guesses == 4:
        print("/"+"-"*4)
        print("|\n"*3+"|")
        print("_"*7)
    elif number_guesses == 3:
        print("/"+"-"*4)
        print("|"+" "*3+"0")
        print("|\n"*3)
        print("_"*7)
    elif number_guesses == 2:
        print("/"+"-"*4)
        print("|"+" "*3+"0")
        print("|"+" "*2+"/"+" "+"\\")
        print("|\n"*2)
        print("_"*7)
    elif number_guesses == 1:
        print("/"+"-"*4)
        print("|"+" "*3+"0")
        print("|"+" "*2+"/|" +"\\")
        print("|"+" "*3 +"|")
        print("|")
        print("_"*7)
    elif number_guesses == 0:
        print("/"+"-"*4)
        print("|"+" "*3+"0")
        print("|"+" "*2+"/|"+"\\")
        print("|"+" "*3 +"|")
        print("|"+" "*2+"/ " +"\\")
        print("_"*7)
"""
    if number_guesses == 4:
        print("/---- \n| \n| \n| \n_______")
    elif number_guesses == 3:
        print("/---- \n|   0 \n| \n| \n| \n_______")
    elif number_guesses == 2:
        print("/---- \n|   0 \n|  /|\\ \n| \n| \n_______")
    elif number_guesses == 1:
        print("/---- \n|   0 \n|  /|\\ \n|   | \n| \n_______")
    elif number_guesses == 0:
        print("/---- \n|   0 \n|  /|\\ \n|   | \n|  / \\ \n_______")
"""  
# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):

    print("Guess the word:", ''.join(answer))
    number_guesses = 5
    list_word = list(word)
    while answer != list_word and number_guesses > 0:
        if word == answer:
            return
        char_guess = get_user_input()

        if char_guess == "exit" or char_guess == "quit":
            print("Bye!")
            return
       
        if is_missing_char(word, answer, char_guess):
            answer = do_correct_answer(word, answer, char_guess)
            print(''.join(answer))
        else:
            number_guesses = number_guesses - 1
            do_wrong_answer(answer, number_guesses)
            
    if number_guesses == 0:
        print("Sorry, you are out of guesses. The word was: " + word)
    else: 
        print("Winner!!!")
    return

# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    answer_word = random_fill_word(selected_word)
    #char = get_user_input()
    current_answer = random_fill_word(selected_word)
    run_game_loop(selected_word, current_answer)

