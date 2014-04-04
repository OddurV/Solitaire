# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random
import pygame.image
import pygame.rect
import os.path
import re
import Reglur
import Buttons  #Klassi af pygame siduni sem byr til takka, litilega breyttur
import time
from Spilastokkur import*


def cardNames():
    s = Spilastokkur()
    cards = s
    return cards
    
    

    '''
    for card_num in range(1, 14) :
        for card_suit in suits :
            str_card = str(card_num) if card_num > 9 else '0' + str(card_num)
            cards.append(card_suit + str_card)
    '''

class Stillingar:
    myndir_nofn = cardNames()
    mynd_path = "Myndir/"
    mynd_gerd = ".jpg"
    mynd_bakhlid = 'Bakhlid'
    mynd_botn = 'bottom03'
    mynd_upplausn = (124, 174)
    upphafs_bil = 10
    rod_bil = 60
    margin_bil = 100
    tile_small_space = 20
    tile_large_space = 15
    double_speed = 500
        
def loadImage(name):
    image =  pygame.image.load(os.path.join(Stillingar.mynd_path, str(name) + Stillingar.mynd_gerd))
    return image.convert_alpha()


#Basic class on which all the other classes will depend
class AbstractObject(object):
    def __init__(self, name, pos):
        #Name of the object
        self.name = name
        #It's position and area (starts of as a 0 dimensional rect)
        self.rect = pygame.Rect(pos[0], pos[1], 0, 0) 

    #Checks if a x, y position is in the object
    def __len__(self):
        return len(self.name)

    def __int__(self):
        return int(self.name)

    def hasPosition(self, pos) :
        if not self.visible : return False
        return self.rect.collidepoint(pos)

    def hasCollision(self, obj) :
        return self.rect.colliderect(obj.rect)

    #Just returns the x, y position of self.rect
    def getPosition(self) :
        return (self.rect.x, self.rect.y)

    #Moving objects might not be as easy as chaing rect.x, so use subclass this if necessary
    def setPosition(self, pos) :
        self.rect.x, self.rect.y = pos[0], pos[1]

    def movePosition(self, move) :
        self.rect.move_ip(move)


#An object that has an image associated with it
#Can be made invisible
class AbstractImage(AbstractObject) :
    def __init__(self, name, pos, image) :
        AbstractObject.__init__(self, name, pos)
        #All objects have an image (surface) associated with them.
        self.image = self.setImage(image) 
        #Will this object be drawn (allows me to easily hide objects, rather than move rect off-screen)
        self.visible = True

    #The simple draw function that needs subclassed to be usefull
    def draw(self, screen) :
        if self.visible :
            screen.blit(image, self.rect)

    #Each object is associated with an image. As soon as the image is loaded, the self.rect attribute needs to be updated
    def setImage(self, image) :
        loaded = loadImage(image)
        self.rect.w, self.rect.h = loaded.get_width(), loaded.get_height()
        return loaded


#The basic container for cards. Subsequent piles will subclass it 
#The image represents the empty pile
class AbstractPile(AbstractImage) :

    def __init__(self, name, pos, image, cards = []) :
        AbstractImage.__init__(self, name, pos, image)
        self.cards = []
        self.addCards(cards)

    #Are there any cards in the pile?
    def isEmpty(self) : 
        if self.cards : return False
        return True

    #How many cards are in the pile
    def cardNum(self) : return len(self.cards)

    #Turns all the cards in the pile faceup or facedown
    def allFaceUp(self, boolean) :
        for card in self.cards :
            card.faceUp = boolean

    #Draws the bottom symbol stored in self.image (generally used to show an empty pile)
    def drawBottom(self, screen) :
        screen.blit(self.image, self.rect)

    #Remove cards from the top of the pile (end of the list)
    def takeCards(self, num) :
         if num > self.cardNum() or num < 0 : raise IndexError
         break_point = self.cardNum() - num
         to_take = self.cards[break_point : ] #Cards that are taken
         self.cards = self.cards [ : break_point] #Cards that remain
         return to_take

    def takeAll(self) :
        return self.takeCards(self.cardNum())

    #The setPosition function moves all the cards, rather than setting the position directly
    #This allows tiled piles to be set correctly, as using setPosition directly would make the tiled pile into simple pile 
    def setPosition(self, pos) :
        x_move = pos[0] - self.rect.x
        y_move = pos[1] - self.rect.y

        super(AbstractPile, self).setPosition(pos)
        for card in self.cards : card.movePosition((x_move, y_move))

    def movePosition(self, move) :
        super(AbstractPile, self).movePosition(move)
        for card in self.cards : card.movePosition(move)

    #Simple function that takes cards and puts them back
    def returnCards(self, cards) :
        self.addCards(cards)

    #The rest of the functions need to be subclassed
    #Add a list of cards to the end of this pile. This is used to populate the pile originally
    def addCards(self, cards) :
        raise NotImplementedError

    def draw(self, screen) :
        raise NotImplementedError


#This is the abstract class for a pile where all the cards are exactly on top of each other
#It is fully functional if you want to just display this pile, but cannot be interacted with by user
class AbstractSimplePile(AbstractPile) :
    def __init__(self, name, pos, image, cards = []) :
        AbstractPile.__init__(self, name, pos, image, cards)

    #The draw call does not draw all the cards in the pile
    #Only the top card is drawn, as it hides all the other cards
    def draw(self, screen) :
        if not self.visible : return

        if  self.isEmpty():
            self.drawBottom(screen)

        else :
            self.cards[-1].draw(screen)

    #Can a cards be added to this pile by the user (for this class, always no)
    def validAddCards(self, pile) :
        return False

    #Add a single card (the card keeps track of where it was last added)
    def addSingle(self, card) :
        card.setPosition((self.rect.x, self.rect.y))
        card.pile = self
        self.cards.append(card)

    #Add cards to this pile
    #If you just want to know if cards could be added by user, run validAddPile
    def addCards(self, cards) :
        for card in cards : self.addSingle(card)


#The cards are now spread out vertically (with the last card in the list at the top)
#The tile pile has two spacings between cards
#init_space for the spacing when the pile is just created and add_space for the spacing when new cards are added
class AbstractTilePile(AbstractPile):
    def __init__(self, name, pos, image, init_space, add_space, cards = []) :
        self.init_space = init_space
        self.add_space = add_space*1.6
        AbstractPile.__init__(self, name, pos, image, cards)

    def draw(self, screen) :
        if not self.visible : return
        if self.isEmpty(): self.drawBottom(screen)
        for card in self.cards : card.draw(screen)

    #Can a cards be added to this pile by the user (for this class, always no)
    def validAddCards(self, pile) :
        return False

    #This function is a little strained as it has to determine if a card is being added by the user
    #Or if cards are being returned to a pristine tiled pile
    #This is to ensure that the tile spacing does arbitarily switch
    def addSingle(self, card) :
        if self.isEmpty() :
            card.setPosition((self.rect.x, self.rect.y))
        else :
            last_card = self.cards[-1]
            #If the last card is faceUp, add the card with add_space spacing
            if last_card.faceUp : card.setPosition((last_card.rect.x, last_card.rect.y + self.add_space))
            #If the last card is faceDown, it means the card should be added with the init_space
            else : card.setPosition((last_card.rect.x, last_card.rect.y + self.init_space))

        card.pile = self
        self.cards.append(card)
        self.updateArea() #Don't forget to update the new area

    #Add cards to this pile
    #If you just want to know if cards could be added by user, run validAddPile
    def addCards(self, cards) :
        for card in cards : self.addSingle(card)

    #The rect area actually gets bigger as more cards are added, so it needs to be updated
    def updateArea(self) :
        if self.isEmpty() : 
            ref = self.image.get_rect()
            self.rect.h= ref.h

        else : #The hight of the tiled pile is simply the difference between the top of first and bottom of last card
            bottom = self.cards[-1].rect.bottom
            top = self.cards[0].rect.top
            self.rect.h = bottom - top

    #Remove cards from the top of the pile (end of the list)
    #Had to be subclassed to ensure the area is correctly updated
    def takeCards(self, num) :
        result = super(AbstractTilePile, self).takeCards(num)
        self.updateArea()
        return result

#A abstract class that can hold multiple piles if those piles need to talk to each other
#It does not have an image by itself, so self.rect has no dimension
#Which means that hasPosition has to be subclassed to allow user interaction and define pile interactions
class AbstractMultiPile(AbstractObject) :
    def __init__(self, name, pos, space) :
        AbstractObject.__init__(self, name, pos)
        self.space = space
        self.piles = []

    #Each added pile is spaced by self.space from the previous pile
    def setupPile(self, new_pile) :
        displace = 0
        for pile in self.piles :
            displace += pile.rect.width + self.space 
        new_pile.setPosition((self.rect.x + displace, self.rect.y))
        self.piles.append(new_pile)

    #Is a pile located at that position (return None if there is nothing)
    def getPile(self, pos) :
        for pile in self.piles :
            if pile.hasPosition(pos) : return pile

    def hasPosition(self, pos) :
        if self.getPile(pos) : return True
        return False

    def movePosition(self, move) :
        for pile in self.piles :
            pile.movePosition(move)

    def draw(self, screen) :
        for pile in self.piles :
            pile.draw(screen)
                        
class Card(AbstractImage) :
    #The back of card image is stored here (it is the same for all cards)
    #Set if with self.loadBack()
    back_of_card = None

    #As static members are loaded before __main__ I cannot load the back_of_card image right away
    #This is because abstract.loadImage() calls a pygame function (convert_alpha) that requires pygame.init() to be called
    #This static function can be called to load the back_of_card image
    @staticmethod
    def loadBack(name) :
        Card.back_of_card = loadImage(name)

    #The two colors of the cards
    RED = 1
    BLACK = 2

    def __init__(self, name, pos) :
        #The name of the card is 01-13[cdhs]
        #Notice that the image for the card is specified by its name
        AbstractImage.__init__(self, name, pos, name)
        

        #Sometimes it is necessary to keep track of what pile a card is in
        self.pile = None

        self.faceUp = True

    def getNumber(self):
        number = map(str, re.findall(r'\d+', str(self.name)))
        number = ''.join(number)
        number = int(number)
        return number
 
    def getSuit(self): return self.name[0]

    def getColor(self):
        if self.getSuit() == 't' or self.getSuit() == 'h' : return Card.RED
        else: return Card.BLACK

    def sameColor(self, card) :
        return self.getColor() == card.getColor()

    def draw(self, screen) :
        if self.visible :
            image = self.image if self.faceUp else Card.back_of_card
            screen.blit(image, self.rect)

#Encodes the draw and discard pile of the game
#The left draw pile if face down and upon click moves the top card onto the right discard pile faceup
#If the draw pile is empty, it takes all the cards from the discard pile
class StartPile(AbstractMultiPile) :
    DRAW = 0
    DISCARD = 1

    def __init__(self, name, pos, space, bottom, cards = []) :
        AbstractMultiPile.__init__(self, name, pos, space)
        self.setupPile(self.setupDraw(cards, bottom))
        self.setupPile(self.setupDiscard(bottom))

    #For the two setup functions, the position does not matter, as the setupPile function will correctly position the piles
    def setupDraw(self, cards, bottom) :
        draw_pile = AbstractSimplePile('Draw', (0,0), bottom, cards)
        draw_pile.allFaceUp(False)
        return draw_pile

    def setupDiscard(self, bottom) :
        discard_pile = AbstractSimplePile('Discard', (0,0), bottom)
        return discard_pile

    # If the draw pile is clicked 
    def drawUpClick(self) :
        if not self.piles[StartPile.DRAW].isEmpty() : 
            take_cards = self.piles[StartPile.DRAW].takeCards(1) #If the pile is not empty, get the top most card
            take_cards[0].faceUp = True
            self.piles[StartPile.DISCARD].addCards(take_cards) #Add the card to discard

        else : #Otherwise, move all the cards from discard to draw and but them facedowm
            self.piles[StartPile.DISCARD].allFaceUp(False)
            all_cards = self.piles[StartPile.DISCARD].takeAll()
            all_cards.reverse()
            self.piles[StartPile.DRAW].addCards(all_cards)

    #On click
    def onClick(self, event) :
        clicked_pile = self.getPile(event.pos)

        if not clicked_pile : return #Sanity check, just in case onClick was called accidentaly
        if not clicked_pile.visible: return

        if event.type == MOUSEBUTTONUP and event.button == 1 :
            if clicked_pile.name == 'Draw' : 
                self.drawUpClick()

        #Discard pile just returns the top card in a pile
        if event.type == MOUSEBUTTONDOWN and event.button == 1 :
            if clicked_pile.name == 'Discard' and not clicked_pile.isEmpty(): return clicked_pile.takeCards(1)

    #Double click is always MOUSEUP.
    #For the draw pile, does the same as single click
    #THe discard pile does not respond to single up clicks, but the double click takes the top card
    def onDoubleClick(self, event) :
        clicked_pile = self.getPile(event.pos)
        if not clicked_pile : return #Sanity check, just in case onClick was called accidentaly
        if not clicked_pile.visible: return

        if clicked_pile.name == 'Draw' : self.drawUpClick()
        if clicked_pile.name == 'Discard' and not clicked_pile.isEmpty() : return clicked_pile.takeCards(1)

    #Can cards be added to any of the piles
    def validAddCards(self, cards) :
        return False



#The 7 tiled piles that make up the main playing field
class MainPile(AbstractTilePile) :
    def __init__(self, name, pos, image, init_space, add_space, cards = []) :
        self.pileSetup(cards)
        AbstractTilePile.__init__(self, name, pos, image, init_space, add_space, cards)

    #All but the last card in the pile is facedown
    def pileSetup(self, cards) :
        for card in cards : card.faceUp = False
        if cards: cards[-1].faceUp = True

    #This function returns the top most card on the deck that was clicked
    #If no card was clicked, returns -1
    def topCardClicked(self, pos) :
        result = -1
        for i, card in enumerate(self.cards) :
            if card.hasPosition(pos) : result = i

        return result

    def onClick(self, event) :
        if not self.visible : return

        #When clicked down, return all the cards including and after the card clicked
        if event.type == MOUSEBUTTONDOWN and event.button == 1 :
            card_clicked = self.topCardClicked(event.pos)
            if card_clicked != -1 and self.cards[card_clicked].faceUp:
                cards_to_take = self.cardNum() - card_clicked
                return self.takeCards(cards_to_take)

        #If the last card in the pile if face down, an upclick will turn in around
        if event.type == MOUSEBUTTONUP and event.button == 1 :
            if not self.isEmpty() and self.cards[-1].hasPosition(event.pos) :
                self.cards[-1].faceUp = True

    #Returns the last card in the pile if it is faced up and has been clicked
    def onDoubleClick(self, event) :
        if not self.visible : return

        card_clicked = self.topCardClicked(event.pos)
        if card_clicked != -1 and self.cards[card_clicked].faceUp and card_clicked == self.cardNum() - 1:
            return self.takeCards(1)

    #can these cards be added to this pile by the user
    #We only care about the first card in cards
    #implicit assumption is that the rest of the program makes sure the order of the cards remains valid
    def validAddCards(self, cards) :
        #Only a king can be added to an empty pile
        if self.isEmpty() :
            if cards[0].getNumber() == 13 and self.hasCollision(cards[0]) : 
                return True
        else:
            ref_card = self.cards[-1] # The top most card of the pile determines validity
            if not ref_card.faceUp : #Card must be faceup to be seen when it is added to
                return False 

            if not ref_card.sameColor(cards[0]) and ref_card.getNumber() == cards[0].getNumber() + 1 :
                if ref_card.hasCollision(cards[0]) : 
                    return True

        return False


#A simple pile that only allows addition of one card with increasing value with the same suit
#When empty, can accept only aces (the ace added will determine the suit)
#Keeps track of how many cards have been added to any SuitPile (for the win condition of 52)
class SuitPile(AbstractSimplePile) :
    total_cards = 0

    def __init__(self, name, pos, image) :
        AbstractSimplePile.__init__(self, name, pos, image)

    #validAddCards has to be expended
    #If contact is true, the added card must be in touch with the suit pile
    #This matters because double clicking a card can directly move it to a suit pile
    def validAddCards(self, cards, contact = True) :
        if contact : 
            if not self.hasCollision(cards[0]): return False
        if len(cards) != 1 : return False

        if self.isEmpty() :
            if cards[0].getNumber() == 1: return True
            return False

        ref_card = self.cards[-1]
        if ref_card.getSuit() == cards[0].getSuit() and ref_card.getNumber() + 1 == cards[0].getNumber() :
            return True
        return False

    #On click
    def onClick(self, event) :
        if not self.visible : return False

        if event.type == MOUSEBUTTONDOWN and event.button == 1 :
            if not self.isEmpty(): return self.takeCards(1)

    def onDoubleClick(self, event) :
        pass

    #To keep track of the total number of cards in SuitPiles, add and take card function need to be expanded
    def takeCards(self, num) :
        cards_taken = super(SuitPile, self).takeCards(num)
        SuitPile.total_cards -= num
        return cards_taken

    def addSingle(self, card) :
        super(SuitPile, self).addSingle(card)
        SuitPile.total_cards += 1

#This class allows for cards to be easily moved around
#It takes cards from a pile and keeps them in the same relative positions while they are moved around
#It also keeps track of where the cards came from and can return it if necessary
class Repository(object) :
    def __init__(self, name) :
        self.name = name
        self.cards = []
        self.source = None

    def addCards(self, cards) :
        if self.source or self.cards : raise Exception
        if cards :
            self.cards = cards
            self.source = cards[0].pile

    def hasCards(self) : 
        if self.cards : return True
        return False

    def clear(self) :
        self.cards = []
        self.source = None

    def returnCards(self) :
        self.source.addCards(self.cards)
        self.clear()

    #Move the card to the pile (please check if the move if valid first)
    def addToPile(self, pile) :
        pile.addCards(self.cards)
        self.clear()
 
    def draw(self, screen) :
        for card in self.cards : card.draw(screen)

    def movePosition(self, move) :
        for card in self.cards : card.movePosition(move)
                
class DoubleClick :
    def __init__(self) :
        self.double_click = pygame.time.Clock()
        self.time = 0 #Necessary to temporary store time passed after checking second down click
        self.first_click = True #Is this the first click in the double click
        self.wasDC = False #Was the alst call to isDC() a double click

    #Implementing double click was a lot harder than initially thought
    #A double click starts on a mouse down and ends on the second mouse up
    #If there is too much time between the first and second mouse down, the second mouse down will be treated as a first
    def isDC(self, event) :
        if event.type == MOUSEBUTTONDOWN and event.button == 1 :
            click_time = self.double_click.tick() #Check how long since last click
            if not self.first_click : #If it's the first click, exit function with False
                #If it's the second downclick, make sure that a double click is still a possibility 
                #If not, make this down click the first click
                #Since tick() was called, store time passed in self.time, to be added to the upclick later
                if click_time > Stillingar.double_speed : self.first_click = True
                else : self.time = click_time

        if event.type == MOUSEBUTTONUP and event.button == 1 :
            if not self.first_click : #If it's the second click
                click_time = self.double_click.tick() #Get time since last click (the second down click)
                self.first_click = True #The next click will again be first
                if click_time + self.time < Stillingar.double_speed : #Add the click_time and self.time and check if fast enough
                    self.wasDC = True 
                    return True
            else : self.first_click = False #If it was first first upclick, now the second_click is expected
        #If we get to here, no double click was detected    
        self.wasDC = False
        return False


class Game :
    def __init__(self) :
        pygame.init()
        random.seed()

        self.screen = self.setDisplay() #Display dimensions
        self.double_click = DoubleClick() #Double click checker
        self.move_pile = Repository('Repository') #For moving piles
        
        self.cards = self.loadCards() #All the cards
        self.piles = self.populatePiles() #All the piles

    #The display dimensions are calculated given the wanted margins and card dimensions
    def setDisplay(self) :
        x_dim = (Stillingar.margin_bil * 2) + (Stillingar.mynd_upplausn[0] * 7) + (Stillingar.upphafs_bil * 6)
        y_dim = Stillingar.margin_bil + (Stillingar.mynd_upplausn[1] * 2) + Stillingar.rod_bil
        y_dim += (Stillingar.tile_small_space * 6) + (Stillingar.tile_large_space * 12)
        return pygame.display.set_mode((x_dim, y_dim))

    #Load the cards (the common card back and the card images)
    def loadCards(self) :
        Card.loadBack(Stillingar.mynd_bakhlid)
        cards = [Card(x, (0, 0)) for x in Stillingar.myndir_nofn]
        random.shuffle(cards)
        return cards

    
    #Place the piles (are reset the SuitPile win number down to 0)
    def populatePiles(self) :
        piles = []
        suit_piles = []
        SuitPile.total_cards = 0

        marker = 0 #Keeps track of the last card added
        x = Stillingar.margin_bil #The x_position of the pile
        y = Stillingar.margin_bil + Stillingar.mynd_upplausn[1] + Stillingar.rod_bil
        for i in range(1,8) : #Need seven main piles
            pile_name = 'Main' + str(i)
            cards = self.cards[marker : i + marker] #Each pile position also tells me how many cards it needs
            piles.append(MainPile(pile_name, (x, y), Stillingar.mynd_botn, Stillingar.tile_small_space, Stillingar.tile_large_space, cards))

            #The suit piles are exactly above main piles (starting on the four one)
            if i > 3 : suit_piles.append(SuitPile('Suit' + str(i - 3), (x, Stillingar.margin_bil), Stillingar.mynd_botn))

            #tick along x and marker
            x += piles[-1].rect.w + Stillingar.upphafs_bil
            marker = i + marker

        #Add the start pile 
        cards = self.cards[marker : 52] #The remaining cards
        piles.append(StartPile('Start', (Stillingar.margin_bil, Stillingar.margin_bil), Stillingar.upphafs_bil, Stillingar.mynd_botn, cards))

        piles.extend(suit_piles) #The last four piles always must be the suit piles
        return piles

    #simply gets the pile that was clicked (none if no pile was clicked)
    def clickedPile(self, event) :
        for pile in self.piles :
            if pile.hasPosition(event.pos) : return pile

    #The basic idea of the game loop is thus :
    #If a pile is clicked, onClick() is run
    #If onClick() returns cards, this means that these cards can be moved around (while mouse is held down)
    #The moving of cards is performed by self.move_pile
    #With a double click, the down, up, and and click are read as single clicks (and still run as such)
    #The lst up click will result in onDoubleClick being called 
    def gameLoop(self) :
        background_image = pygame.image.load("./Myndir/Backgr.jpg").convert()                                
        background_position = [0, 0]                                       
        self.Button1 = Buttons.Button() 
        self.Button2 = Buttons.Button()
        self.StartTime=time.time()
        myfont = pygame.font.SysFont("impact", 20)
        while True :
            self.EndTime=time.time()
            self.TimeElapsed=self.EndTime - self.StartTime
            S = int(self.TimeElapsed)
            round(S,0)
            T = str(S)
            print(S)
            
            if self.winCondition(): 
                self.browninanMotion(2) #Move the piles around randomly if game has been won

            for event in pygame.event.get() :
                #Check and store if a double click occured
                if (event.type == MOUSEBUTTONUP or event.type == MOUSEBUTTONDOWN) and event.button == 1 :
                    self.double_click.isDC(event)

                #Check if the program is quit
                if event.type == QUIT :
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit

                #Pressing r resets the program
                if event.type == KEYUP and event.key == K_r :
                    self.reset()

                #If the game has been won, reset it with a mouse click
                if self.winCondition():
                    if event.type == MOUSEBUTTONUP and event.button == 1 :
                        self.reset()
                        
                if event.type == MOUSEBUTTONDOWN and self.Button1.pressed(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit

                if event.type == MOUSEBUTTONDOWN and self.Button2.pressed(pygame.mouse.get_pos()):
                    self.reset()

                #Now for the main meat of the program
                else :
                    if event.type == MOUSEBUTTONUP and event.button == 1 :
                        #Is the user currently dragging cards (and now wants to let them go)
                        #I store it as the I need to check this variable again later and the cards might have been released
                        move_pile_full = self.move_pile.hasCards() 

                        if move_pile_full : #If yes
                            #This finds the left most pile where the dropped cards are accepted
                            selected_pile = None
                            for pile in self.piles :
                                if pile.validAddCards(self.move_pile.cards) : 
                                    selected_pile = pile
                                    break

                            #If a valid pile is found, drop the cards there, otherwise return the cards
                            if selected_pile : self.move_pile.addToPile(selected_pile)
                            else : self.move_pile.returnCards()



                        #If the move_pile was empty and no double click, just run a simple onClick on the pile
                        if not move_pile_full and not self.double_click.wasDC :
                            clicked_pile = self.clickedPile(event)

                            if clicked_pile :
                                clicked_pile.onClick(event)

                    #If mouse is held down, move those cards to the self.move_pile
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                        clicked_pile = self.clickedPile(event)

                        if clicked_pile :
                            cards_taken = clicked_pile.onClick(event)
                            if cards_taken : self.move_pile.addCards(cards_taken)

                    #if the mouse is moved, move the mouse_pile (if it has cards)
                    if event.type == MOUSEMOTION :
                        if self.move_pile.hasCards() : self.move_pile.movePosition(event.rel)

            
            self.screen.blit(background_image, background_position)
            label = myfont.render((T), 1, (255,60,0))
            self.screen.blit(label, (560,0))
            self.Button1.create_button(self.screen, (255,0,60), 0, 0, 120,    30,    0,        "Loka Leik", (0,0,0)) 
            self.Button2.create_button(self.screen, (255,0,60), 120, 0, 120,    30,    0,        "Nyr Leikur", (0,0,0))
            #Kommentadi thetta ut i bili, var ad koma i veg fyrir ad bakgrunnur virkadi
            #self.screen.fill((0, 0, 0))                                                                            
            self.draw()
            pygame.display.flip()




    
        

    #Draw is simple, just draw all the piles
    def draw(self) :
        for pile in self.piles :
            pile.draw(self.screen)

        self.move_pile.draw(self.screen)

    def start(self) :
        self.gameLoop()

    #When all the cards are in the suit pile
    def winCondition(self) :
        return SuitPile.total_cards == len(self.cards)

    #Moves the piles randomly in all directions (the length arguement specifies how hard they move)
    def browninanMotion(self, length) :
        for pile in self.piles :
            x_move = random.randint(-length, length)
            y_move = random.randint(-length, length)
            pile.movePosition((x_move, y_move))

    def reset(self) :
        self.cards = self.loadCards()
        self.piles = self.populatePiles()

if __name__ == "__main__": 
    g = Game()
    g.start()
