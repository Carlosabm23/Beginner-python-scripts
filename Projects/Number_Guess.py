import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("To High!")
    elif user_guess < actual_answer:
        print("Too low!")
    else:
        print(f"You got it! The number is {actual_answer}")




def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': \n ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,101)
    print(f"The correct answer is {answer}")


    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number. ")

    guess = 0
    while guess != answer:

        guess = int(input("Guess a Number: \n"))

        check_answer(guess,answer)
game()









