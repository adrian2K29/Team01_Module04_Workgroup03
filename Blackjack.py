import random
import art

card_values = {
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}

face_cards = {"Jack", "Queen", "King"}

cards = ("Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King")

def rule(x, y):
    return x + y


def check(x, y):
    if x > y:
        return "you win \n"
    elif x < y:
        return "you lose \n"
    else:
        return "push \n"


def card_value(card):
    if card in face_cards:
        return card_values[card]
    elif card == "Ace":
        return card_values["Ace"]
    return card

def blackjack():

    player_hand = []
    cpu_hand = []
    
    game = True

    for x in range(2):
        player_hand.append(random.choice(cards))
    
    player_count = sum(card_value(card) for card in player_hand)

    for x in range(2):
        cpu_hand.append(random.choice(cards))

    cpu_count = sum(card_value(card) for card in cpu_hand)

    print(art.logo)

    while game:
        if player_count < 21:
            print("\n")
            print(f"Your hand: {player_hand}, current score: {player_count}")
            print(f"Cpu's 1st card: {cpu_hand[0]}")
            turn = input("type 'y' to hit, type 'n' to stay: ")
            if turn == 'n':
                while cpu_count <= 16:
                    cpu_hand.append(random.choice(cards))
                    cpu_count += card_value(cpu_hand[-1]) #error
                print(f"CPU hand:{cpu_hand}, score: {cpu_count}")
                game = False
            else:
                player_hand.append(random.choice(cards))
                player_count += card_value(player_hand[-1]) #error
        elif player_count == 21:
            print(player_hand)
            print(player_count)
            game = False
        else:
            if "Ace" in player_hand:
                player_hand.remove("Ace")
                player_hand.append(1)
                player_count -= 10
            else:
                print(player_hand)
                print(player_count)
                game = False

    player_bust = int(player_count > 21)
    cpu_bust = int(cpu_count > 21)

    if player_bust & cpu_bust:
        print("push \n")
    elif player_bust:
        print("bust \n")
    elif cpu_bust:
        print("win \n")
    else:
        bout = check(player_count, cpu_count)
        print(bout)

    black()

def black():
    player_input = input("would you like to play black-jack? ").lower()
    if player_input == 'y':
        print("\n" * 20)
        blackjack()

blackjack()
