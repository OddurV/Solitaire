# -*- coding: utf-8 -*-
import random
import pygame.image
import pygame.rect
import os.path

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
    mynd =  pygame.image.load(spil.path)
    return image.convert_alpha()

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

#Spil
class Spil(AbstractMynd):
    #Fastayrðing gagna:
    #Hvert spil hefur sort (hjarta, spaði, tígull eða lauf) og 
    #gildi (1-13) og tilvísun (path) í mynd af sjálfu sér
    def __init__(self, sort, gildi, path):
        AbstractMynd.__init__(self,sort+str(gildi),stadsetning,path)
        self.sort=sort
        self.gildi=gildi
        self.path=path #Slóð fyrir myndina sem er notuð í GUI
        
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
    
#Spilastokkur
class Spilastokkur:
    #Fastayrðing gagna:
    #Spilastokkurinn inniheldur lista sem byrjar með 52 spilum

    #N: S=Spilastokkur()
    #F: Ekkert
    #E: S er nýr spilastokkur með 52 spilum í handahófskenndri röð
    def __init__(self):
        self.listi=[]
        self.p="Myndir/"
        for i in ["h","s","t","l"]:
            for j in range(1,14):
                self.listi.append(Spil(i,j,self.p+i+str(j)+".jpg"))
        self.Stokka()
    
    #Fall sem skilar spili úr listanum á þægilegan hátt
    #Dæmi: ef maður hefur stokkinn S og vill fyrsta spilið
    #      þá getur maður skrifað S(0) í staðinn fyrir
    #      S.listi[0], en báðar aðferðir virka.
    #F: num er heiltala 0<=num<len(Spilastokkur)
    #E: spili númer num hefur verið skilað
    def __getitem__(self,num):
        return self.listi[num]
    
    #Fall sem skilar lengd spilastokksins
    #N: len(Spilastokkur)
    #F: Ekkert
    #E: lengt spilastokksins hefur verið skilað
    def __len__(self):
        return len(self.listi)
        
    #Stokkar spilastokkinn
    #N: Spilastokkur.Stokka()
    #F: Spilastokkurinn hefur 52 spil
    #E: Það er búið að stokka spilastokkinn
    def Stokka(self):
        for i in range(52):
            self.Vixla(i,random.randint(0,51))
    
    #Fall sem víxlar tveimur spilum í stokknum
    #N: Spilastokkur.Vixla(num1,num2)
    #F: num1 og num2 eru heiltölur, 0<=num1<=num2<len(Spilastokkur)
    #E: það er búið að víxla spilum númer num1 og num2
    def Vixla(self,numer1,numer2):
        breyta=[self[numer1].sort,self[numer1].gildi]
        self[numer1].sort=self[numer2].sort
        self[numer1].gildi=self[numer2].gildi
        self[numer2].sort=breyta[0]
        self[numer2].gildi=breyta[1]
    
    #Tek spil úr stokknum
    #N: Spilastokkur.Taka()
    #F: Ekkert
    #E: Fyrsta spilinu í stokknum hefur verið skilað, og eytt úr stokknum
    def Taka(self):
        x=self[len(self)-1]
        del self.listi[len(self)-1]
        return x
        
    #Legg spil í bunkann
    #N: Spilastokkur.Leggja(spil)
    #F: Ekkert
    #E: Það er búið að bæta spil aftast í spilastokkinn
    def Leggja(self,spil):
        self.listi.append(spil)
