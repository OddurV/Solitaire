import pygame

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False

myfont = pygame.font.SysFont("monospace", 15)

# render text
label = myfont.render("Markmi� spilara er a� setja spil stokks � fj�ra stafla, �ar sem �ll", 1, (255,255,0))
screen.blit(label, (10, 10))
label = myfont.render("spil hvers stafla eru af s�mu sort og voru sett �anga� � �repvaxandi", 1, (255,255,0))
screen.blit(label, (10, 25))
label = myfont.render("r��.", 1, (255,255,0))
screen.blit(label, (10, 40))

label = myfont.render("�s flokkast sem l�gsta spili� og fyrsta spil hvers stafla ver�ur a�", 1, (255,255,0))
screen.blit(label, (10, 65))
label = myfont.render("vera �s. Spil stokks sn�a alltaf ni�ur.", 1, (255,255,0))
screen.blit(label, (10, 80))

label = myfont.render("Bunkarnir eru af st�r� 1 til 7 � �repvaxandi r�� fr� h�gri til vinstri.", 1, (255,255,0))
screen.blit(label, (10, 105))
label = myfont.render("Spil bunka sn�a ni�ur en ef efsta spil bunka sn�r ni�ur m� sn�a �v� upp.", 1, (255,255,0))
screen.blit(label, (10, 120))

label = myfont.render("Spilari m� taka efsta spil stokks og setja � stafla ef �a� er h�gt.", 1, (255,255,0))
screen.blit(label, (10, 145))
label = myfont.render("Hann m� l�ka setja spili� � annan stafla - svokalla�an ruslastafla. Ef", 1, (255,255,0))
screen.blit(label, (10, 160))
label = myfont.render("stokkurinn er b�inn m� endurvinna ruslastaflann, en �a� ���ir a� sn�a honum", 1, (255,255,0))
screen.blit(label, (10, 175))
label = myfont.render("vi� og endurnota sem stokk.", 1, (255,255,0))
screen.blit(label, (10, 190))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    
 #   screen.fill((255, 255, 255))
  #  screen.blit(text,
   #     (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    
    pygame.display.flip()
    clock.tick(60)

#                          
# 
