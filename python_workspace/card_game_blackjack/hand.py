from card import Card


class Hand():
    def __init__(self, name):
        self.name = name
        self.active_cards = []
        self.no_of_aces = 0
        self.card_value = 0

    def add_card(self, card):
        self.active_cards.append(card)
        self.update_card_value(card)

    def update_card_value(self, card):
        self.card_value += card.value
        if(card.rank == 'ace'):
            self.no_of_aces += 1
        self.adjust_for_ace()
        return self.card_value

    def adjust_for_ace(self):
        while(self.card_value > 21 and self.no_of_aces > 0):
            self.card_value -= 10
            self.no_of_aces -= 1

    def pop_card(self):
        return self.active_cards.pop(0)

    def show_all(self):
        for card in self.active_cards:
            print(f'{self.name} has {card}')

    def show_few(self):
        for card in self.active_cards[1:]:
            print(f'{self.name} has {card}')

    def __str__(self):
        return f'{self.name} has {len(self.active_cards)} cards'
