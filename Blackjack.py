import random
import art

cards = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)

def rule(x, y):
    return x + y

def check(x, y):
    if x > y:
        return "you win \n"
    elif x < y:
        return "you lose \n"
    else:
        return "push \n"

def blackjack():

    player_hand = []
    cpu_hand = []
    
    game = True

    for x in range(2):
        player_hand.append(random.choice(cards))
    
    player_count = rule(player_hand[0],player_hand[1])

    for x in range(2):
        cpu_hand.append(random.choice(cards))

    cpu_count = rule(cpu_hand[0],cpu_hand[1])

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
                    cpu_count = rule(cpu_count, cpu_hand[-1])
                print(f"CPU hand:{cpu_hand}, score: {cpu_count}")
                game = False
            else:
                player_hand.append(random.choice(cards))
                player_count = rule(player_count, player_hand[-1])
        elif player_count == 21:
            print(player_hand)
            print(player_count)
            game = False
        else:
            if 11 in player_hand:
                player_hand.remove(11)
                player_hand.append(1)
            else:
                print(player_hand)
                print(player_count)
                game = False

    if player_count > 21 and cpu_count > 21:
        print("push \n")
    elif player_count > 21 and not cpu_count > 21:
        print("bust \n")
    elif not player_count > 21 and cpu_count > 21:
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
