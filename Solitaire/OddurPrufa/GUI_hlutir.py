# -*- coding: utf-8 -*-
import random
import pygame.image
import pygame.rect
import os.path
import GUI_abstract as hlutur
from pygame.locals import *

#Spil
class Spil(hlutur.AbstractMynd):
    #Bakhliðin er geymd hér, hún er sú sama fyrir öll spilin
    #Hún er upphafsstillt með self.HladaBakhlid()
    bakhlid=None
    
    #Þar sem static er hlaðið inn á undan __main__ þá er ekki hægt að hlaða
    #bakhliðinni strax. Þetta er vegna þess að HladaMynd() kallar á 
    #pygame fall (convert_alpha) sem þarfnast kalls á pygame.init()
    #Það er hægt að nota þetta static fall til að hlaða bakhliðinni
    @staticmethod
    def HladaBakhlid(self): #athuga að nota self.path í staðinn?
        Spil.bakhlid=hlutur.HladaMynd(self)
        
    #Litir spilanna
    RAUTT=1
    SVART=2
    
    #Fastayrðing gagna:
    #Hvert spil hefur sort (hjarta, spaði, tígull eða lauf) og 
    #gildi (1-13) og tilvísun (path) í mynd af sjálfu sér
    def __init__(self, sort, gildi, stadsetning):
        hlutur.AbstractMynd.__init__(self,sort+str(gildi),stadsetning,"Myndir/"+sort+str(gildi)+".jpg")
        self.sort=sort
        self.gildi=gildi
        self.path="Myndir/"+sort+str(gildi)+".jpg" #Slóð fyrir myndina sem er notuð í GUI
        self.stafli=None
        self.snyrUpp=True
        
        
    #Fall sem skilar streng sem táknar spilið (t.d. H1 fyrir hjartaás)
    #N: Spil1
    #F: Ekkert
    #E: Sort og gildi spilsins hefur verið skilað sem streng
    def __str__(self):
        return ("{0}{1}".format(self.sort,self.gildi))
        
    #Fall sem athugar hvort eitt spil er jafngilt öðru
    #N: Spil1==Spil2
    #F: other er spil
    #E: Skilar True ef Spil1 og Spil2 eru jafngild, annars False
    def __eq__(self, other):
        return self.sort == other.sort and self.gildi == other.gildi
    
    #def faGildi(self): return self.gildi
    #def faSort(self): return self.sort
    def faLit(self):
        if self.sort=="h" or self.sort=="t": return Spil.RAUTT
        return Spil.SVART
    
    def samiLitur(self,spil):
        return self.faLit()==spil.faLit()
    
    def teikna(self,skjar):
        if self.synilegt:
            mynd=self.mynd if self.snyrUpp else Spil.bakhlid
            skjar.blit(mynd,self.rammi)
    
#Upphafsstafli
class Upphafsstafli(hlutur.AbstractMargfaldurStafli):
    #Fastayrðing gagna:
    #Upphafsstaflinn inniheldur lista sem byrjar með 52 spilum
    DRAGA=0
    HENDA=1


    def __init__(self,nafn,stadsetning,bil,botn,spilalisti=[]):
        hlutur.AbstractMargfaldurStafli.__init__(self,nafn,stadsetning,bil)
        self.uppsetningStafla(self.uppsetningDraga(spilalisti,botn))
        self.uppsetningStafla(self.uppsetningHenda(botn))
        self.listi=[]
        for i in ["h","s","t","l"]:
            for j in range(1,14):
                self.listi.append(Spil(i,j,(0,0)))#path var skipt út fyrir pos
        self.Stokka()
    
    #Fall sem skilar spili úr listanum á þægilegan hátt
    #Dæmi: ef maður hefur stokkinn S og vill fyrsta spilið
    #      þá getur maður skrifað S(0) í staðinn fyrir
    #      S.listi[0], en báðar aðferðir virka.
    #F: num er heiltala 0<=num<len(Upphafsstafli)
    #E: spili númer num hefur verið skilað
    def __getitem__(self,num):
        return self.listi[num]
    
    #Fall sem skilar lengd spilastokksins
    #N: len(Upphafsstafli)
    #F: Ekkert
    #E: lengt spilastokksins hefur verið skilað
    def __len__(self):
        return len(self.listi)
        
    #Stokkar spilastokkinn
    #N: Upphafsstafli.Stokka()
    #F: Upphafsstaflinn hefur 52 spil
    #E: Það er búið að stokka spilastokkinn
    def Stokka(self):
        for i in range(52):
            self.Vixla(i,random.randint(0,51))
    
    #Fall sem víxlar tveimur spilum í stokknum
    #N: Upphafsstafli.Vixla(num1,num2)
    #F: num1 og num2 eru heiltölur, 0<=num1<=num2<len(Upphafsstafli)
    #E: það er búið að víxla spilum númer num1 og num2
    def Vixla(self,numer1,numer2):
        breyta=[self[numer1].sort,self[numer1].gildi]
        self[numer1].sort=self[numer2].sort
        self[numer1].gildi=self[numer2].gildi
        self[numer2].sort=breyta[0]
        self[numer2].gildi=breyta[1]
    
    #Tek spil úr stokknum
    #N: Upphafsstafli.Taka()
    #F: Ekkert
    #E: Fyrsta spilinu í stokknum hefur verið skilað, og eytt úr stokknum
    def Taka(self):
        x=self[len(self)-1]
        del self.listi[len(self)-1]
        return x
        
    #Legg spil í bunkann
    #N: Upphafsstafli.Leggja(spil)
    #F: Ekkert
    #E: Það er búið að bæta spil aftast í spilastokkinn
    def Leggja(self,spil):
        self.listi.append(spil)
    
    #Það þarf ekki staðsetningu fyrir uppsetningDraga og uppsetningHenda,
    #uppsetningStafla sér um að hafa það rétt
    def uppsetningDraga(self,spilalisti,botn):
        draga_stafli=hlutur.AbstractEinfaldurStafli("Draga",(0,0),botn,spilalisti)
        draga_stafli.alltUpp(False)
        return draga_stafli
    
    def uppsetningHenda(self,botn):
        henda_stafli=hlutur.AbstractEinfaldurStafli("Henda",(0,0),botn)
        return henda_stafli
    
    #Ef það er smellt á Draga staflann
    def dragaSmella(self):
        if not self.staflar[Upphafsstafli.DRAGA].isEmpty():
            taka_spil=self.staflar[Upphafsstafli.DRAGA].takaSpil(1)
            taka_spil[0].snyrUpp=True
            self.staflar[Upphafsstafli.HENDA].leggjaSpil(taka_spil)
        
        else:
            self.staflar[Upphafsstafli.HENDA].alltUpp(False)
            oll_spil=self.staflar[Upphafsstafli.HENDA].takaAllt(oll_spil)
            oll_spil.reverse()
            self.staflar[Upphafsstafli.DRAGA].leggjaSpil(oll_spil)
    
    def aSmelli(self,event):
        smelltur_stafli=self.faStafla(event.stadsetning)
        
        if not smelltur_stafli: return #Til öryggis, ef það var kallað óvart á þetta
        if not smelltur_stafli.synilegt: return
        
        if event.type==MOUSEBUTTONUP and event.button==1:
            if smelltur_stafli.nafn=="Draga":
                self.dragaSmella()
        
        #Endurvinnslubunkinn skilar efsta spilinu
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if smelltur_stafli.nafn=="Henda" and not smelltur_stafli.isEmpty(): return smelltur_stafli.takaSpil(1)
            
    #tvísmellur er alltaf MOUSEUP
    #Fyrir Draga bunkann gerir þetta það sama og einfaldur smellur
    #Henda bunkinn svarar ekki einföldum smelli, en tvöfaldur tekur efsta spilið
    def aTvismelli(self,event):
        smelltur_stafli=self.faStafla(event.stadsetning)
        if not smelltur_stafli: return
        if not smelltur_stafli.synilegt: return
        
        if smelltur_stafli.nafn=="Draga": self.dragaSmella()
        if smelltur_stafli.nafn=="Henda" and not smelltur_stafli.isEmpty(): return smelltur_stafli.takaSpil(1)
    
    def leyfaFleiriSpil(self,spil):
        return False
        
    def leggjaSpil(self,spil):
        raise NotImplementedError

#Staflarnir 7 sem eru aðal svæðið
class MeginStafli(hlutur.AbstractFlisaStafli):
    def __init__(self,nafn,stadsetning,mynd,upphafs_bil,meira_bil,spilalisti=[]):
        self.uppsetningStafla(spilalisti)
        hlutur.AbstractFlisaStafli.__init__(self,nafn,stadsetning,mynd,upphafs_bil,meira_bil,spilalisti)
    
    #Allt nema efsta spilið snýr niður
    def uppsetningStafla(self,spilalisti):
        for spil in spilalisti: spil.snyrUpp=False
        if spilalisti: spilalisti[-1].snyrUpp=True
    
    #Skilar efsta spilinu úr bunkanum sem var smellt á.
    #ef það var ekki smellt á spil þá skilar þetta -1
    def efstaSpilSmellt(self,stadsetning):
        svar=-1
        for i, spil in enumerate(self.spilalisti):
            if spil.hefStadsetningu(stadsetning): svar=i
        return svar
    
    def aSmelli(self,event):
        if not self.synilegt: return
        
        #Þegar smellt niður, þá skilar þetta öllum spilum frá og með spilinu sem var smellt á
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            smellt_spil=self.efstaSpilSmellt(event.stadsetning)
            if smellt_spil !=-1 and self.spilalisti[smellt_spil].snyrUpp:
                taka_spil=self.spilafjoldi()-smellt_spil
                return self.takaSpil(taka_spil)
        
        #Ef efsta spilið snýr niður þá mun smellur snúa því við
        if event.type==MOUSEBUTTONUP and event.button==1:
            if not self.isEmpty() and self.spilalisti[-1].hefStadsetningu(event.stadsetning):
                self.spilalisti[-1].snyrUpp=True
    
    #Skilar efsta spilinu úr staflanum ef það sneri upp og var smellt á það
    def aTvismelli(self,event):
        if not self.synilegt: return
        
        smellt_spil=self.efstaSpilSmellt(event.stadsetning)
        if smellt_spil != -1 and self.spilalisti[smellt_spil].snyrUpp and smellt_spil==self.spilafjoldi()-1:
            return self.takaSpil(1)
    
    #Er hægt að bæta þessum spilum á þennan stafla?
    #Bara fyrsta spilið í listanum skiptir máli, gerum ráð fyrir að forritið hafi raðað hinum rétt
    def leyfaFleiriSpil(self,spilalisti):
        if self.isEmpty():
            if spilalisti[0].gildi==13 and self.hefArekstur(spilalisti[0]):
                return True
        else:
            ref_spil=self.spilalisti[-1]
            if not ref_spil.snyrUpp:
                return False
            
            if not ref_spil.samiLitur(spilalisti[0]) and ref_spil.gildi==spilalisti[0].gildi+1:
                if ref_spil.hefArekstur(spilalisti[0]):
                    return True
        return False

#Einfaldur stafli sem leyfir bara að bæta einu spili í einu með vaxandi gildi og sömu sort
#Ef tómur, tekur bara við ásum
#Telur hvað eru mörg spil í öllum lokastöflum (fyrir sigurskilyrðið, 52)
class lokaStafli(hlutur.AbstractEinfaldurStafli):
    heildarfjoldi_spila=0
    
    def __init__(self,nafn,stadsetning,mynd):
        hlutur.AbstractEinfaldurStafli.__init__(self,nafn,stadsetning,mynd)
    
    #Þarf að útvíkka leyfaFleiriSpil, því tvísmellur sendir spil hingað
    def leyfaFleiriSpil(self, spilalisti,snerting=True):
        if snerting:
            if not self.hefArekstur(spilalisti[0]): return False
        if len(spilalisti)!=1: return False
        
        if self.isEmpty():
            if spilalisti[0].gildi==1: return True
            return False
        
        ref_spil=self.spilalisti[-1]
        if ref_spil.sort==spilalisti[0].sort and ref_spil.gildi+1==spilalisti[0].gildi:
            return True
        return False
    
    #á smelli
    def aSmelli(self,event):
        if not self.synilegt: return False
        
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if not self.isEmpty(): return self.takaSpil(1)
    
    def aTvismelli(self,event):
        pass
    
    #útvíkka þessi föll til að halda utan um heildarfjoldi spila í lokastöflum
    def takaSpil(self,num):
        taka_spil=super(lokaStafli,self).takaSpil(num)
        lokaStafli.heildarfjoldi_spila -= num
        return taka_spil
    
    def leggjaEitt(self,spil):
        super(lokaStafli,self).leggjaEitt(spil)
        lokaStafli.heildarfjoldi_spila +=1

#Klasi sem einfaldar flutning spila
#Tekur lista af spilum úr stafla og heldur þeim saman á meðan þau eru hreyfð
#Man líka hvaðan þau komu, og skilar þeim aftur ef það þarf
class geymsla(object):
    def __init__(self,nafn):
        self.nafn=nafn
        self.spilalisti=[]
        self.uppruni=None
    
    def leggjaSpil(self,spilalisti):
        if self.uppruni or self.spilalisti: raise Exception
        if spilalisti:
            self.spilalisti=spilalisti
            self.uppruni=spilalisti[0].stafli
            
    def hefSpil(self):
        if self.spilalisti: return True
        return False
    
    def hreinsa(self):
        self.spilalisti=[]
        self.uppruni=None
    
    def skilaSpilum(self):
        self.uppruni.leggjaSpil(self.spilalisti)
        self.hreinsa()
    
    #Hreyfi spilið í staflann
    def leggjaIStafla(self,stafli):
        stafli.leggjaSpil(self.spilalisti)
        self.hreinsa()
    
    def teikna(self,skjar):
        for spil in self.spilalisti: spil.teikna(skjar)
    
    def hreyfaStadsetningu(self,hreyfing):
        for spil in self.spilalisti: spil.hreyfaStadsetningu(hreyfing)
