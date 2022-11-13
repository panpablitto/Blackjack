import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cash = 1000
continue_game = "yes"
user_hand = []
diler_hand =[]

def chose_card(added_list, cards_amount):
    for i in range(0,cards_amount):
            added_list.append(random.choice(cards))
    return True

def sum_and_check(list_name, numer_to_check):
    if sum(list_name)<numer_to_check:
        return True
    else:
        return False

def keep_playing(continue_game):
    if continue_game == "yes":
        return True
    else:
        return False


while keep_playing(continue_game) == True:
    print(F"You have: ${user_cash}")
    continue_game = input("would you like to continue game yes/no? \n")
    user_bet = int(input("How much would you like to bet?: \n"))
    chose_card(user_hand, 2)
    chose_card(diler_hand, 2)
    print(f"this is your cards: {user_hand}\nthis is diler cards: {diler_hand[0]}")
    while sum_and_check(user_hand, 22) == True:
        next_card =input("would you like to take next card yes/no? \n")
        if next_card =="yes":
            chose_card(user_hand, 1)
            print(f"this is your cards: {user_hand}")
        elif next_card =="no":
            while sum_and_check(diler_hand, 17) == True:
                chose_card(diler_hand, 1)
            if sum_and_check(diler_hand, 22) == True:
                if sum(user_hand)>sum(diler_hand):
                    print(f"you won! You won: {user_bet}")
                    user_cash += user_bet
                    print(f"This is diler hand: {diler_hand}")
                    user_hand.clear()
                    diler_hand.clear()
                else:
                    user_cash -= user_bet
                    print(f"you lose! You lost: {user_bet}")
                    print(f"This is diler hand: {diler_hand}")
                    user_hand.clear()
                    diler_hand.clear()
                    break
            else:
                print(f"you won! You won: {user_bet}")
                user_cash += user_bet
                print(f"This is diler hand: {diler_hand}")
                user_hand.clear()
                diler_hand.clear()
                break
    if sum_and_check(user_hand, 22) == False:
        lose_win(0, user_cash, user_bet, diler_hand, user_hand)
print(f"thanks for your game. You won: {user_cash}")
