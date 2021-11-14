'''
1)2 player game 
2)4 suites - Heart, Diamond, Spade, Club
3)13 ranks - 2,3,4,5,6,7,8,9,10,Jack,Queen,King,Ace
4)4*13 = 52 Cards. Shuffle them
5)Divide 52 cards into 2 MAIN decks and assign to both players
6)ITERATION #1 - Repeat while game is still on***
    7)IF player1 has NO cards left in his MAIN deck, declare player2 as WINNER and EXIT the game
    8)IF player2 has NO cards left in his MAIN deck, declare player1 as WINNER and EXIT the game
    9)Pop(top) the card from each player's MAIN deck and push into their ACTIVE deck 
    10)Peek(top) from their ACTIVE deck and compare the card rank of each player
    11)IF - One of the player has highest value
        12) THEN - that player wins the iteration and collects cards from both ACTIVE decks
           and appends to the bottom of his MAIN deck. 
        13) Continue ITERATION #1
    14)ELSE IF - the value matches
        15)THEN there is a WAR. 
        16)ITERATION #2 - Repeat while at WAR***
            17)IF player1 has less than 5 cards left in his MAIN deck, declare player2 as WINNER and EXIT the game
            18)IF player2 has less than 5 cards left in his MAIN deck, declare player1 as WINNER and EXIT the game
            19)In case of war, each player pops(top) five cards from their MAIN deck into their ACTIVE deck
            20)Peek(top) from their ACTIVE deck and compare the card rank of each player
            20)IF - One of the player has highest value
                21)THEN - he wins the iteration and collects all the cards to the bottom of his MAIN deck. 
                22)Exit the WAR and Continue ITERATION #1
            22)ELSE IF - the value matches
                23)THEN there is a another WAR. Continue ITERATION #2   
'''
from player import Player
from deck import Deck
import random

deck_instance = Deck()
deck_instance.shuffle()
print(str(deck_instance))
print('------------')
player_one = Player('Vijay')
player_two = Player('Priya')
for index in range(0, 26):
    player_one.add_card(deck_instance.deal())
    player_two.add_card(deck_instance.deal())
print('------------')
print(str(player_one))
print(str(player_two))
print('------------')

round_num = 0
war_pawn_count = 5
game_on = True
while(game_on):
    if(len(player_one.all_cards) == 0):
        print(f'{player_two.name} is winner after {round_num} rounds. exit game')
        game_on = False
    elif(len(player_two.all_cards) == 0):
        print(f'{player_one.name} is winner after {round_num} rounds. exit game')
        game_on = False
    else:
        print(f'{str(player_one)} <-> {str(player_two)}')
        round_num += 1
        player_one_active_cards = []
        player_two_active_cards = []
        player_one_card = player_one.pop_card()
        player_one_active_cards.append(player_one_card)
        player_two_card = player_two.pop_card()
        player_two_active_cards.append(player_two_card)
        print(
            f'{player_one.name}:{str(player_one_card)} vs {player_two.name}:{str(player_two_card)}')
        if(player_one_active_cards[-1].value > player_two_active_cards[-1].value):
            print(f'{player_one.name} win round # {round_num}')
            player_one.add_card(player_one_active_cards.pop())
            player_one.add_card(player_two_active_cards.pop())
        elif(player_two_active_cards[-1].value > player_one_active_cards[-1].value):
            print(f'{player_two.name} win round # {round_num}')
            player_two.add_card(player_one_active_cards.pop())
            player_two.add_card(player_two_active_cards.pop())
        else:
            war_on = True
            while(war_on):
                round_num += 1
                print(f'Enter WAR on round # {round_num}')
                if(len(player_one.all_cards) < 5):
                    print(
                        f'{player_two.name} is winner after {round_num} rounds. exit game')
                    war_on = False
                    game_on = False
                elif(len(player_two.all_cards) < 5):
                    print(
                        f'{player_one.name} is winner after {round_num} rounds. exit game')
                    war_on = False
                    game_on = False
                else:
                    for _ in range(war_pawn_count):
                        player_one_card = player_one.pop_card()
                        player_one_active_cards.append(player_one_card)
                        player_two_card = player_two.pop_card()
                        player_two_active_cards.append(player_two_card)
                    print(
                        f'{player_one.name}:{str(player_one_card)} vs {player_two.name}:{str(player_two_card)}')
                    if(player_one_active_cards[-1].value > player_two_active_cards[-1].value):
                        print(f'{player_one.name} win round # {round_num}')
                        player_one.add_card(player_one_active_cards)
                        player_one.add_card(player_two_active_cards)
                        war_on = False
                    elif(player_two_active_cards[-1].value > player_one_active_cards[-1].value):
                        print(f'{player_two.name} win round # {round_num}')
                        player_two.add_card(player_one_active_cards)
                        player_two.add_card(player_two_active_cards)
                        war_on = False
