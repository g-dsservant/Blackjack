'''
Card module
Contains basic classes required for BlackJack
'''

import random

#constants
SUITS = ("hearts","diamonds","clubs",'spades')
RANKS = ("two",'three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
VALUES = {"two":2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
          'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11
          }


class Card:
    '''This Class represents cards.'''

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]
        self.face_up = True
        
    def __str__(self):
        if self.face_up:
            return f"'{self.rank} of {self.suit}'"
        return "'Face Down'"
    
    def turn_card_over(self):
        '''Turns the card over'''
        self.face_up = not self.face_up

       
class Deck:
    '''
    This Class represents a standard deck of 52 cards.
    '''
    
    def __init__(self):
        self.all_cards = [Card(suit,rank) for suit in SUITS for rank in RANKS]
        
    def shuffle(self):
        '''Shuffles the deck'''
        random.shuffle(self.all_cards)
    
    def deal(self):
        '''Deals a card to an individual from bottom of the deck'''
        return self.all_cards.pop()
    
    def restack(self):
        '''Restacks the deck when the current deck has less than 10 cards'''
        if len(self.all_cards) <= 10:
            self.all_cards = [Card(suit,rank) for suit in SUITS for rank in RANKS]
            self.shuffle()


class Hand:
    '''
    This Class represents the cards held by an individual.
    '''
    
    def __init__(self,name='Anonymous'):
        self.name = name
        self.cards = []
    
    def add_card(self,new_card):
        '''Adds a card to the hand'''
        self.cards.append(new_card)
    
    def clear_hand(self):
        '''Clears all cards from the hand'''
        self.cards = []
    
    def value(self):
        '''Calculates the value of all cards according to standard Blackjack rules'''
        aces = 0
        total = 0
        for card in self.cards:
            if card.rank == 'ace':
                aces += 1
            total += card.value
            
        while aces:
            if total > 21:
                total -= 10
            aces -= 1
        
        return total


class Chip:
    '''
    This Class represents the chips held by an individual
    '''
    
    def __init__(self):
        self.balance = 0
        self.bet = 0
    
    def add_balance(self,amount):
        '''Adds new chips to the balance'''
        self.balance += amount
        
    def remove_balance(self,amount):
        '''Removes chips from balance'''
        self.balance -= amount
        
    def clear_bet(self):
        '''Clears the existing bet for new round'''
        self.bet = 0

        



if __name__ == '__main__':
    print("This is card.py module, please open blackjack.py")
    input("Press ENTER to exit.......")
