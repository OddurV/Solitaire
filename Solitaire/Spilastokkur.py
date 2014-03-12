# -*- coding: utf-8 -*-
import random

#Spil
class Spil:
	#Hvert spil hefur sort (hjarta, spaði, tígull eða lauf) og 
	#gildi (1-13) og tilvísun (path) í mynd af sjálfu sér
	def __init__(self, sort, gildi, path):
		self.sort=sort
		self.gildi=gildi
		self.path=path #Slóð fyrir myndina sem er notuð í GUI
		
	#Fall sem skilar streng sem táknar spilið (t.d. H1 fyrir hjartaás)
	def __str__(self):
		return ("{0}{1}".format(self.sort,self.gildi))
		
	#Fall sem athugar hvort eitt spil er jafngilt öðru
	def __eq__(self, other):
		return self.sort == other.sort and self.gildi == other.gildi

#Spilastokkur
class Spilastokkur:
	#Spilastokkurinn inniheldur lista sem byrjar með 52 spilum
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
	def __getitem__(self,num):
		return self.listi[num]
	
	#Fall sem skilar lengd spilastokksins
	def __len__(self):
		return len(self.listi)
		
	#Stokkar spilastokkinn
	def Stokka(self):	
		for i in range(52):
			self.Vixla(i,random.randint(0,51))
	
	#Fall sem víxlar tveimur spilum í stokknum
	def Vixla(self,numer1,numer2):
		breyta=[self.listi[numer1].sort,self.listi[numer1].gildi]
		self.listi[numer1].sort=self.listi[numer2].sort
		self.listi[numer1].gildi=self.listi[numer2].gildi
		self.listi[numer2].sort=breyta[0]
		self.listi[numer2].gildi=breyta[1]
	
	#Tek spil úr stokknum
	def Taka(self):
		x=self.listi[0]
		del self.listi[0]
		return x
		
	#Legg spil í bunkann
	def Leggja(self,spil):
		self.listi.append(spil)
