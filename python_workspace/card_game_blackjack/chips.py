class Chips():
    def __init__(self, value=100):
        self.value = value
        self.bet = 0

    def make_bet(self, bet):
        self.bet = bet

    def win_bet(self):
        self.value += self.bet
        self.bet = 0

    def lose_bet(self):
        self.value -= self.bet
        self.bet = 0
