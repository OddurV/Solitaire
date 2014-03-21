# -*- coding: utf-8 -*-
#UNDER CONSTRUCTION - ODDUR
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
    #E: Ef löglegt er að hreyfa spilarununa sem er á bilinu num til len(Bunki1) 
    #   skilar fallið True og hefur verið færð úr bunka 1 yfir í bunka 2.
    #   Ef ólöglegt er engin hreyfing framkvæmd og fallið skilar False
    def Hreyfa(self,Bunki1,Bunki2,UndirBunki2,num):
        if LeyfilegHreyfing(Bunki2,UndirBunki2,Bunki1[num]):
            temp=[]
            x=len(Bunki1)
            for i in range(x-num):
                temp.append(Bunki1.pop())
            for i in range(x-num):
                Bunki2.append(temp.pop())
            return True
        else:
            return False
        
     #Fall sem hreyfir spil úr einum bunka í stafla
    #N: Spilari.Hreyfa(Bunki1,Stafli1
    #F: Bunki1 og Stafli1 eru listar
    #E: Ef löglegt er að hreyfa efsta spil bunkans
    #   skilar fallið True og hefur verið færð úr bunka 1 yfir í bunka 2.
    #   Ef ólöglegt er engin hreyfing framkvæmd og fallið skilar False
    def LokaHreyfing(self, Bunki, Stafli):
        if LeyfilegLokahreyfing(Bunki[-1],Stafli):
            Stafli.append(Bunki.pop())
            return True
        else:
            return False
            
    
            
    #Fall sem snýr við efsta spilinu í undirbunka,
    #ef bunkinn ofaná er tómur
    #N: Spilari.Fletta(UndirBunki,Bunki)
    #F: UndirBunki og Bunki eru listar af spilum
    #E: Efsta spilið í UndirBunkanum hefur verið sett í Bunkann ef Bunki var tómur
    #   og fallið skilar True. Ef Bunki var ekki tómur gerist ekkert og fallið skilar 
    #   False
    def Fletta(self,UndirBunki,Bunki):
        if LeyfaFletta(UndirBunki,Bunki):
            Bunki.append(UndirBunki.pop())
            return True
        else:
            return False