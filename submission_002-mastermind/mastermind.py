import random

def run_game():    
#get random numbers
    digits = []
    # random_digit = random.randint(1,8)
    '''
    while len(digits) != 4:
        x = digits.append(random.randint(1,8))
        if x in digits:
            continue '''
    a = random.randint(1,8)
    b = random.randint(1,8)
    c = random.randint(1,8)
    d = random.randint(1,8)

    digits = [a, b, c, d]

        # digits == [x]    
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    #get user input and make sure that there are no 9's and 0's and the number of digits should be 4
    lives = 12
    
    while lives > 0:
        while True:
            try:
                guess = input("Input 4 digit code: ")
            except EOFError:
                print("")
                # guess = ['0', '0', '0', '0']   
                # #convert list to string
                # guess_str = ' '.join(guess)
            if guess.isdigit() == False:
                print("Please enter exactly 4 digits.")
                continue
            else:
                pass
            if len(guess) != 4 or '9' in str(guess) or '0' in str(guess):
                print("Please enter exactly 4 digits.")
                continue
            break        

    #guesses = str(list(guess))
            
        countA = 0 #to check if the number is in the awnser
        countB = 0 #to check if the number is in the right place
        #check the number of digit in the correct place or not       
        for m,t in enumerate(digits):
            if int(guess[m]) == t:
                countA += 1
            elif str(t) in guess:
                countB += 1
        print("Number of correct digits in correct place:    ",countA)
        print("Number of correct digits not in correct place:",countB)        
        
        answer = " "
        for A1 in digits:
            answer = answer + str(A1)
        if countA == 4:
            print("Congratulations! You are a codebreaker!")
            print(f'The code was:{answer}')
            break

        lives -= 1
        print("Turns left:", lives)    
        if lives == 0:
            print("Game Over")
            


if __name__ == "__main__":
    run_game()
