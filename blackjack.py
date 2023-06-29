import Card
import game

import os

round_on = True
round_num = 0

print('Welcome to BlackJack!')
name = input("Please enter your name: ")
player_one = Card.Player(name)
game.balance = game.amountcheck()
player_one.addbalance(game.balance)

dealer = Card.Player("Dealer",5*(game.balance))

while round_on:
    
    if player_one.balance <= 0:
        print("You're out of balance!")
        round_on = False
        break
    
    newdeck = Card.Deck()
    newdeck.shuffle()
    
    round_num += 1
    
    print(f"\nRound {round_num} begins!")
    print(f"Available Balance = {player_one.balance}")
    game.bet = game.amountcheck(player_one,round_num)
    
    player_one.clearcards()
    dealer.clearcards()
    
    for _ in range(2):
        player_one.addcard(newdeck.deal())
        dealer.addcard(newdeck.deal())
        
    dealer.cards[1].turnover()
    
    game.printcards(player_one,dealer)
    
    
    stop_before_dealer = game.player_turn(player_one,dealer,newdeck)
    
    if stop_before_dealer:
        pass
    else:
        game.dealer_turn(player_one,dealer,newdeck)
    
    
    round_on = game.choice_round_on()
    os.system('cls')      
          
        
print(f"Thank you for Playing! Your final balance is {player_one.balance}!")

cont = input("Press ENTER to exit.......")
            
    
    
    
            
    
