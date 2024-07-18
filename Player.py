class Player:
    
    def __init__(self, name, funds):
        self.name = name
        self.hand = []
        self.bet_amount = 0
        self.funds = funds

    def place_bet(self, amount):
        self.bet_amount += amount
        self.funds -= amount

    def receive_card(self, card):
        self.hand.append(card)

    def stand(self):
        pass

    def double_down(self):
        pass

    def split_hand(self):
        pass

    def get_hand_value(self):
        value = sum(card.get_value() for card in self.hand)
        return value

    def bust(self):
        return self.get_hand_value() > 21
