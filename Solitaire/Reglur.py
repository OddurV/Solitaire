# -*- coding: utf-8 -*-
#import Spilastokkur

#Leikreglur


# Fall sem skilar true ef það má setja Spil1 ofan á Spil2 
# miðað við reglur fyrir að setja ofan á bunka
def PassaSaman(Spil1, Spil2):
    rjettGildiZ = (Spil1.gildi==Spil2.gildi+1)
    if x.sort=="H" or x.sort=="T":
        rjettSortZ=(y.sort=="S" or y.sort=="L")
    else:
        rjettSortZ=(y.sort=="H" or y.sort=="T")
    return rjettGildiZ and rjettSortZ

#Fall sem athugar hvort að leikurinn er löglegur
#Skilar True eða False
#N: LeyfilegHreyfing(Bunki1,Bunki2,num1,num2)
#F: Bunki1 og Bunki2 eru listar, num1 og num2 eru heiltölur
#   0<=num1<=num2<len(Bunki1)
#E: Skilar True ef það er leyfilegt að færa spilarununa sem
#   er á bilinu num1 til num2, úr bunka 1 og í bunka 2.
#   Annars er False skilað
def LeyfilegHreyfing(Bunki1,Bunki2,num):
	x=Bunki1[num]
	y=Bunki2[-1]
	return PassaSaman(x,y)


#Fall sem athugar hvort að það má færa spilið upp í lokabunka (G)
#N: LeyfilegLokahreyfing(Bunki1,G,num1)
#F: Bunki1 og G eru listar
#E: Skilar True ef það er leyfilegt að færa aftasta spilið í bunka1
#   yfir í G
def LeyfilegLokahreyfing(Bunki1,G):
    spil_a_bunka  = Bunki1[-1]
    spil_a_stokki = G[-1]
    rjettGildiZ = (spil_a_bunka.gildi==spil_a_stokki.gildi+1)
    rjettSortZ = (spil_a_bunka.sort==spil_a_stokki)
    return check1 and check2
	
#Fall sem athugar hvort að leikmaðurinn hefur sigrað
#N: Sigra(G)
#F: G er listi af listunum sem öll spilin eiga að enda í
#E: Skilar True ef það eru 13 spil í hverjum lista, annars False
def Sigra(G):
	return len(G[0])==len(G[1]) and len(G[1])==len(G[2]) and len(G[2])==len(G[3]) and len(G[0])==13

#Fall sem athugar hvort að leikmaðurinn hefur tapað
#N: Tapa(Spilari)
#F: S er hlutur af tagi Spilari
#E: Skilar True ef það er enginn leikur mögulegur
#   skilar annars False
def Tapa(Spilari):
	tapZ = False
	for spil in Spilari.S:
        for bunki in Spilari.B:
            tapZ = PassaSaman(spil,bunki[-1])            
	      
	      
	      
	      
	      
