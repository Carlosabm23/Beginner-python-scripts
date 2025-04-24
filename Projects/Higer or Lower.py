import art
import random
from game_data import data


def format_data(account):
    """Returns a nicely formatted string with account info."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Returns True if guess is correct, else False."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

# Main game loop
def game():
    print(art.logo)
    score = 0
    game_should_continue = True
    account_a = random.choice(data)
    account_b = random.choice(data)

    # Make sure starting accounts are different
    while account_a == account_b:
        account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        while True:
            account_b = random.choice(data)
            if account_b != account_a:
                break

        print(f"\nCompare A: {format_data(account_a)}")
        print(art.logo_3)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["Follower_count"]
        b_follower_count = account_b["Follower_count"]
        name_a = account_a["name"]
        name_b = account_b["name"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"\n✅ You are correct! Current score: {score}")
        else:
            print(f"\n❌ Sorry, that's wrong.")
            print(f"{name_a} had {a_follower_count} followers. {name_b} had {b_follower_count} followers.")
            print(f"Final score: {score}")
            game_should_continue = False

game()

































# def score_(user_answer,correct_answer,score):
#     if user_answer == correct_answer:
#         return score -1
#
#
#
# def game():
#     score = 1
#     while score == 1:
#         print("\n")
#         number1 = random.randint(0,100)
#         number2 = random.randint(0,100)
#         print(f"Which number is bigger {number1} or or {number2} ?")
#         answer = int(input("Which is Bigger? \n"))
#         if  number1 > number2 :
#             correct = number1
#         elif number2 > number1:
#             correct = number2
#         else:
#             print("You are wrong")
#
#         if answer == correct:
#             print(f"You are correct {answer} is the bigger number")
#         else:
#             print(f"Sorry {correct} was the bigger number")
#         score_(answer,correct,score)
#         if score == 0:
#             print("Over")
#
# game()









