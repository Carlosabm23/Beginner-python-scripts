import random
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



def check_answer(user_guess, actual_answer,turns):
    """ chescks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("To High!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it! The number is {actual_answer}")




def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    # else:
    #     print("please pick 'easy or 'hard'!")

def game():
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,101)
    print(f"The correct answer is {answer}")


    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number. ")

        guess = int(input("Guess a Number: \n"))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print(f"Game over, the number was {answer}")
            return
        elif guess != answer:
            print("Guess again")
game()









