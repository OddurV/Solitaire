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
	x=Bunki1[num1]
	y=Bunki2[len(Bunki2)-1]
	check1=(x.gildi==y.gildi+1)
	if x.sort=="H" or x.sort=="T":
		check2=(y.sort=="S" or y.sort=="L")
	else:
		check2=(y.sort=="H" or y.sort=="T")
	return check1 and check2

#Fall sem athugar hvort að leikmaðurinn hefur sigrað
#N: Sigra(G)
#F: G er listi af listunum sem öll spilin eiga að enda í
#E: Skilar True ef það eru 13 spil í hverjum lista, annars False
def Sigra(G):
	return len(G[0])==len(G[1]) and len(G[1])==len(G[2]) and len(G[2])==len(G[3]) and len(G[0])==13

#Fall sem athugar hvort að leikmaðurinn hefur tapað
#N: Tapa(?)
#F: ?
#E: Skilar True ef það er enginn leikur mögulegur OG Sigra() skilar False
#   skilar annars False
def Tapa():
	pass
	      
