# -*- coding: utf-8 -*-
from Spilastokkur import *
from Reglur import *
from Prompt import *

#Leikmaðurinn heldur á öllum bunkunum 
#og getur hreyft spil á milli þeirra
class Spilari:
    #Fastayrðing gagna:
    #S er spilastokkur. E, B, UB og G eru listar sem innihalda 
    #lista sem innihalda ekkert eða fleiri spil
    
    #N: x=Spilari()
    #F: Ekkert
    #E: x er nýr leikmaður sem heldur á spilastokki og 19 bunkum í formi lista
    def __init__(self):
        self.S=Spilastokkur()
        self.E=[] #Endurvinnslubunki
        
        #Bunki 1-7
        self.B=[[],[],[],[],[],[],[]]
        
        #UndirBunki 1-7
        self.UB=[[],[],[],[],[],[],[]]
                
        #Grunnur/staflar 1-4
        self.G=[[],[],[],[]] 
        
        #legg spil í bunkana
        for i in range(7):
            for j in range(i+1):
                self.UB[i].append(self.S.Taka())
                
        #"sný upp" efstu spilunum í UB og set þau í samsvarandi lista í B
        for i in range(7):
            self.B[i].append(self.UB[i].pop())
        
    #Dreg spil úr spilastokknum og set það efst í endurvinnslubunkann
    #Ef stokkurinn er tómur, þá er endurvinnslubunkinn endurunninn
    #N: Spilari.Draga(Spilastokkur,Endurvinnslubunki)
    #F: Ekkert
    #E: Ef það voru spil í stokknum þá hefur efsta spilið verið sett í 
    #   endurvinnslubunkann, ef það voru engin spil í stokknum þá hefur
    #   endurvinnslubunkinn verið endurunninn, en ef hann var líka tómur
    #   þá hefur ekkert gerst.
    def Draga(self):
        if len(self.S)==0:
            if len(self.E)==0:
                return
            else:
                self.Endurvinna()
        else:
            self.E.append(self.S.Taka())

    #Fall sem setur endurvinnslubunkann aftur í spilastokkinn
    #N: Spilari.Endurvinna(S,E)
    #F: S er tómur, og það er a.m.k. eitt spil í E
    #E: Öll spilin í E hafa verið færð aftur í S
    def Endurvinna(self):
        for i in range(0,len(self.E),1):
            self.S.Leggja(self.E.pop())
        
    #Fall sem hreyfir spil úr einum bunka í annan
    #N: Spilari.Hreyfa(Bunki1,Bunki2,UndirBunki2,num)
    #F: Bunki1, Bunki2 og UndirBunki2 eru listar, num er heiltala
    #   0<=num<len(Bunki1)
    #E: spilarunan sem er á bilinu num til len(Bunki1) hefur verið
    #   færð úr bunka 1 yfir í bunka 2.
    def Hreyfa(self,Bunki1,Bunki2,UndirBunki2,num):
        if LeyfilegHreyfing(Bunki2,UndirBunki2,Bunki1[num]):
            temp=[]
            x=len(Bunki1)
            for i in range(x-num):
                temp.append(Bunki1.pop())
            for i in range(x-num):
                Bunki2.append(temp.pop())
        else:
            Villa()
            
    #Fall sem snýr við efsta spilinu í undirbunka,
    #ef bunkinn ofaná er tómur
    #N: Spilari.Fletta(UndirBunki,Bunki)
    #F: UndirBunki og Bunki eru listar af spilum, Bunki er tómur
    #E: Efsta spilið í UndirBunkanum hefur verið sett í Bunkann
    def Fletta(self,UndirBunki,Bunki):
        if LeyfaFletta(UndirBunki,Bunki):
            Bunki.append(UndirBunki.pop())
        else:
            Villa()