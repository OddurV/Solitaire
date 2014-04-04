# -*- coding: cp1252 -*-
import pygame

from pygame.locals import *
def display():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    done = False

    myfont = pygame.font.SysFont("monospace", 15)

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
    label = myfont.render("stokkurinn er b�inn m� endurvinna ruslastaflann, en �a� ���ir a� sn�a", 1, (255,255,0))
    screen.blit(label, (10, 175))
    label = myfont.render("honum vi� og endurnota sem stokk.", 1, (255,255,0))
    screen.blit(label, (10, 190))

    label = myfont.render("Spilarinn m� l�ka setja efsta spili� ofan � einn bunkann, en a�eins ef", 1, (255,255,0))
    screen.blit(label, (10, 215))
    label = myfont.render("gildi �ess er einum l�gra og �a� er af ��rum lit. T.d. m� laufafjarki", 1, (255,255,0))
    screen.blit(label, (10, 230))
    label = myfont.render("eing�ngu fara ofan � t�gul- e�a hjartafimmu. �s m� eing�ngu fara ofan", 1, (255,255,0))
    screen.blit(label, (10, 245))
    label = myfont.render("� tvist af ��rum lit, og k�ngur m� eing�ngu fara ofan � t�man bunka,", 1, (255,255,0))
    screen.blit(label, (10, 260))
    label = myfont.render("- bunkinn telst enn�� vera til �� a� enginn spil s�u � honum - spilari", 1, (255,255,0))
    screen.blit(label, (10, 285))
    label = myfont.render("m� ekki b�a til t�ma bunka.", 1, (255,255,0))
    screen.blit(label, (10, 300))

    label = myfont.render("Eftir s�mu reglum m� spilari f�ra til efstu spil bunkanna og efstu", 1, (255,255,0))
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

