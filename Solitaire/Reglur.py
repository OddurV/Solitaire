# -*- coding: utf-8 -*-
import Spilastokkur

#Leikreglur

#Fall sem athugar hvort að leikurinn er löglegur
#Skilar True eða False
#N: legalMove(Bunki1,Bunki2,num1,num2)
#F: Bunki1 og Bunki2 eru listar, num1 og num2 eru heiltölur
#   0<=num1<=num2<len(Bunki1)
#E: Skilar True ef það er leyfilegt að færa spilarununa sem
#   er á bilinu num1 til num2, úr bunka 1 og í bunka 2.
#   Annars er False skilað
def legalMove(Bunki1,Bunki2,num1,num2):
	pass

#Fall sem athugar hvort að leikmaðurinn hefur sigrað
#N: Sigra(G1,G2,G3,G4)
#F: G1-4 eru listarnir sem öll spilin eiga að enda í
#E: Skilar True ef það eru 13 spil í hverjum lista, annars False
def Sigra(G1,G2,G3,G4):
	pass

#Fall sem athugar hvort að leikmaðurinn hefur tapað
#N: Tapa(?)
#F: ?
#E: Skilar True ef það er enginn leikur mögulegur OG Sigra() skilar False
#   skilar annars False
def Tapa():
	pass
	      
