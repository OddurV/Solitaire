# -*- coding: utf-8 -*-
import random

#Spil
class Spil:
	def __init__(self, sort, gildi, path):
		self.sort=sort
		self.gildi=gildi
		self.path=path #Slóð fyrir myndina sem er notuð í GUI
		
	def __str__(self):
		return ("{0}{1}".format(self.sort,self.gildi))
		
	def __eq__(self, other):
		return self.sort == other.sort and self.gildi == other.gildi

#Spilastokkur
class Spilastokkur:
	def __init__(self):
		self.listi=[]
		p="Myndir/"
		for i in ["H","S","T","L"]:
			for j in range(1,14):
				self.listi.append(Spil(i,j,p+i+str(j)+".jpg"))
		self.Stokka()
	
	def __getitem__(self,num):
		return self.listi[num]
	
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

#Bunki
class Bunki:
	def __init__(self):
		self.listi=[]

	def __getitem__(self,num):
		return self.listi[num]
		
	def __len__(self):
		return len(self.listi)
		
	#Tek spil á hendi
	def Halda(self,spil):
		self.listi.append(spil)
	
	#Losa mig við spil
	def Taka(self,num1,num2):
		x=[]
		for i in range(num1,num2,1):#Ath, kannski á þetta að vera (num2-1)?
			x.append(self.listi[i])
		for j in range(num2,num1,-1):#Ath, kannski á þetta að vera (num2-1)?
			del self.listi[j]
		return x
