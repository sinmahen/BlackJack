class Dealer:
    
    def __init__(self):
        self.hand = []

    def deal_initial_cards(self, deck):
        self.hand.append(deck.deal_card())
        self.hand.append(deck.deal_card())

    def play_turn(self, deck):
        while self.get_hand_value() < 17:
            self.hand.append(deck.deal_card())

    def get_hand_value(self):
        value = 0
        aces = 0
        for card in self.hand:
            value += card.get_value()
            if card.rank == "Ace":
                aces += 1
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def bust(self):
        return self.get_hand_value() > 21
