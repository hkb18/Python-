from art import logo, vs
import random
from game_data import data


# Score Keeping.

# Make game repeatable.

# Make B become the next A.


def get_random_account():
    """ Get data from random account """
    return random.choice(data)


def check_answer(guess, a_followers, b_followers):
    """ Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong. """
    if a_followers > b_followers:
        return guess == "A"
    # if guess=="A":
    # return True
    # else:
    # False
    else:
        return guess == "B"


def game():

    score = 0
    game_should_continue = True
    account_b = get_random_account()

    while game_should_continue:
        print(logo)
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = random.choice(data)

        def format_account(account):
            """ Format account into printable format: name, description and country """
            account_name = account["name"]
            account_descr = account["description"]
            account_country = account["country"]
            return f" {account_name}, a {account_descr}, from {account_country}"

        print(f"Compare A: {format_account(account_a)}.")
        print(vs)
        print(f"Compare B: {format_account(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        if is_correct:
            score += 1
            print(f"YOUR RIGHT.🎉 Current Score is {score}\n")
        else:
            print(f"YOUR WRONG....!!!!💀💀 Final Score is {score}")
            game_should_continue = False


game()
