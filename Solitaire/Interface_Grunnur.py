import pygame
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

#Fjarlaegdir i layout:

pygame.init()
  
# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
#Loop until the user clicks the close button.
done = False
RenderList=[] 
MousePressed=False 
MouseDown=False
MouseReleased=False
Target=None
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
#Placeholder fyrir leikjaluppuna
while not done:
    # --- Main event loop
    #screen.fill((0,0,0))

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            
    # --- Game logic should go here
    #Músaevent

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if B1.collidepoint(pos):
                click1 = pos
                B1.move(event.pos[0],event.pos[1])
                #print(pos)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # print(event.pos)
                click2 = event.pos
                x_hnit = click2[0] - click1[0]
                y_hnit = click2[1] - click1[1]
                stada = (x_hnit, y_hnit)
                B1.x += x_hnit
                B1.y += y_hnit
                #B1.move(x_hnit, y_hnit)
                pygame.draw.rect(screen, RED, B1, 1)
                if B1.colliderect(G1):
                    print('virkadi')
                #print(x_hnit)
                #print(y_hnit)
                #print(B1.x)
                #print(B1.y)
                #self.rect.x, self.rect.y = pos[0], pos[1]
                #print("B1")
                #x_hnit = pos[0] - B1.x
                #y_hnit = pos[1] - B1.y
                #B1.move_ip(move)
                #print(x_hnit)
                #print(y_hnit)     
        #else:
 
        pygame.display.flip()
                #pygame.display.flip()
            #if event.type == pygame.MOUSEMOTION:
                   #x1, y1 = pygame.mouse.get_pos()
                    #print(x1)
                    #print(y1)

    """
           inHandSurf.set_colorkey((0,0,0))
            spiderWindow.blit(background, (0,0))
            inHandX = mouse[0] - offset[0]
            inHandY = mouse[1] - offset[1]
            inHandPos = (inHandX,inHandY)
            spiderWindow.blit(inHandSurf, inHandPos)
            inHandRect.x = inHandX
            inHandRect.y = inHandY
    """

    """
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
        print "You pressed the left mouse button at (%d, %d)" % event.pos
    elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
        print "You released the left mouse button at (%d, %d)" % event.pos

    """


    """
            def setPosition(self, pos) :
		x_move = pos[0] - self.rect.x
		y_move = pos[1] - self.rect.y

		super(AbstractPile, self).setPosition(pos)
		for card in self.cards : card.movePosition((x_move, y_move))
    """
    """
	def hasPosition(self, pos) :
		if self.getPile(pos) : return True
		return False
    """
    """
	def getPile(self, pos) :
		for pile in self.piles :
			if pile.hasPosition(pos) : return pile
    """
    """
        def clickedPile(self, event):
                for pile in self.piles:
                        if pile.hasPosition(event.pos): return pile
    """
    """
	def setPosition(self, pos) :
		self.rect.x, self.rect.y = pos[0], pos[1]

	def movePosition(self, move) :
		self.rect.move_ip(move)

    """
                    
    # --- Drawing code should go here
    #Bakgrunnur
    screen.fill(GREEN)
    #kassar teiknaðir eftir pygame.draw.rect(screen, color, (x,y,width,height), thickness)
    #Thetta er til að nota sem vidmid thegar layout er sett upp
    #B
    B1 = pygame.draw.rect(screen, RED, (10,348,124,174), 0)
    B2 = pygame.draw.rect(screen, BLACK, (154,348,124,174), 0)
    B3 = pygame.draw.rect(screen, BLACK, (298,348,124,174), 0)
    B4 = pygame.draw.rect(screen, BLACK, (442,348,124,174), 0)
    B5 = pygame.draw.rect(screen, BLACK, (586,348,124,174), 0)
    B6 = pygame.draw.rect(screen, BLACK, (730,348,124,174), 0)
    B7 = pygame.draw.rect(screen, BLACK, (874,348,124,174), 0)
    #B2 = pygame.image.load("h1.jpeg")
    #S
    S = pygame.draw.rect(screen, BLACK, (10,20,124,174), 0)
    #E
    E = pygame.draw.rect(screen, BLACK, (154,20,124,174), 0)
    #G
    G1 = pygame.draw.rect(screen, RED, (442,20,124,174), 0)
    G2 = pygame.draw.rect(screen, BLACK, (586,20,124,174), 0)
    G3 = pygame.draw.rect(screen, BLACK, (730,20,124,174), 0)    
    G4 = pygame.draw.rect(screen, BLACK, (874,20,124,174), 0)

    #screen.blit(B2, B1)

     
    # Fall til ad uppfaera skjainn
    pygame.display.flip()
 
    #Stilli a 60 fps
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

"""

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
"""
