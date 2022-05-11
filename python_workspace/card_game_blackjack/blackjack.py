'''
The goal of blackjack is to have a hand that totals higher than the dealer's, but not exceeding 21
If a player's hand totals higher than 21, it is called BUST and the player is out of the game
1)Create a deck of 52 cards
2)Shuffle the deck
3)Ask the Player for their bet
4)Make sure that the Player's bet does not exceed their available chips
5)Deal two cards to the Dealer and two cards to the Player
6)Show only one of the Dealer's cards, the other remains hidden
7)Show both of the Player's cards
8)Ask the Player if they wish to Hit, and take another card
9)If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10)If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
11)Determine the winner and adjust the Player's chips accordingly
12)Ask the Player if they'd like to play again

DECK/CARD
A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) 
and thirteen ranks (2 through 10, then the face cards Jack, Queen, King and Ace) for 
a total of 52 cards per deck. 
Jacks, Queens and Kings all have a rank of 10. 
Aces have a rank of either 11 or 1 as needed to reach 21 without busting. 
4 suites - Heart, Diamond, Spade, Club
13 ranks - 2,3,4,5,6,7,8,9,10,Jack(10),Queen(10),King(10),Ace(11)

NOUNS:
Deck
Card
Chips - keep track of a Player's starting chips, bets, and ongoing winnings
Hand(player/dealer) - represents what cards are there in someone's hand. It adds card from deck and keeps a track of
overall value for a hand

PSEUDOCODE:
1)2 player game - 1 Human Player and 1 Computer Dealer 
2)4 suites - Heart, Diamond, Spade, Club
3)13 ranks - 2,3,4,5,6,7,8,9,10,Jack(10),Queen(10),King(10),Ace(1 or 11)
4)4*13 = 52 Cards. Shuffle them
5)Initialize 100 chips(default) each and assign to Human Player and Computer Dealer.
6)ITERATION #1 - Repeat while player still wants to take another Bet***
    7)Ask for bet amount for Human Player. It should not exceed the available chips count
    8)Pull 2 cards each from deck to human player 'hand' and computer dealer 'hand'
    9)Show full cards for human player
    10)Show few cards(hide one) for computer dealer
    11)Ask for Hit or Stand from Player
    12)ITERATION #2 - Repeat while player is still opting for Hit***
        13)Pull 1 card from deck and append to human player 'hand'
        14)IF - Card pulled is Ace, THEN increment ace count
        15)ITERATION #3 - while ace count > 0 AND total value of cards in 'hand' > 21
            16)adjust ace and decrement ace count  
        17)IF - total value of cards in player 'hand' > 21
            18)declare player is 'BUST' and dealer has won
            19)player transfers the chips(bet amount) to the computer dealer
        20)ELSE - Prompt the player for Hit or Stand 
    21)IF - player has not BUST
        22)ITERATION #4 - Repeat while total value of cards in 'hand' for dealer is <17 ***
            23)Pull 1 card from deck and append to computer dealer 'hand'
            24)IF - Card pulled is Ace, THEN increment ace count
            25)ITERATION #5 - ace count > 0 AND total value of cards in 'hand' > 21
                26)adjust ace and decrement ace count  
            27)IF - total value of dealer cards in 'hand' > 21
                28)declare dealer is 'BUST' and player has won
                29)dealer transfers the chips(bet amount) to the human player 
        30)IF - total value of dealer cards in 'hand' > player cards in 'hand'
            31)declare player loses the bet and dealer has won
            32)player transfers the chips(bet amount) to the computer dealer
        33)ELSE declare dealer is 'BUST' and player has won
            34)dealer transfers the bet amount chips to the human player
    35)Ask whether Player wants to continue betting?
'''
from deck import Deck
from hand import Hand
from chips import Chips
import random

deck_instance = Deck()
deck_instance.shuffle()
print(str(deck_instance))
chips_count = int(input('How many chips does human player have?'))
player_chips = Chips(chips_count)
bet_on = input('would you like to bet. y/n? ')
round_num = 0
while(bet_on == 'y'):
    while(True):
        player_hand = Hand('Human Player')
        player_hand.add_card(deck_instance.deal())
        player_hand.add_card(deck_instance.deal())
        player_hand.show_all()
        dealer_hand = Hand('Computer Dealer')
        dealer_hand.add_card(deck_instance.deal())
        dealer_hand.add_card(deck_instance.deal())
        dealer_hand.show_few()
        bet_amount = int(input('Enter the number of chips to bet? '))
        if(bet_amount > player_chips.value):
            print(
                f'Sorry! You have only {player_chips.value} chips left. Please retry..')
        else:
            break
    player_chips.make_bet(bet_amount)
    while(player_hand.card_value <= 21):
        hit_or_stand = input('do you like to hit or stand. h/s? ')
        if(hit_or_stand == 'h'):
            player_hand.add_card(deck_instance.deal())
            player_hand.show_all()
        elif(hit_or_stand == 's'):
            break
    while(dealer_hand.card_value < 17):
        dealer_hand.add_card(deck_instance.deal())
    dealer_hand.show_all()
    if(player_hand.card_value > 21):
        print('Player BUST. Dealer WON')
        player_chips.lose_bet()
    elif(dealer_hand.card_value > 21):
        print('Dealer BUST. Player WON')
        player_chips.win_bet()
    elif(dealer_hand.card_value > player_hand.card_value):
        print('Dealer WON')
        player_chips.lose_bet()
    elif(dealer_hand.card_value < player_hand.card_value):
        print('Player WON')
        player_chips.win_bet()
    round_num += 1
    print(f'End of round #{round_num}. Player has {player_chips.value} chips!')
    if(player_chips.value > 0):
        bet_on = input('would you like to bet again. y/n? ')
    else:
        break
print(
    f'End of GAME at round #{round_num}!!')
