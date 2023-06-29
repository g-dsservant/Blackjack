bet =  0
balance = 0

def printcards(player=0,dealer=0):
    if dealer != 0:
        print("\n")
        print("Dealers cards -> ", end ="")
        for card in dealer.cards:
            print(card, end=' ')
    
    print()
    if player != 0:
        print(f"{player.name} cards -> ", end ="")
        for card in player.cards:
            print(card, end=' ')
        print("\n")

    
    
    
    
def playerchoice(player):
    options = ['H','S','DD']
    flag_dd = 0
    while True:
        try:
            if len(player.cards) == 2 and bet<=(balance/2):
                choice = input("Do you want to stand, hit or DoubleDown (S or H or DD)? ")
            else:
                choice = input("Do you want to stand or hit (S or H)? ")
            if choice not in options:
                raise TypeError
            if choice == 'DD' and (len(player.cards) != 2 or bet>(balance/2)):
                flag_dd = 1
                raise TypeError
        except:
            if flag_dd == 1:
                print('You cannot Double Down now!')
            else:
                print('Enter a valid option!')
        else:
            return choice
        
        

        
def choice_round_on():
    choice = 'wrong'
    options = ['Y','N']
    
    while choice not in options:
        choice = input("Do you want to play another round (Y or N) ? ")
        
        if choice not in options:
            print("Select a valid option!")
    
    if choice == 'Y':
        return True
    else:
        return False
    
    
    
def player_turn(player,dealer,deck):
    
    import os
    
    global bet
    outcome = False
    player_on = True
    
    choice = playerchoice(player)
    
    while player_on:
        
        if choice == 'H':
            os.system('cls')
            print("You've decided to hit!")
            player.addcard(deck.deal())
            printcards(player,dealer)
            
            if player.value() > 21:
                print(f"{player.name} busted! Dealer wins!")
                player.removebalance(bet)
                dealer.addbalance(bet)
                outcome = True
                player_on = False
                break
            
            else:
                choice = playerchoice(player)
                player_on = True
                continue
        
        if choice == 'S':
            os.system('cls')
            print("You've decided to stand! Moving on to Dealer")
            dealer.cards[1].turnover()
            printcards(player,dealer)
            
            player_on = False
            break

        if choice == 'DD':
            os.system('cls')
            bet = bet*2
            print("You've decided to Double Down! Here is your final card!")
            player.addcard(deck.deal())
            printcards(player)

            if player.value() > 21:
                print(f"{player.name} busted! Dealer wins!")
                player.removebalance(bet)
                dealer.addbalance(bet)
                outcome = True
                player_on = False
                break
            
            else:
                print("Moving on to Dealer")
                dealer.cards[1].turnover()
                printcards(player,dealer)
            
                player_on = False
                break

    

    return outcome





def dealer_turn(player,dealer,deck):
    
    import os
    global bet
    
    if player.value() == 21 and len(player.cards) == 2:
            print(f"\n{player.name} has a blackjack!")
            if dealer.value() == 21 and len(dealer.cards) == 2:
                print("Dealer also has a Blackjack, It's a Push!")
 
            else:
                dealer.removebalance(bet*(3/2))
                player.addbalance(bet*(3/2))
                print(f'Natural 21! {player.name} wins!')


    else:
        while dealer.value() <=16:
            print("Dealer's value less than 17")
            dealer.addcard(deck.deal())
            printcards(player,dealer)

        if dealer.value() > 21:
            print(f"Dealer busts! {player.name} wins!")
            dealer.removebalance(bet)
            player.addbalance(bet)
            

        elif dealer.value() > player.value():
            print(f"Dealer has Higher value than {player.name}, Dealer wins!")
            player.removebalance(bet)
            dealer.addbalance(bet)

        elif dealer.value() == player.value():
            print("It's a push")

        else:
            print(f"{player.name} has Higher value than Dealer, {player.name} wins!")
            dealer.removebalance(bet)
            player.addbalance(bet)
    
    

    

    
from math import ceil    
def amountcheck(player=0,round_num=0):
    if player == 0:
        while True:
            try:
                amount = int(input('Please enter your available balance: '))
                if amount < 0:
                    raise ValueError
            except:
                print("Please enter a valid amount!")
            else:
                return amount
    
    else:
        while True:
            try:
                amount = int(input(f"How much would you like to bet for round {round_num}? "))
                if amount not in range(1,ceil(player.balance+1)):
                    raise ValueError
            except:
                print("Please enter a valid amount!")
            else:
                return amount



if __name__ == "__main__":
    print("This is game module, please run the file named blackjack.py")
    cont = input("Press ENTER to continue......")

