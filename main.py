from Admin import Admin
from BlackJackGame import BlackJackGame
from Deck import Deck
from Dealer import Dealer
from Player import Player

def main():
    # Initialize deck and shuffle it
    deck = Deck()
    deck.shuffle()

    # Create dealer and admin
    dealer = Dealer()
    admin = Admin(None)

    # Initialize players
    players = [
        Player("Alice", 1000),
        Player("Bob", 1000)
    ]

    # Create the game instance
    game = BlackJackGame(players, deck, dealer, admin)

    # Associate the admin with the game
    admin.game = game

    # Start the game
    game.start_game()

    # Play rounds until the game ends
    game_ended = False
    while not game_ended:  # Continue playing until game ends
        game.play_round()
        game_ended = game.end_game()  # Update game_ended based on end_game()

    print("Game over!")

if __name__ == "__main__":
    main()