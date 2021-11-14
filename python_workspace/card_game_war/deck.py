from card import Card
from card import suits
from card import ranks
import random


class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.all_cards.append(card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

    def __str__(self):
        all_cards_str = ''
        for index in range(0, 52):
            all_cards_str += (str(self.all_cards[index])) + '\n'
        return all_cards_str
