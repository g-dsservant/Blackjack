suits = ('hearts','diamonds','spades','clubs')
ranks = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':[1,11]}


class Card:
    
    def __init__(self,suit,rank,face_up=True):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        self.face_up = face_up
    
    def turnover(self):
        self.face_up = not self.face_up
    
    def __str__(self):
        if self.face_up:
            return f"'{self.rank} of {self.suit}'"
        else:
            return "'Face Down'"
        
        


class Deck:
    
    def __init__(self):
        self.allcards = [Card(suit,rank) for suit in suits for rank in ranks]
    
    def shuffle(self):
        import random
        random.shuffle(self.allcards)
    
    def restack(self):
        if len(self.allcards) <= 10:
            self.__init__()
            self.shuffle()
            return self
        else:
            return self
        
    def deal(self):
        return self.allcards.pop()
    
    
    

class Player:
    
    def __init__(self,name,balance=0):
        self.name = name
        self.cards = []
        self.balance = balance
    
    def addbalance(self,amount):
        self.balance += amount
        
    def removebalance(self,amount):
        self.balance -= amount
    
    def addcard(self,new_card):
        if new_card.rank == 'ace':
            self.cards.append(new_card)
        else:
            self.cards.insert(0,new_card)
    
    def value(self):
        total = 0
        flag = len(self.cards)
        for i in range(len(self.cards)):
            if self.cards[i].rank == 'ace':
                flag = i
                break
            else:
                total += self.cards[i].value
        
        while flag < len(self.cards):
            if total>10:
                total += self.cards[flag].value[0]
                flag += 1
            else:
                total += self.cards[flag].value[1]
                flag += 1
        
        return total
    
    def clearcards(self):
        self.cards = []



if __name__ == "__main__":
    print("This is Card module, please run the file named blackjack.py")
    cont = input("Press ENTER to continue......")
