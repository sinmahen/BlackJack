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
        if len(self.hand) != 2 or self.hand[0].rank != self.hand[1].rank:
            raise ValueError("Cannot split hand. The two cards must have the same rank.")
        
        # Logic for splitting the hand
        new_hand = [self.hand.pop()]  # Remove one card to create a new hand
        self.hand.append(self.hand[0])  # Keep the second card in the original hand

        return new_hand  # Return the new hand for further processing

    def get_hand_value(self):
        value = sum(card.get_value() for card in self.hand)
        return value

    def bust(self):
        return self.get_hand_value() > 21