from art import logo
import random
import os

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
computer_hand = []


def draw_card(hand):
    hand.append(random.choice(deck))


def init_game():
    draw_card(player_hand)
    draw_card(player_hand)
    draw_card(computer_hand)
    draw_card(computer_hand)


def over_21(hand):
    if sum(hand) > 21:
        return True
    return False


def hit_computer_until_17():
    while sum(computer_hand) < 17:
        draw_card(computer_hand)
        check_ace_and_replace(computer_hand)


def check_ace_and_replace(hand):
    while over_21(hand):
        if 11 in hand:
            hand.remove(11)
            hand.append(1)
        else:
            break


def print_hands(start=False, end=False):
    if start:
        print(f"    Your cards: {player_hand}, current score: {sum(player_hand)}")
        print(f"    Computer's cards: [{computer_hand[0]},_]")
    if end:
        print(f"    Your final hand: {player_hand}, final score: {sum(player_hand)}")
        print(f"    Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")


def check_black_jack(hand, text=""):
    if sum(hand) == 21:
        print(f"{text} with Blackjack")
        return False
    return True


def check_winner():
    print_hands(end=True)
    if sum(player_hand) > sum(computer_hand):
        print("You win!")
    elif sum(player_hand) < sum(computer_hand):
        print("You lose!")
    else:
        print("Its a draw!")
    return


def game():
    os.system("cls")
    user_plays = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    player_hand.clear()
    computer_hand.clear()
    if user_plays == "y":
        init_game()
        print(logo)
        print_hands(start=True)
        continue_playing = check_black_jack(player_hand, "You win")
    else:
        return

    while continue_playing:
        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if hit == "y":
            draw_card(player_hand)
            if over_21(player_hand):
                check_ace_and_replace(player_hand)
            print_hands(start=True)
            if over_21(player_hand):
                print_hands(start=True)
                print("You went over. You lose :'(")
                break
        else:
            if sum(player_hand) != 21:
                continue_playing = check_black_jack(computer_hand, "You lose, opponent")
                if not continue_playing:
                    break
            hit_computer_until_17()
            if over_21(computer_hand):
                print_hands(end=True)
                print("Opponent went over. You win :D")
                break
            check_winner()
            break
    game()


if __name__ == "__main__":
    game()
