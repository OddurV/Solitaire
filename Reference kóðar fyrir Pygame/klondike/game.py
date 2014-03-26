import sys, os
localPath = os.path.abspath(sys.argv[0]+"/..")
import pygame

import cards
import gameplay

idler = pygame.time.Clock()

pygame.init()

size = width, height = (1000,700)
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 36)
background = (255,255,255)

cards.Images = Spade, Heart, Diamond, Club = (pygame.image.load(localPath + "/spades.jpg"),
                                              pygame.image.load(localPath + "/hearts.jpg"),
                                              pygame.image.load(localPath + "/diamonds.jpg"),
                                              pygame.image.load(localPath + "/clubs.jpg"))
cardBack = pygame.image.load(localPath + "/back.jpg")

cardDimensions = cardWidth, cardHeight = (75, 110)

#spacing between each card (x)
spacing = 20
tableauOffset = (150,150)
coverFraction = 0.3
undeckFraction = 0.4
stackPosition = (500, 10)
undeckPos = (cardWidth + spacing, 0)
columnRects = [pygame.Rect(x*(cardWidth + spacing) + tableauOffset[0], tableauOffset[1], cardWidth, 800) for x in range(7)]
stackRects = [pygame.Rect(x*(cardWidth + spacing) + stackPosition[0], stackPosition[1], cardWidth, cardHeight) for x in range(4)]
undeckRects = [pygame.Rect(undeckFraction * x*(cardWidth + spacing) + undeckPos[0], undeckPos[1], cardWidth, cardHeight) for x in range(3)]

def renderCard(screen, suit, number, cardRect):
    pygame.draw.rect(screen, (255,255,255), cardRect, 0)
    pygame.draw.rect(screen, (0,0,0), cardRect, 2)
    if suit == cards.DIAMONDS or suit == cards.HEARTS:
        textColor = (255,0,0)
    else:
        textColor = (0,0,0)
    if number != 0:
        text = font.render(cards.getSymbol(number), True, textColor, background)
        
        textRect = text.get_rect()
        pipRect = cards.Images[suit - 1].get_rect()
        pipRect.topleft = map(lambda x,y:x + y, (2, 25), cardRect.topleft)
        textRect.topleft = map(lambda x,y:x+y,cardRect.topleft,(5,2))
        screen.blit(cards.Images[suit - 1], pipRect)
        screen.blit(text, textRect)
def renderBack(screen, cardRect):
    screen.blit(cardBack, cardRect)
def getCardRect(column, row):
    return pygame.Rect(column * (cardWidth + spacing) + tableauOffset[0], row * (cardHeight * coverFraction) + tableauOffset[1], cardWidth, cardHeight)
activeCard = None
activePos = None
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for index, rect in enumerate(columnRects):
                if rect.collidepoint(event.pos):
                    for colIndex ,card in enumerate(gameplay.tableau[index]):
                        cRect = getCardRect(index, colIndex)
                        if cRect.collidepoint(event.pos) and gameplay.states[cards.getCardIndex(card)][0] == gameplay.UP:
                            activeCard = card
                            activeOffset = (cRect.topleft[0] - event.pos[0], cRect.topleft[1] - event.pos[1])
                            activePos = (cRect.topleft[0], cRect.topleft[1])
                            activeCoords = (colIndex, index)
                    break
            undeckIndex = -1
            if len(gameplay.undeck) < 3:
                undeckIndex = len(gameplay.undeck) - 1
            if undeckRects[undeckIndex].collidepoint(event.pos):
                activeCard = gameplay.undeck[-1]
                activeOffset = (undeckRects[undeckIndex].topleft[0] - event.pos[0], undeckRects[undeckIndex].topleft[1] - event.pos[1])
                activePos = (undeckRects[undeckIndex].topleft[0], undeckRects[undeckIndex].topleft[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            if activeCard != None:
                moved = False
                for index, rect in enumerate(columnRects):
                    if rect.colliderect(pygame.Rect(activePos[0], activePos[1], cardWidth, cardHeight)):
                        #ambiguities here! solve later...
                        if gameplay.attemptMove(activeCard, index):
                            moved = True
                            break
                if not moved:
                    for index, rect in enumerate(stackRects):
                        if rect.colliderect(pygame.Rect(activePos[0], activePos[1], cardWidth, cardHeight)):
                            if gameplay.attemptMove(activeCard, index, inTableau=False):
                                moved = True
                                break
                activeCard = None
            else:
                rect = pygame.Rect(0,0,cardWidth,cardHeight)
                if rect.collidepoint(event.pos):
                    gameplay.turn3()
        elif event.type == pygame.MOUSEMOTION:
            if activeCard != None:
                activePos = (event.pos[0] + activeOffset[0], event.pos[1] + activeOffset[1])
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                gameplay.reset()
    screen.fill(background)
    x = tableauOffset[0]
    for col in gameplay.tableau:
        y = tableauOffset[1]
        for card in col:
            if gameplay.states[cards.getCardIndex(card)][0] == gameplay.UP and card != activeCard:
                renderCard(screen, card[0], card[1], pygame.Rect(x,y,cardWidth, cardHeight))
            elif card != activeCard:
                renderBack(screen, pygame.Rect(x,y,cardWidth, cardHeight))
            else:
                break
            y += cardHeight * coverFraction
        x += (cardWidth + spacing)
    for card, rect in zip(gameplay.stacks, stackRects):
        renderCard(screen, card[0], card[1], rect)
    for index, card in enumerate(gameplay.undeck[-3:]):
        if card != activeCard:
            renderCard(screen, card[0], card[1], undeckRects[index])
    if gameplay.deck != []: 
        renderBack(screen, pygame.Rect(0,0,cardWidth, cardHeight))
    if activeCard != None:
        for count, card in enumerate(gameplay.cardsBelow(activeCard)):
            renderCard(screen, card[0], card[1], pygame.Rect(activePos[0],activePos[1] + count * cardHeight * coverFraction, cardWidth, cardHeight))
    pygame.display.flip()
    if activeCard == None:
        idler.tick(20)