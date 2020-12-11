import random

code = [0,0,0,0]
correct_digits_and_position = 0
correct_digits_only = 0

def code_generator():
    """This function is meant to generate the 4-digit code."""

    global code

    for i in range(4):
        value = random.randint(1, 8)
        while value not in code:
            code[i] = value
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')

def get_user_input():
    """This function is to get the user input."""
    return input("Input 4 digit code: ")

def display_message(correct_digits_and_position,correct_digits_only ):
    """This function displays the Number of correct digits in correct place and Number of correct digits not in correct place."""
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))


# TODO: Decompose into functions
def run_game():
    code_generator()

    global correct_digits_and_position
    global correct_digits_only

    correct = False
    turns = 0
    while not correct and turns < 12:
        answer = get_user_input()
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        correct_digits_and_position = 0
        correct_digits_only = 0

        for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1

        display_message(correct_digits_and_position,correct_digits_only)
        turns += 1
       
        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns))
            
    print('The code was: '+str(code))
    
if __name__ == "__main__":
    run_game()
