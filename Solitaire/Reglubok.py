import pygame

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False

myfont = pygame.font.SysFont("monospace", 15)

# render text
label = myfont.render("Markmið spilara er að setja spil stokks í fjóra stafla, þar sem öll", 1, (255,255,0))
screen.blit(label, (10, 10))
label = myfont.render("spil hvers stafla eru af sömu sort og voru sett þangað í þrepvaxandi", 1, (255,255,0))
screen.blit(label, (10, 25))
label = myfont.render("röð.", 1, (255,255,0))
screen.blit(label, (10, 40))

label = myfont.render("Ás flokkast sem lægsta spilið og fyrsta spil hvers stafla verður að", 1, (255,255,0))
screen.blit(label, (10, 65))
label = myfont.render("vera ás. Spil stokks snúa alltaf niður.", 1, (255,255,0))
screen.blit(label, (10, 80))

label = myfont.render("Bunkarnir eru af stærð 1 til 7 í þrepvaxandi röð frá hægri til vinstri.", 1, (255,255,0))
screen.blit(label, (10, 105))
label = myfont.render("Spil bunka snúa niður en ef efsta spil bunka snýr niður má snúa því upp.", 1, (255,255,0))
screen.blit(label, (10, 120))

label = myfont.render("Spilari má taka efsta spil stokks og setja á stafla ef það er hægt.", 1, (255,255,0))
screen.blit(label, (10, 145))
label = myfont.render("Hann má líka setja spilið í annan stafla - svokallaðan ruslastafla. Ef", 1, (255,255,0))
screen.blit(label, (10, 160))
label = myfont.render("stokkurinn er búinn má endurvinna ruslastaflann, en það þýðir að snúa honum", 1, (255,255,0))
screen.blit(label, (10, 175))
label = myfont.render("við og endurnota sem stokk.", 1, (255,255,0))
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
