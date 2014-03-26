import random
SPADES = 1
HEARTS = 2
DIAMONDS = 3
CLUBS = 4
names = ("spades", "hearts", "diamonds", "clubs")
def getSymbol(cardValue):
    if 2 <= cardValue and cardValue <= 10:
        return repr(cardValue)
    elif cardValue == 1:
        return 'A'
    else:
        return ('J','Q','K')[cardValue - 11]
        
def getSortedDeck():
    deck = []
    for suit in range(1,5):
        for value in range(1,14):
            deck.append((suit, value))
    return deck
def shuffle(deck):
    for index in range(len(deck) - 1,0,-1):
        next = random.randrange(0,index)
        #swapping is awkward...
        t_card = deck[next]
        deck[next] = deck[index]
        deck[index] = t_card
    return deck
def getName(card):
    return getSymbol(card[1]) + " of " +names[card[0] - 1]

def isLegal(card1, card2):
    if card1[0] == card2[0] or card1[1] == card2[1]:
        return True
    else:
        return False

def getNextCard(card1, tableau=False):
    if tableau:
        if card1[1] != 1:
            if card1[0] == 1 or card1[0] == 4:
                return ((2, card1[0] - 1),(3, card1[0] - 1))
            else:
                return ((1, card1[0] - 1),(4, card1[0] - 1))        
    elif card1[1] != 14:
        return (card1[0], card1[1] + 1)
def getCardIndex(card):
    return 13*(card[0] - 1) + (card[1] - 1)
    

        
        
