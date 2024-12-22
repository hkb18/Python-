import random
from art import logo
# RULES
# cards pt >21 ...BUST(game over)
# KQJ = 10
# A = 1 or 11
# if dealer gets <16 from cards lesser than player..they should take 1 more card

# is_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


def play_game():

    print(logo)
    user_cards = []
    computer_cards = []
    is_gameover = False

    def deal_cards():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        """Take a list of cards and return the score calculated frm the cards"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, computer_score):
        if user_score > 21 and computer_score > 21:
            return "You went over. You lose 😤"
        if user_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Opponent went over. You win 😁"
        elif user_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"

    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    while not is_gameover:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards:{user_cards}, current score:{user_score}")
        print(f"    Computer's first card:{computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_gameover = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_gameover = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f" \n  Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
