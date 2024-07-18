class Admin:
    
    def __init__(self, game):
        self.game = game

    def add_player(self, name, initial_funds):
        player = Player(name, initial_funds)
        self.game.players.append(player)

    def remove_player(self, player):
        self.game.players.remove(player)

    def reset_game(self):
        self.game.players.clear()
        self.game.deck.shuffle()
