import pygame
import sys
from objects import *
from general import SolSet
from pygame.locals import *
import random

class DoubleClick:
        def __init__(self):
                self.double_click = pygame.time.Clock()
                self.time = 0
                self.first_click = True
                self.wasDC = False

        def isDC(self, event):
                if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                         click_time = self.double_click.tick()
                         if not self.first_click:
                                 if click_time > SolSet.double_speed: self.first_click = True
                                 else: self.time = click_time

                if event.type == MOUSEBUTTONUP and event.button == 1:
                        if not self.first_click:
                                click_time = self.double_click.tick()
                                self.first_click = True
                                if click_time + self.time < SolSet.double_speed:
                                        self.wasDC = True 
                                        return True
                        else : self.first_click = False
                self.wasDC = False
                return False


class Game:
        def __init__(self):
                pygame.init()
                random.seed()
                self.screen = self.setDisplay()
                self.double_click = DoubleClick()
                self.move_pile = Repository('Repository') 

                self.cards = self.loadCards() 
                self.piles = self.populatePiles() 

        def setDisplay(self) :
                x_dim = (SolSet.margin_space * 2) + (SolSet.image_resolution[0] * 7) + (SolSet.start_space * 6)
                y_dim = SolSet.margin_space + (SolSet.image_resolution[1] * 2) + SolSet.row_space
                y_dim += (SolSet.tile_small_space * 6) + (SolSet.tile_large_space * 12)
                return pygame.display.set_mode((x_dim, y_dim))

        def loadCards(self) :
                Card.loadBack(SolSet.image_back)
                cards = [Card(x, (0, 0)) for x in SolSet.image_names]
                random.shuffle(cards)
                return cards

        def populatePiles(self) :
                piles = []
                suit_piles = []
                SuitPile.total_cards = 0

                marker = 0 
                x = SolSet.margin_space
                y = SolSet.margin_space + SolSet.image_resolution[1] + SolSet.row_space
                for i in range(1,8):
                        pile_name = 'Main' + str(i)
                        cards = self.cards[marker : i + marker]
                        piles.append(MainPile(pile_name, (x, y), SolSet.image_bottom, SolSet.tile_small_space, SolSet.tile_large_space, cards))
                        if i > 3 : suit_piles.append(SuitPile('Suit' + str(i - 3), (x, SolSet.margin_space), SolSet.image_bottom))
                        x += piles[-1].rect.w + SolSet.start_space
                        marker = i + marker

                cards = self.cards[marker : 52]
                piles.append(StartPile('Start', (SolSet.margin_space, SolSet.margin_space), SolSet.start_space, SolSet.image_bottom, cards))

                piles.extend(suit_piles) 
                return piles

        def clickedPile(self, event):
                for pile in self.piles:
                        if pile.hasPosition(event.pos): return pile

        def gameLoop(self):
                while True:
                    if self.winCondition(): 
                        self.browninanMotion(2) 
        
                    for event in pygame.event.get():
                        if (event.type == MOUSEBUTTONUP or event.type == MOUSEBUTTONDOWN) and event.button == 1 :
                            self.double_click.isDC(event)

                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()  

                        if event.type == KEYUP and event.key == K_r:
                            self.reset()

                        if self.winCondition():
                            if event.type == MOUSEBUTTONUP and event.button == 1:
                                self.reset()

                        else :
                            if event.type == MOUSEBUTTONUP and event.button == 1:
                                move_pile_full = self.move_pile.hasCards() 

                                if move_pile_full: 
                                    selected_pile = None
                                    for pile in self.piles :
                                        if pile.validAddCards(self.move_pile.cards): 
                                            selected_pile = pile
                                            break
                                    if selected_pile: self.move_pile.addToPile(selected_pile)
                                    else : self.move_pile.returnCards()

                                if self.double_click.wasDC: self.onDoubleClick(event)

                                if not move_pile_full and not self.double_click.wasDC:
                                    clicked_pile = self.clickedPile(event)

                                    if clicked_pile:
                                        clicked_pile.onClick(event)

                            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                                clicked_pile = self.clickedPile(event)

                                if clicked_pile:
                                    cards_taken = clicked_pile.onClick(event)
                                    if cards_taken: self.move_pile.addCards(cards_taken)

                            if event.type == MOUSEMOTION:
                                if self.move_pile.hasCards(): self.move_pile.movePosition(event.rel)

                    self.screen.fill((0, 0, 0))
                    self.draw()
                    pygame.display.flip()


        def onDoubleClick(self, event):
                clicked_pile = self.clickedPile(event)

                if clicked_pile:

                    card_taken = clicked_pile.onDoubleClick(event)
                    if card_taken :
                        no_home = True 
                        for pile in self.piles[-4:] :

                            if pile.validAddCards(card_taken, False) : 
                                pile.addCards(card_taken)
                                no_home = False
                                break;

                        if no_home : card_taken[0].pile.addCards(card_taken)
        def draw(self):
                for pile in self.piles :
                    pile.draw(self.screen)

                self.move_pile.draw(self.screen)

        def start(self):
                self.gameLoop()

        def winCondition(self):
                return SuitPile.total_cards == len(self.cards)

        def browninanMotion(self, length):
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
