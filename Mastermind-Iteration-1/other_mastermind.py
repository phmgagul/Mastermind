import random

def run_game():
    """
    TODO: implement Mastermind code here 
    """

    correct_digits_in_correct_place = 0
    incorrect_digits_in_incorrect_place = 0
    guesses = 12
    code_list = []


    while len(code_list) != 4:
        number = random.randint(1, 8)
        if number not in code_list:
            code_list.append(number)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    print(code_list)
    while guesses != 0:

        correct_digits_in_correct_place = 0
        incorrect_digits_in_incorrect_place = 0
        user_input = input("Input 4 digit code: ")
        while len(user_input) != 4:
            print("Please enter exactly 4 digits.")
            user_input = input("Input 4 digit code: ")

        # print(code_list)0
        x = 0
        while x < len(code_list):
            if int(user_input[x]) == code_list[x]:
                correct_digits_in_correct_place += 1
            elif int(user_input[x]) in code_list:
                incorrect_digits_in_incorrect_place += 1
            x+=1

        print("Number of correct digits in correct place:    ",correct_digits_in_correct_place)
        print("Number of correct digits not in correct place:", incorrect_digits_in_incorrect_place)

        if correct_digits_in_correct_place !=4: 
            guesses -= 1
            print("Turns left:", guesses)
        elif correct_digits_in_correct_place == 4:
            code = ""
            for x in range(len(code_list)):
                code += str(code_list[x])
            print("Congratulations! You are a codebreaker!")
            print("The code was:", code)
            break


if __name__ == "__main__":
    run_game()
