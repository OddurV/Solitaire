# -*- coding: utf-8 -*-

#ÖSSUR ER AÐ VINNA Í ÞESSU


#import Spilastokkur


#Leikreglur


#Fall sem athugar hvort að leikurinn er löglegur
#Skilar True eða False
#N: LeyfilegHreyfing(Bunki1,UndirBunki1,Spil)
#F: Bunki1, UndirBunki1 og Bunki2 eru listar, Spil er Spil
#F: UndirBunki1 er undirbunki Bunki1
#E: Skilar True ef það er leyfilegt að leggja Spil ofan á Bunki1
#   Annars er False skilað
def LeyfilegHreyfing(Bunki1,UndirBunki1, Spil):
    #Athuga hvort efsta spil Bunka sé face-up eða hvort setja megi kóng
    if len(Bunki1) == 0:
        if len(UndirBunki1) == 0:
            return Spil.gildi==13
        else:
            return False
    
    #Önnur tilfelli:
    efstaSpilBunka = Bunki1[-1]
    rjettGildiZ = (efstaSpilBunka.gildi==Spil.gildi+1)
    if efstaSpilBunka.sort=="H" or efstaSpilBunka.sort=="T":
        rjettSortZ=(Spil.sort=="S" or Spil.sort=="L")
    else:
        rjettSortZ=(Spil.sort=="H" or Spil.sort=="T")
    return rjettGildiZ and rjettSortZ


#Fall sem athugar hvort að það má færa spilið upp í lokabunka/stafla 
#N: LeyfilegLokahreyfing(Spil, Stafli)
#F: Spil er Spil og Stafli er Grunnur/Stafli í Spilara
#E: Skilar True ef það er leyfilegt að setja spil ofaná stafla
def LeyfilegLokahreyfing(Spil, Stafli):
    if (len(Stafli) == 0):
        if Spil.gildi==1:
            return True
        else:
            return False
    efstaSpilStafla  = Stafli[-1]
    rjettGildiZ = (Spil.gildi == efstaSpilStafla.gildi+1)
    rjettSortZ = (Spil.sort == efstaSpilStafla)
    return rjettGildiZ and rjettSortZ
    
#Fall sem athugar hvort að það má snúa við efsta spilinu í undirbunkanum
#N: LeyfaFletta(UndirBunki,Bunki)
#F: UndirBunki og Bunki eru listar af spilum
#E: Skilar True ef Bunki er tómur og Undirbunki er ekki tómur, annars False
def LeyfaFletta(UndirBunki,Bunki):
    return len(Bunki)==0 and len(UndirBunki)>0
    
#Fall sem athugar hvort að leikmaðurinn hefur sigrað
#N: Sigra(G)
#F: G er listi af listunum sem öll spilin eiga að enda í
#E: Skilar True ef það eru 13 spil í hverjum lista, annars False
def Sigra(G):
    return len(G[0])==len(G[1]) and len(G[1])==len(G[2]) and len(G[2])==len(G[3]) and len(G[0])==13

#Fall sem athugar hvort að leikmaðurinn getur eitthvað gert
#ATH. þetta fall er nánast algjörlega tilgangslaust, nema kannski í blábyrjun
#N: Moguleikur(Spilari)
#F: Spilari er hlutur af tagi Spilari
#E: Skilar True ef það er enginn leikur mögulegur
#   skilar annars False
def Moguleikur(Spilari):
    tapZ = False
    
    #Ef það á eftir að snúa við spili á einhverjum bunka, er False skilað
    for i, bunki in enumerate(Spilari.B):
            if len(bunki) == 0:
                if len(Spilari.UB[i])!=0:
                    return False
    
    #Fall sem tekur inn spil og tjekkar fyrir alla bunka og stafla
    def tekkaBordh(Spil, tapZ):
        #Tékka á bunkum
        for i in range(0,7):
                tapZ = tapZ or LeyfilegHreyfing(Spilari.B[i], Spilari.UB[i], Spil)    
        #Tékka á stöflum
        for Stafli in Spilari.G:
            tapZ = tapZ or LeyfilegLokahreyfing(Spil,Stafli)
        return tapZ
    
    #Tékka á hverju einasta spili í stokkinum
    for spil in Spilari.S:
        tapZ = tekkaBordh(spil, tapZ)
        if tapZ:
            return tapZ
    
    #Tékka á efsta spili allra bunka
    for bunki in Spilari.B:
        if len(bunki)!=0 :
            tapZ = tekkaBordh(bunki[-1],tapZ)
            
    #Tékka á efsta spili allra stafla
    for stafli in Spilari.G:
        if len(stafli)!=0 :
            tapZ = tekkaBordh(stafli[-1],tapZ)    
        
    return tapZ
