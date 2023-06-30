'''
Game module
Contains all necessary functions to run the game
'''

import os


class CustomError(Exception):
    '''
    This class is used to raise exceptions in all user input functions in this file.

    Attributes:
          1) Message: The message associated an Exception
    '''
    def __init__(self,message):
        '''
        The constructor of CustomError class.

            Parameters:
                 Message: The text you want to be displayed when that particular Exception is raised.
        '''
        self.message = message


def amount_check(chip,round_num=0):
    '''
    This function has two utilities:
         1) To accept and validate total balance of the player at the start of the game from the user
         2) To accept and validate the bet value at the start of every round from the user
    '''
    if not round_num:
        while True:
            try:
                amount = int(input("Please enter your available balance: "))
                if amount < 0:
                    raise CustomError("Balance cannot be negative!")
            
            except CustomError as error:
                print(f"{error.message}")
            
            except ValueError:
                print("Enter a valid amount!")
            
            else:
                chip.balance = amount
                break
    
    else:
        while True:
            try:
                amount = int(input(f"How much would you like to bet for Round {round_num}?: "))
                if amount > chip.balance or amount <= 0:
                    raise CustomError("Cannot bet outside your balance!")
                
            except ValueError:
                print("Enter a valid amount!")
        
            except CustomError as error:
                print(f"{error.message}")
        
            else:
                chip.bet = amount
                break


def player_choice(hand,chip):
    '''
    This function accepts and validates the choice of what the user's next move will be.
    '''
    valid_options = ['S','H','DD']
    choice = 'wrong'
    
    while True:
        try:
            if len(hand.cards) == 2 and chip.bet <= (chip.balance/2):
                choice = input("Do you want to Stand, Hit or DoubleDown (S or H or DD)?: ")
            else:
                choice = input("Do you want to Stand, Hit (S or H)?: ")
        
            if choice == 'DD' and (len(hand.cards) != 2 or chip.bet > (chip.balance/2)):
                raise CustomError("You cannot Double Down at this point!")
            
            if choice not in valid_options:
                raise CustomError("Select a valid option!")
        
        except CustomError as error:
            print(f"{error.message}")
        
        else:
            return choice
                

def player_turn(hand_player,hand_dealer,chip,deck):
    '''
    This function takes in the user choice using "player_choice()" function and, depending on that choice, it determines whether the player can continue with the game or if they have lost. 
    Returns True if they can continue or False if they have lost.
    '''
    outcome = True
    choice = player_choice(hand_player,chip)
    
    while True:
        if choice == 'S':
            os.system('cls')

            print("You have decided to Stand!")
            print("Moving on to the dealer!")
            break
            
        if choice == 'H':
            os.system('cls')

            hand_player.add_card(deck.deal())
            print("You have decided to Hit! Here are your new cards")
            display_cards(hand_player,hand_dealer)
            
            if hand_player.value() > 21:
                print(f"{hand_player.name} busted! Dealer wins!")
                chip.remove_balance(chip.bet)
                outcome = False
                break
            
            else:
                choice = player_choice(hand_player,chip)
                continue
                
        if choice == 'DD':
            os.system('cls')

            print("You have decided to Double Down! Here are you're new cards!")
            chip.bet = chip.bet * 2
            hand_player.add_card(deck.deal())
            display_cards(hand_player,hand_dealer)
            
            if hand_player.value() > 21:
                print(f"{hand_player.name} busted! Dealer wins!")
                chip.remove_balance(chip.bet)
                outcome = False
                break
            
            print("Moving on to the Dealer!")
            break
    
    return outcome


def dealer_turn(hand_player,hand_dealer,chip,deck):
    '''
    This function determines what the dealer should do based on his cards and decides who has won the game.
    '''
    hand_dealer.cards[1].turn_card_over()

    display_cards(hand_player,hand_dealer)

    
    if hand_player.value() == 21 and len(hand_player.cards) == 2:
        
        if hand_dealer.value() == 21:
            print("It's a push!")
        
        else:
            print(f"{hand_player.name} got a BlackJack!")
            chip.add_balance((3/2)*chip.bet)
        
    else:
        
        while hand_dealer.value() <= 16:
            print("Dealer has less than 17! Dealer gets to Hit!")
            hand_dealer.add_card(deck.deal())
            display_cards(hand_player,hand_dealer)
        
        if hand_dealer.value() > 21:
            print(f"Dealer busts, {hand_player.name} wins!")
            chip.add_balance(chip.bet)
        
        elif hand_dealer.value() > hand_player.value():
            print("Dealer has a higher value! Dealer wins!")
            chip.remove_balance(chip.bet)
        
        elif hand_dealer.value() == hand_player.value():
            print("It's a push!")
        
        else:
            print(f"{hand_player.name} has a higher value! {hand_player.name} wins!")
            chip.add_balance(chip.bet)


def choice_to_continue():
    '''
    This function accepts and validates the choice of whether the user wants to play another round or not.
    '''
    valid_options = ['Y','N']
    choice = 'wrong'
    
    while choice not in valid_options:
        
        choice = input("Do you want to play another round (Y os N)?")
        
        if choice not in valid_options:
            print("Select a valid option!")
        
        else:
            return choice == 'Y'
            

def display_cards(hand_player=0,hand_dealer=0):
    '''
    This function is used to display cards of either the player or the dealer or both.
    '''
    if hand_player:
        print("\n")
        print(f"{hand_player.name}'s cards ->", end = ' ')

        for card in hand_player.cards:
            print(card,end=' ')

        print()
    
    if hand_dealer:
        print(f"Dealer's cards ->", end = ' ')

        for card in hand_dealer.cards:
            print(card,end=' ')
        
    print('\n')
    
        

if __name__ == '__main__':
    print("This is game.py module, please open blackjack.py")
    input("Press ENTER to exit.......")
