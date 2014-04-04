# -*- coding: cp1252 -*-
import pygame

from pygame.locals import *
def display():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    done = False

    myfont = pygame.font.SysFont("monospace", 15)

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
    label = myfont.render("stokkurinn er búinn má endurvinna ruslastaflann, en það þýðir að snúa", 1, (255,255,0))
    screen.blit(label, (10, 175))
    label = myfont.render("honum við og endurnota sem stokk.", 1, (255,255,0))
    screen.blit(label, (10, 190))

    label = myfont.render("Spilarinn má líka setja efsta spilið ofan á einn bunkann, en aðeins ef", 1, (255,255,0))
    screen.blit(label, (10, 215))
    label = myfont.render("gildi þess er einum lægra og það er af öðrum lit. T.d. má laufafjarki", 1, (255,255,0))
    screen.blit(label, (10, 230))
    label = myfont.render("eingöngu fara ofan á tígul- eða hjartafimmu. Ás má eingöngu fara ofan", 1, (255,255,0))
    screen.blit(label, (10, 245))
    label = myfont.render("á tvist af öðrum lit, og kóngur má eingöngu fara ofan á tóman bunka,", 1, (255,255,0))
    screen.blit(label, (10, 260))
    label = myfont.render("- bunkinn telst ennþá vera til þó að enginn spil séu í honum - spilari", 1, (255,255,0))
    screen.blit(label, (10, 285))
    label = myfont.render("má ekki búa til tóma bunka.", 1, (255,255,0))
    screen.blit(label, (10, 300))

    label = myfont.render("Eftir sömu reglum má spilari færa til efstu spil bunkanna og efstu", 1, (255,255,0))
    screen.blit(label, (10, 325))
    label = myfont.render("spil staflanna.", 1, (255,255,0))
    screen.blit(label, (10, 340))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
        
        pygame.display.flip()
        clock.tick(60)

