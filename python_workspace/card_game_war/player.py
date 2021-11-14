class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.active_cards = []

    def add_card(self, card_obj):
        if(isinstance(card_obj, list)):
            self.all_cards.extend(card_obj)
        else:
            self.all_cards.append(card_obj)

    def pop_card(self):
        return self.all_cards.pop(0)

    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards'
