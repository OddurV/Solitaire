# -*- coding: utf-8 -*-
import random

#Spil
class Spil:
    #Fastayrðing gagna:
    #Hvert spil hefur sort (hjarta, spaði, tígull eða lauf) og 
    #gildi (1-13) og tilvísun (path) í mynd af sjálfu sér
    def __init__(self, sort, gildi, path):
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
        p="Myndir/"
        for i in ["H","S","T","L"]:
            for j in range(1,14):
                self.listi.append(Spil(i,j,p+i+str(j)+".jpg"))
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
