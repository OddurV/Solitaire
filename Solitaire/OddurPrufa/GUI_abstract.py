# -*- coding: utf-8 -*-
import pygame.image
import pygame.rect
import os.path
from pygame.locals import *

#Stillingar fyrir myndirnar
class Stillingar:
    Upplausn=(124,174)
    Upphafs_bil=10
    Linubil=30
    Spassia=20
    Flis_litid_bil=5
    Flis_stort_bil=15
    Hradi=500

#Fall sem hleður inn myndum
def HladaMynd(spil) :
    mynd =  pygame.image.load(spil)
    return mynd.convert_alpha()

    #Einfaldur klasi sem allir aðrir hlutir nota
class AbstractHlutur(object):
    def __init__(self, nafn, stadsetning):
        #Nafn hlutsins
        self.nafn=nafn
        #Staðsetning hlutsins (byrjar sem 0-víddar rétthyrningur)
        self.rammi=pygame.Rect(stadsetning[0],stadsetning[1],0,0)
        
    #Athuga hvort að x,y staðsetning er í hlutnum
    def hefStadsetningu(self, stadsetning):
        if not self.synilegt:return False
        return self.rammi.collidepoint(stadsetning)
    
    #Athuga hvort að það er árekstur
    def hefArekstur(self, hlutur):
        return self.rammi.colliderect(hlutur.rammi)
    
    #Skilar x,y staðsetningunni úr self.rammi
    def faStadsetningu(self):
        return (self.rammi.x, self.rammi.y)
    
    #Set staðsetningu
    def setjaStadsetningu(self,stadsetning):
        self.rammi.x, self.rammi.y = stadsetning[0], stadsetning[1]
    
    #Hreyfi staðsetninguna
    def hreyfaStadsetningu(self,hreyfa):
        self.rammi.move_ip(hreyfa)

#Hlutur sem hefur mynd tengda við hann
class AbstractMynd(AbstractHlutur):
    def __init__(self, nafn, stadsetning, mynd):
        AbstractHlutur.__init__(self, nafn, stadsetning)
        #Allir hlutir hafa skilgreinda mynd
        self.mynd=self.setjaMynd(mynd)
        #Á að teikna hlutinn eða ekki
        self.synilegt=True
        
    #Einföld teikniskipun sem þarf undirklasa til að vera gagnleg
    def teikna(self, skjar):
        if self.synilegt:
            skjar.blit(mynd, self.rammi)
    
    #Hver hlutur er tengdur við mynd. Um leið og myndinni hefur verið
    #hlaðið inn þarf að uppfæra self.rammi tilviksbreytuna
    def setjaMynd(self,mynd):
        hlada=HladaMynd(mynd)
        self.rammi.w,self.rammi.h=hlada.get_width(),hlada.get_height()
        return hlada

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
        x_hreyfa=stadsetning[0]-self.rammi.x
        y_hreyfa=stadsetning[1]-self.rammi.y
        
        super(AbstractStafli,self).setjaStadsetningu(stadsetning)
        for spil in self.spilalisti: spil.hreyfaStadsetningu((x_hreyfa,y_hreyfa))
    
    def hreyfaStadsetningu(self,hreyfing):
        super(AbstractStafli,self).hreyfaStadsetningu(hreyfing)
        for spil in self.spilalisti: spil.hreyfaStadsetningu(hreyfing)
    
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
            else: spil.setjaStadsetningu((efsta_spil.rammi.x,efsta_spil.rammi.y+self.upphafs_bil))
        
        spil.stafli=self
        self.spilalisti.append(spil)
        self.uppfaeraSvaedi()
    
    #Legg spil í staflann
    def leggjaSpil(self,spilalisti):
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
        
#Abstract klasi sem getur haldið á mörgum stöflum, ef þeir þurfa að tala saman
#Hann þarf ekki mynd, þannig að self.rammi hefur enga vídd
#Það veldur því að hefStadsetningu þarf að vera í undirklasa til að leyfa 
#notandavirkni og samskipti milli stafla
class AbstractMargfaldurStafli(AbstractHlutur):
    def __init__(self,nafn,stadsetning,bil):
        AbstractHlutur.__init__(self,nafn,stadsetning)
        self.bil=bil
        self.staflar=[]
    
    #Sérhver stafli er staðsettur með bilinu self.bil frá fyrri stafla
    def uppsetningStafla(self,nyr_stafli):
        millibil=0
        for stafli in self.staflar:
            millibil += stafli.rammi.width+self.bil
        nyr_stafli.setjaStadsetningu((self.rammi.x+millibil,self.rammi.y))
        self.staflar.append(nyr_stafli)
    
    #Er stafli í þessari staðsetningu? (skilar None ef það er ekkert)
    def faStafla(self,stadsetning):
        for stafli in self.staflar:
            if stafli.hefStadsetningu(stadsetning): return stafli
    
    def hefStadsetningu(self,stadsetning):
        if self.faStafla(stadsetning): return True
        return False
    
    def hreyfaStadsetningu(self,hreyfing):
        for stafli in self.staflar:
            stafli.hreyfaStadsetningu(hreyfing)
    
    def teikna(self,skjar):
        for stafli in self.staflar:
            stafli.teikna(skjar)
