import random


def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])


def score(cards):
    my_score = 0
    count = 0
    flag = False
    for card in cards:
        if card[0] == 'Ace':
            flag = True
            count += 1
        my_score += card_value(card)
    if my_score > 21 and flag:
        my_score = my_score - 10 * count
    print(f"Cards:", cards)
    print(f"Score: ", my_score)
    print("\n")
    return my_score


def check_winner(dealer_score, player_score):
    if dealer_score > 21:
        print("Player wins (Dealer Loss Because Dealer Score is exceeding 21)")
    elif player_score > dealer_score:
        print("Player wins (Player Has High Score than Dealer)")
    elif dealer_score > player_score:
        print("Dealer wins (Dealer Has High Score than Player)")
    elif player_score == 21:
        print("You won!")
    elif player_score == dealer_score != 21:
        print("The dealer won.")


def blackjack():
    card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = [(card, category) for category in card_categories for card in cards_list]

    random.shuffle(deck)
    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]

    while True:
        print('For player:')
        player_score = score(player_card)

        if player_score > 21:
            print("Dealer wins (Player Loss Because Player Score is exceeding 21)")
            print('\n')
            break
        if player_score == 21:
            print("you won!")
            break

        choice = input('What do you want? ["play" to request another card, "stop" to stop]: ').lower()
        if choice == "play":
            new_card = deck.pop()
            player_card.append(new_card)
        elif choice == "stop":
            print('For dealer:')
            dealer_score = score(dealer_card)
            print("Dealer must play at 16 and stop at 17.")
            while dealer_score <= 16:
                new_card = deck.pop()
                dealer_card.append(new_card)
                dealer_score = score(dealer_card)
            check_winner(dealer_score, player_score)
            break
        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == '__main__':
    blackjack()