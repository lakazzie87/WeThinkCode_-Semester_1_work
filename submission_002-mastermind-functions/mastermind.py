import random
# TODO: Decompose into functions
def generate_code():
    '''
    this function will generate a random 4 digit code
    :return: Unique 4 digit code
    '''
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    #code = [1,2,3,4]
    return code
    
    
    '''
    checks int input function and if it is valid
    :return: valid user input
    '''
def input_function_validation():
    #TODO check this out
    answer_exist = True 
    try:
        answer = input("Input 4 digit code: ").strip()
    except EOFError:
        answer = "0000"
        # print(f"Answer {answer} successfully!")
    #TODO: check individual indexes
    return answer

    
    '''
    function to check correct digit only
    '''
def validation(user_code):
    if len(user_code) != 4:
        print("Please enter exactly 4 digits.")
        return False
    elif not user_code.isdigit():
        print("Please enter exactly 4 digits.")
        return False
    else:
        return True
def check_correct_digi_pos(user_code, generated_code):
    correct_digits_and_position = 0
    list_index = 0
    for c in user_code:
        if int(c) == generated_code[list_index]:
            correct_digits_and_position += 1
        list_index += 1
    print(f"Number of correct digits in correct place:     {correct_digits_and_position}")
    return correct_digits_and_position


    '''
    Function to check correct digits and postion
    :return: correct position and digit
    '''
def correct_digit_only(user_code,generated_code):
    
    correct_digit = 0
    list_index = 0
    code = generated_code
    for v in user_code:
        if int(v) in generated_code:
            correct_digit += 1
    correct_pos = check_correct_digi_pos(user_code, generated_code)
    print(f"Number of correct digits not in correct place: {correct_digit - correct_pos}")
    return

    '''
    check if they won or not function
    :return: if user has won or lost
    '''
def winner_or_loser(genCode): 
    '''
        :param genCode: this is our code as the devs
        :param answer: this is thier code as the player
    '''
    turns = 0
    count = 0
    while turns < 12:
        our_answer = input_function_validation()
        if validation(our_answer) == False:
            turns -= 1
            continue
        count = 0
        i = 0
        for x in our_answer:
            if int(x) == genCode[i]:
                count += 1
            i += 1
        correct_digit_only(our_answer, genCode)
        if count == 4:
            #correct_digit_only(our_answer, genCode)
            print('Congratulations! You are a codebreaker!')
            break        
        else:
            #correct_digit_only(our_answer, genCode)
            print('Turns left: '+str((12 - turns) - 1))
            turns += 1    
    print('The code was: '+str(genCode))

def run_game():
    code = generate_code()
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    winner_or_loser(code)
    
if __name__ == "__main__":
    run_game()