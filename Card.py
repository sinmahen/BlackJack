class Card:
    
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def get_value(self):
        return self.value
