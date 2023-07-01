'''BlackJack Game'''

import os
import card
import game



def main():
    '''
    This function contains the game logic.
    '''
    round_om = True
    round_num = 0

    print('Welcome to BlackJack!')

    hand_player = card.Hand.ask_name()
    hand_dealer = card.Hand('Dealer')

    chips_player = card.Chip.ask_balance()
    
    #create and shuffle deck
    new_deck = card.Deck()
    new_deck.shuffle()

    #enter loop for rounds
    while round_on:

        #clear the output before
        os.system('cls')

        #stop the game when player runs out of balance
        if chips_player.balance <= 0:
            print("You're out of balance!")
            round_on = False
            break

        #clear the cards of player and dealer from previous round
        hand_player.clear_hand()
        hand_dealer.clear_hand()
        chips_player.clear_bet()

        #if we have less than 10 cards, we restack/create a new deck and shuffle it
        new_deck.restack()

        round_num += 1
        print(f"Round {round_num} begins!")
        print(f"Available Balance: {chips_player.balance}")

        #ask how much they want to bet for the current round
        chips_player.ask_bet(round_num)

        #deal two cards to the player and the dealer
        for _ in range(2):
            hand_player.add_card(new_deck.deal())
            hand_dealer.add_card(new_deck.deal())

        #last card of dealer has to be facing down
        hand_dealer.cards[1].turn_card_over()
        
        #display their cards
        game.display_cards(hand_player,hand_dealer)

        #players turn, dealers turn
        if game.player_turn(hand_player,hand_dealer,chips_player,new_deck):
            game.dealer_turn(hand_player,hand_dealer,chips_player,new_deck)

        #ask if they want to play another round
        round_on = game.choice_to_continue()

    #end
    os.system('cls')
    print(f"Thank you for playing, your final balance is {chips_player.balance}")

main()
input("Press ENTER to exit.......")
