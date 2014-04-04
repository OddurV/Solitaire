# -*- coding: utf-8 -*-
from Spilastokkur import *
from Reglur import *
from Prompt import *
import time
import shelve
import pygame.image
import pygame.rect
import os.path

#Stafli af spilum
#myndin táknar tóman stafla
class AbstractStafli(AbstractMynd):
    def __init__(self,nafn,stadsetning,mynd,spilalisti=[]):
        AbstractMynd.__init__(self,nafn,stadsetning,mynd)
        self.spilalisti=[]
        self.leggjaSpil(spilalisti)
        
    #Eru spil í staflanum?
    def isEmpty(self):
        if self.spilalisti: return False
        return True
    
    #Hversu mörg spil eru í staflanum?
    def spilafjoldi(self): return len(self.spilalisti)
    
    #Snýr öllum spilunum í bunkanum upp eða niður
    def alltUpp(self,boolean):
        for spil in self.spilalisti:
            spil.snyrUpp=boolean
    
    #Teiknar botnmyndina sem er geymd í self.mynd (notað til að sýna tóman stafla)
    def teiknaBotn(self,skjar):
        skjar.blit(self.mynd,self.rammi)
    
    #Fjarlægir spil efst úr staflanum (aftast í listanum)
    def takaSpil(self,num):
        if num>self.spilafjoldi() or num<0: raise IndexError
        skiptistak=self.spilafjoldi()-num
        taka=self.spilalisti[skiptistak:] #Spilin sem eru tekin
        self.spilalisti=self.spilalisti[:skiptistak] #Spilin sem eru eftir
        return taka
        
    def takaAllt(self):
        return self.takaSpil(self.spilafjoldi())
        
    #setjaStadsetningu hreyfir öll spilin í stað þess að setja staðsetninguna beint
    def setjaStadsetningu(self,stadsetning):
        x_hreyfa=stadsetning[0]-self.rect.x
        y_hreyfa=stadsetning[1]-self.rect.y
        
        super(AbstractStafli,self).setjaStadsetningu(stadsetning)
        for spil in self.spilalisti: spil.hreyfaStad((x_hreyfa,y_hreyfa))
    
    def hreyfaStad(self,hreyfing):
        super(AbstractStafli,self).hreyfaStad(hreyfing)
        for spil in self.spilalisti: spil.hreyfaStad(hreyfing)
    
    #Einfalt fall sem tekur spil og skilar þeim aftur
    def skilaSpilum(self,spilalisti):
        self.leggjaSpil(spilalisti)
    
    #Næstu föll þurfa undirklasa
    def leggjaSpil(self,spilalisti):
        raise NotImplementedError
    
    def teikna(self,skjar):
        raise NotImplementedError

#Abstract klasi fyrir stafla þar sem öll spilin eru nákvæmlega ofan á hvort öðru
#Virkar alveg til að sýna staflann, en notandinn getur ekki hreyft hann
class AbstractEinfaldurStafli(AbstractStafli):
    def __init__(self,nafn,stadsetning,mynd,spilalisti=[]):
        AbstractStafli.__init__(self,nafn,stadsetning,mynd,spilalisti)
    
    #Teikna fallið teiknar ekki öll spilin í bunkanum, heldur bara það efsta
    def teikna(self,skjar):
        if not self.synilegt: return
        
        if self.isEmpty():
            self.teiknaBotn(skjar)
        
        else:
            self.spilalisti[-1].teikna(skjar)
    
    #Er hægt að bæta spilum í staflann? (í þessum klasa, nei)
    def leyfaFleiriSpil(self,stafli):
        return False
    
    #Legg eitt spil efst í staflann (spilið man hvar það var lagt niður síðast)
    def leggjaEitt(self,spil):
        spil.setjaStadsetningu((self.rammi.x,self.rammi.y))
        spil.stafli=self
        self.spilalisti.append(spil)
    
    #Legg mörg spil í staflann
    def leggjaSpil(self,spilalisti):
        for spil in spilalisti: self.leggjaEitt(spil)

#spilunum er dreift lóðrétt, og síðasta spilið er efst.
#Flísastaflinn hefur tvö bil milli spila
class AbstractFlisaStafli(AbstractStafli):
    def __init__(self,nafn,stadsetning,mynd,upphafs_bil,meira_bil,spilalisti=[]):
        self.upphafs_bil=upphafs_bil
        self.meira_bil=meira_bil
        AbstractStafli.__init__(self,nafn,stadsetning,mynd,spilalisti)
    
    def teikna(self,skjar):
        if not self.synilegt: return
        if self.isEmpty(): self.teiknaBotn(skjar)
        for spil in self.spilalisti: spil.teikna(skjar)
        
    #Er hægt að bæta spilum í staflann? (í þessum klasa, nei)
    def leyfaFleiriSpil(self,stafli):
        return False
    
    #Þetta fall athugar hvort að notandinn er að leggja spilið
    #eða hvort það er verið að skila spilinum í nýjan flísastafla
    #Það er til þess að bilin fari ekki á flakk
    def leggjaEitt(self,spil):
        if self.isEmpty():
            spil.setjaStadsetningu((self.rammi.x,self.rammi.y))
        else:
            efsta_spil=self.spilalisti[-1]
            #Ef efsta spilið snýr upp, þá er spilið lagt á með meira bili
            if efsta_spil.snyrUpp: spil.setjaStadsetningu((efsta_spil.rammi.x,efsta_spil.rammi.y+self.meira_bil))
            #Ef efsta spilið er á hvolfi þá er spilið lagt beint ofan á það
            else: efsta_spil.snyrUpp: spil.setjaStadsetningu((efsta_spil.rammi.x,efsta_spil.rammi.y+self.upphafs_bil))
        
        spil.stafli=self
        self.spilalisti.append(spil)
        self.uppfaeraSvaedi()
    
    #Legg spil í staflann
    def leggjaSpil(self.spilalisti):
        for spil in spilalisti: self.leggjaEitt(spil)
    
    #ramminn verður stærri eftir því sem fleiri spilum er bætt við
    def uppfaeraSvaedi(self):
        if self.isEmpty():
            ref=self.mynd.get_rect()
            self.rammi.h=ref.h
        else:
            botn=self.spilalisti[-1].rammi.bottom
            toppur=self.spilalisti[0].rammi.top
            self.rammi.h=botn-toppur
    
    #Fjarlægir spil efst úr staflanum (aftast úr listanum)
    #þurfti að vera í undirklasa til að tryggja að svæðið sé uppfært rétt
    def takaSpil(self,num):
        svar=super(AbstractFlisaStafli,self).takaSpil(num)
        self.uppfaeraSvaedi()
        return svar
        
#AbstractMargfaldurStafli(AbstractHlutur)

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
         