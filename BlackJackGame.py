class BlackJackGame:
    def __init__(self, players, deck, dealer, admin):
        self.players = players
        self.deck = deck
        self.dealer = dealer
        self.admin = admin

    def start_game(self):
        self.deck.shuffle()
        for player in self.players:
            player.receive_card(self.deck.deal_card())
            player.receive_card(self.deck.deal_card())
        self.dealer.deal_initial_cards(self.deck)
        print("Game started. Cards have been dealt.")

    def play_round(self):
        for player in self.players:
            print(f"\n{player.name}'s turn:")
            while not player.bust():
                action = input(f"{player.name}, choose action (hit/stand/double/split): ").lower()
                
                if action == 'hit':
                    player.receive_card(self.deck.deal_card())
                    print(f"{player.name} hits and receives a card.")
                elif action == 'stand':
                    player.stand()
                    print(f"{player.name} stands.")
                    break
                elif action == 'double':
                    player.double_down()
                    player.receive_card(self.deck.deal_card())
                    print(f"{player.name} doubles down and receives one final card.")
                    break
                elif action == 'split':
                    try:
                        new_hand = player.split_hand()
                        print(f"{player.name} splits the hand.")
                        self.play_split_hand(player, new_hand)
                    except ValueError as e:
                        print(e)
                    break
                else:
                    print("Invalid action. Please choose 'hit', 'stand', 'double', or 'split'.")
                
                print(f"{player.name}'s hand value: {player.get_hand_value()}")
                if player.bust():
                    print(f"{player.name} busts!")
                    break

        print("\nDealer's turn:")
        self.dealer.play_turn(self.deck)
        dealer_value = self.dealer.get_hand_value()
        print(f"Dealer's hand value: {dealer_value}")
        if self.dealer.bust():
            print("Dealer busts!")

    def play_split_hand(self, player, new_hand):
        print(f"\n{player.name}'s new split hand:")
        player.hand = new_hand
        while not player.bust():
            action = input(f"{player.name}, choose action for split hand (hit/stand): ").lower()
            if action == 'hit':
                player.receive_card(self.deck.deal_card())
                print(f"{player.name} hits and receives a card.")
            elif action == 'stand':
                player.stand()
                print(f"{player.name} stands.")
                break
            else:
                print("Invalid action. Please choose 'hit' or 'stand'.")

            print(f"{player.name}'s hand value: {player.get_hand_value()}")
            if player.bust():
                print(f"{player.name} busts!")

    def end_game(self):
        dealer_value = self.dealer.get_hand_value()
        print("\nGame over. Checking results...")
        game_ended = True  # Set game_ended to True as the game has concluded
        for player in self.players:
            player_value = player.get_hand_value()
            print(f"\n{player.name}'s hand value: {player_value}")
            if player.bust():
                print(f"{player.name} loses the bet.")
            elif dealer_value > 21 or player_value > dealer_value:
                print(f"{player.name} wins!")
                player.funds += player.bet_amount * 2
            elif player_value == dealer_value:
                print(f"{player.name} pushes (draw).")
                player.funds += player.bet_amount
            else:
                print(f"{player.name} loses the bet.")
            player.bet_amount = 0  # Reset bet amount
        print("Funds have been updated.")
        return game_ended  # Return True indicating the game has ended