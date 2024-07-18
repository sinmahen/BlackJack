import random

class Deck:
    
    def __init__(self):
        self.cards = []
        self.initialize_deck()

    def initialize_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        for suit in suits:
            for rank, value in zip(ranks, values):
                self.cards.append(Card(suit, rank, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def size(self):
        return len(self.cards)
