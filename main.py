import random
import art
print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def single_card(list):
    single_card = []
    num1 = random.randint(0,len(list)-1)
    single_card.append(list[num1])
    return single_card

def ace_con(hand):
    hand.remove(11)
    hand.append(1)
    return hand


def hit(current_hand):
    user_decision = input("Type 'y' to get another card, type 'n' to pass: \n")
    if user_decision == 'y':
        additional_card = single_card(cards)
        current_hand.extend(additional_card)
        current_total = sum(current_hand)
        print(f"Your cards: {current_hand}, current score: {current_total}\n")
        return current_total
    elif user_decision == 'n':
        return False

def dealer_hit(hand):
    dealer_total = sum(hand)
    while dealer_total <= 16:
        dealer_next_card = single_card(cards)
        hand.extend(dealer_next_card)
        dealer_total = sum(hand)
    if dealer_total > 21:
        print(f"Dealer's cards are {hand}, dealer bust with score {dealer_total}.\n You win!")
        return "done"
    elif dealer_total > 21 and 11 in hand:
        dealer_new_ace = ace_con(hand)
        dealer_total = sum(dealer_new_ace)
        return dealer_total
    elif dealer_total <= 21:
        print(f"Dealer's cards are {hand}, with score of {dealer_total}.")
        return dealer_total
    elif dealer_total == 21:
        print(f"Dealer hit Blackjack! You lose.\n")
        return "done"

keep_playing = True
while keep_playing == True:
    game_stop = False
    keep_dealing = True
    user_current_hand = single_card(cards)
    user_next_card = single_card(cards)
    user_current_hand.extend(user_next_card)
    user_total = sum(user_current_hand)
    if user_total == 21:
        game_stop = True
        print(f"You hit Blackjack! Congrats you win.")
    dealer_hand = single_card(cards)

    if game_stop == False:
        print(f"Your cards: {user_current_hand}, current score: {user_total}\n")
        print(f"Computer's first card: {dealer_hand}\n")

    while keep_dealing == True and game_stop == False:
        bust_check = hit(user_current_hand)
        # print(bust_check)
        # print(f"This is user current hand {user_current_hand}")
        if bust_check > 21:
            print(f"You went over 21, you busted. You lose.")
            keep_dealing = False
            game_stop = True
        if bust_check > 21 and 11 in user_current_hand:
            ace_con(user_current_hand)
            print(f"You went over 21 your Ace is now a 1.")
            keep_dealing = True
        elif bust_check < 21 and bust_check != False:
            keep_dealing = True 
        elif bust_check == False:
            keep_dealing = False

    user_score = sum(user_current_hand)

    if game_stop == False:
        dealer_second_card = single_card(cards)
        dealer_hand.extend(dealer_second_card)
        dealer_total = sum(dealer_hand)
        print(f"Computer's hand: {dealer_hand}, current score: {dealer_total}\n")
        dealer_score = dealer_hit(dealer_hand)
        if type(dealer_score) == int and dealer_score > user_score:
            print(f"The dealer won with score of {dealer_score} to your score of {user_score}")
        elif type(dealer_score) == int and dealer_score < user_score:
            print(f"You beat the dealer with a score of {user_score} to the dealer score of {dealer_score}")
        elif type(dealer_score) == int and dealer_score == user_score:
            print(f"It's a push, you both tie with a score of {user_score}")
    print("The game is over.")
    player_decision = input("Type 'y' to play again, type 'n' to stop playing.\n")
    if player_decision == 'n':
        keep_playing = False