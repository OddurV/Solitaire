import cards
DOWN = 0
UP = 1
DECK = 0
STACKS = 2

deck = cards.getSortedDeck()
deck = cards.shuffle(deck)
undeck = []
tableau = []
for col in range(7):
    tableau.append([])
    for card in range(col + 1):
        tableau[col].append(deck.pop())
stacks = [(0,0) for x in range(4)]

states = [[DOWN, DECK]]*52
for index, col in enumerate(tableau):
    for rowIndex, card in enumerate(col):
        states[cards.getCardIndex(card)] = [DOWN, [index, rowIndex]]
        if rowIndex == len(col) - 1:
            states[cards.getCardIndex(card)][0] = UP

def getState(card):
    return states[cards.getCardIndex(card)][:]
def legalMove(moveCard, index, inTableau=True):
    if inTableau:
        if len(tableau[index]) != 0:
            toCard = tableau[index][-1]
            if (((moveCard[0] == cards.SPADES or moveCard[0] == cards.CLUBS) and
                (toCard[0] == cards.HEARTS or toCard[0] == cards.DIAMONDS)) or
               ((moveCard[0] == cards.HEARTS or moveCard[0] == cards.DIAMONDS) and
                (toCard[0] == cards.SPADES or toCard[0] == cards.CLUBS))):
                if toCard[1] == moveCard[1] + 1:
                    return True
        elif moveCard[1] == 13:
            return True
    else:
        if (stacks[index][1] == moveCard[1] - 1 and (stacks[index][0] == moveCard[0] or stacks[index][0] == 0) and
           cardsBelow(moveCard) == [moveCard]):
            return True
    return False
def appendToTableau(moveCard, tableauIndex):
    states[cards.getCardIndex(moveCard)] = [UP, [tableauIndex, len(tableau[tableauIndex])]]
    tableau[tableauIndex].append(moveCard)
def attemptMove(moveCard, index, inTableau=True):
    if inTableau:
        if legalMove(moveCard, index):
            if getState(moveCard)[1] == DECK:
                appendToTableau(moveCard, index)
                undeck.pop()
            else:
                moveIndex = getState(moveCard)[1][0]
                moveList = cardsBelow(moveCard)[:]
                tableau[moveIndex] = tableau[moveIndex][:getState(moveCard)[1][1]]
                for card in moveList:
                    appendToTableau(card, index)
                if len(tableau[moveIndex]) != 0:
                    states[cards.getCardIndex(tableau[moveIndex][-1])][0] = UP
            return True
    elif legalMove(moveCard, index, inTableau=False):
        stacks[index] = moveCard
        if getState(moveCard)[1] != DECK:
            moveIndex = getState(moveCard)[1][0]
            tableau[moveIndex].pop()
            if len(tableau[moveIndex]) != 0:
                states[cards.getCardIndex(tableau[moveIndex][-1])][0] = UP
        else:
            undeck.pop()
        states[cards.getCardIndex(moveCard)] = [UP, STACKS, index]
        return True
    return False
def cardsBelow(activeCard):
    if getState(activeCard)[0] == DECK:
        return [activeCard]
    return tableau[getState(activeCard)[1][0]][getState(activeCard)[1][1]:]
def reset():
    global deck, tableau, states, stacks, undeck
    deck = cards.getSortedDeck()
    deck = cards.shuffle(deck)
    undeck = []
    tableau = []
    for col in range(7):
        tableau.append([])
        for card in range(col + 1):
            tableau[col].append(deck.pop())
    stacks = [(0,0) for x in range(4)]
    
    states = [[DOWN, DECK]]*52
    for index, col in enumerate(tableau):
        for rowIndex, card in enumerate(col):
            states[cards.getCardIndex(card)] = [DOWN, [index, rowIndex]]
            if rowIndex == len(col) - 1:
                states[cards.getCardIndex(card)][0] = UP
def turn3():
    global deck, undeck
    if deck == []:
        deck = undeck
        undeck = []
    undeck += deck[:3]
    deck = deck[3:]
        