# -*- coding: utf-8 -*-
from Spilastokkur import *
from Reglur import *
#from Prompt import *
from pygame.locals import *
import time
import shelve
import pygame.image
import pygame.rect
import os.path

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
        
        self.Stig=0
        self.StartTime=time.time()
        self.EndTime=time.time()
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
                self.Stig=self.Stig-100
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
        if len(Bunki1)==0 or num>len(Bunki1):
            return False
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
        if len(Bunki)==0:
            return False
        if LeyfilegLokahreyfing(Bunki[-1],Stafli):
            Stafli.append(Bunki.pop())
            return True
        else:
            return False
            
    
            
    #Fall sem snýr við efsta spilinu í undirbunka,
    #ef bunkinn ofan á er tómur
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
            
    #Fall sem bætir stigunum manns inn í topplista ef þau eru nógu mörg
    #N: Spilari.BreytaTopplista()
    #F: Ekkert
    #E: Búið er að bæta stigum leikmannsins í topplistann ef þau voru 
    #   nógu mörg til að hann kæmist inn í topp 10.
    def BreytaTopplista(self):
        skuffa=shelve.open("HiScore.txt")
        tmp=[]
        for i in skuffa:
            tmp.append(skuffa[i])
        if len(tmp)<10:
            nafn=raw_input("Þú komst á topplistann! Hvað er nafnið þitt? ")
            skuffa[len(tmp)]=nafn,stig
            skuffa.close()
            return True
        else:
            tmp.sort(key=lambda variable: variable[1])
            if self.Stig>tmp[0][1]:
                nafn=raw_input("Þú komst inn á topplistann! Hvað er nafnið þitt? ")
                skuffa[len(tmp)]=nafn,stig
                skuffa.close()
                return True
            else:
                print "Þú komst ekki inn á topplistann."
                skuffa.close()
                return False
         