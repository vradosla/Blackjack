## Card variables:

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

# Global variables
playing = True
import random
from IPython.display import clear_output
from os import system

## Create Classes: 

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck():
    
    def __init__(self):
        
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):     
            deck_list =" " 
            for Card in self.deck:
                deck_list += f"\n {Card.__str__()}"
            return deck_list
            
    def shuffle(self):
        import random 
        random.shuffle(self.deck)
        
    def deal(self):
            return self.deck[0] and self.deck.pop(0)

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self):
        self.cards.append(my_deck.deal())
        self.value += values[self.cards[-1].rank]
        if values[self.cards[-1].rank] == 11:
            self.aces += 1
        else:
            pass
        if self.value > 21:
            self.value -= (self.aces*10)
            self.aces = 0
        else:
            pass
    
    def __str__(self):
        hand_tracker = ""
        for item in self.cards:
            hand_tracker += f"\n{item.__str__()}"
        return f"{hand_tracker}\n{self.value}"

def chips_size():
    '''
    Needed to feed player chips and dealer chips'''
    while True:
        try:
            chip_size = int(input("Please select your starting chips size: "))
        except:
            print("Please input a number!")
        else:
            return chip_size               
    
class Chips():
    
    def __init__(self,total):
        self.total = total
        self.bet = 0
        
    def win_bet(self,winnings):
        self.total += int(winnings)
    
    def lose_bet(self,lost):
        self.total -= int(lost)
    
    
## Functions:

def take_bet():
    '''
    Gives result bet size. Needs player_chips & dealer_chips
    '''
    print(f"Player's chips {player_chips.total}")
    print(f"Dealer's chips {dealer_chips.total}")

    while True:
        try:
            bet_size = int(input("Please select your bet size: "))
        except:
            print("Please select a number!")
            continue            
        else:
            if (bet_size <= player_chips.total) and (bet_size <= dealer_chips.total):
                return bet_size
            else:
                print("Insufficient chips! Please select a smaller bet!")
                bet_size =""
    else:
        pass

def show_some():
    '''
    Shows the dealer's one card
    '''
    clear_output()
    system('sleep 1')
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("Dealer:")
    print(dealer_hand.cards[0])
    print("and one face-down card")
    print(values[dealer_hand.cards[0].rank])
    print("\n")
    print(f"Player:{player_hand}")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    
def show_all():
    '''
    Shows all cards
    '''
    clear_output()
    system('sleep 1')
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(f"Dealer:{dealer_hand}")
    print("\n")
    print(f"Player:{player_hand}")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    
def player_hit_or_stand():
    '''
    Ask player if they want to hit or stand, check result, return result
    '''
    show_some()
    if player_hand.value == 21:
        print("Blackjack!!!")
        return player_hand.value
    else:
        while player_hand.value < 21:
            player_decision = input("Do you want to hit or stand? Type 'h' or 's' ").lower()
            if player_decision == "h":
                player_hand.add_card()
                show_some()
            elif player_decision == "s":
                show_some()
                return player_hand.value
            else:    
                print("Invalid input. Try again!")
        else:
            if player_hand.value == 21:
                return player_hand.value
            else:
                show_some()
                return "player busted"

def dealer_hit_or_stand():
    '''
    Dealer auto hit or stand
    '''
    show_all()
    while dealer_hand.value <22:
        if player_hand.value >21:
            return dealer_hand.value
        elif dealer_hand.value > player_hand.value:
            return dealer_hand.value
        elif dealer_hand.value <17:
            dealer_hand.add_card()
            show_all()
        else:
            return dealer_hand.value
    else:
        return "dealer busted"
        
# Game results function:
def game_result(bet,player_result,dealer_result):
    '''
    Takes in bet_size result, player hit_or_stand result, and dealer_hit_or_stand result'''
    if  player_result == "player busted":
        player_chips.lose_bet(bet)
        dealer_chips.win_bet(bet)
        print("Player busted!")
    elif dealer_result == "dealer busted":
        dealer_chips.lose_bet(bet)
        player_chips.win_bet(bet)
        print("Dealer busted!")
    elif player_result == dealer_result:
        print("Draw!")
    elif player_result > dealer_result:
        player_chips.win_bet(bet)
        dealer_chips.lose_bet(bet)
        print("Player wins!")
    elif player_result < dealer_result:
        dealer_chips.win_bet(bet)
        player_chips.lose_bet(bet)
        print("Dealer wins!")

        
# Programming the game        

if __name__ == "__main__":
    def blackjack():
        print("Welcome to blackjack!")

        playing = True

        while playing:
            start = input("Do you want to play? Type 'y' or 'n' ").lower()
            if start == "n":
                playing = False
            elif start == "y":
                global player_chips
                global dealer_chips
                player_chips = Chips(chips_size())
                dealer_chips = Chips(player_chips.total)

                while (player_chips.total >0) and (dealer_chips.total >0):
                    global my_deck
                    my_deck = Deck()
                    my_deck.shuffle()

                    global player_hand
                    global dealer_hand
                    player_hand = Hand()
                    dealer_hand = Hand()

                    player_hand.add_card()
                    dealer_hand.add_card()
                    player_hand.add_card()     
                    dealer_hand.add_card()

                    game_result(take_bet(),player_hit_or_stand(),dealer_hit_or_stand())

                    if player_chips.total >0 and dealer_chips.total >0:
                        cont_play = input("Do you want to keep playing? Type 'y' or 'n' ").lower()
                        try:
                            while True:
                                if cont_play == "n":
                                    playing = False
                                    raise StopIteration
                                elif cont_play == "y":
                                    cont_play = ""
                                    break
                                else:
                                    print("Wrong input!")
                                    cont_play = input("Do you want to keep playing? Type 'y' or 'n' ").lower()
                        except StopIteration: break
                    else:
                        pass
                else:
                    if player_chips.total == 0:
                        print("You lose!")
                        start =""
                    elif dealer_chips.total == 0:
                        print("You win!")
                        start =""
            else:
                print("Please give correct input")
                start = input("Do you want to play? Type 'y' or 'n' ").lower()
        else:
            print("Thanks for playing!")
            playing = False    