# -*- coding: utf-8 -*-
import Spilastokkur
import Reglur

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
		S=Spilastokkur()
		E=[]
		
		#Bunki 1-7
		B=[[],[],[],[],[],[],[]]
		
		#UndirBunki 1-7
		UB=[[],[],[],[],[],[],[]]
				
		#Grunnur 1-4
		G=[[],[],[],[]]
		
		#legg spil í bunkana
		for i in range(7):
			for j in range(i):
				UB[i].append(S.Taka())
				
		#"sný upp" efstu spilunum í UB og set þau í samsvarandi lista í B
		for in in range(7):
			B[i].append(UB[i].pop())
		
	#Dreg spil úr spilastokknum og set það efst í endurvinnslubunkann
	#Ef stokkurinn er tómur, þá er endurvinnslubunkinn endurunninn
	#N: Spilari.Draga(Spilastokkur,Endurvinnslubunki)
	#F: Ekkert
	#E: Ef það voru spil í stokknum þá hefur efsta spilið verið sett í 
	#   endurvinnslubunkann, ef það voru engin spil í stokknum þá hefur
	#   endurvinnslubunkinn verið endurunninn, en ef hann var líka tómur
	#   þá hefur ekkert gerst.
	def Draga(self,S,E):
		if len(S)==0:
			if len(E)==0:
				return
			else:
				Endurvinna(S,E)
		else:
			E.append(S.Taka())

	#Fall sem setur endurvinnslubunkann aftur í spilastokkinn
	#N: Spilari.Endurvinna(S,E)
	#F: S er tómur, og það er a.m.k. eitt spil í E
	#E: Öll spilin í E hafa verið færð aftur í S
	def Endurvinna(self,S,E):
		for i in range(0,len(E),1):
			S.Leggja(E.pop())
		
	#Fall sem hreyfir spil úr einum bunka í annan
	#N: Spilari.Hreyfa(Bunki1,Bunki2,num1,num2)
	#F: Bunki1 og Bunki2 eru listar, num1 og num2 eru heiltölur
	#   0<=num1<=num2<len(Bunki1)
	#E: spilarunan sem er á bilinu num1 til num2 hefur verið
	#   færð úr bunka 1 yfir í bunka 2.
	def Hreyfa(self,Bunki1,Bunki2,num1,num2):
		if Reglur.legalMove(Bunki1,Bunki2,num1,num2):
			temp=[]
			for i in range(num2-num1):
				temp.append(Bunki1.pop())
			for i in range(num2-num1):
				Bunki2.append(temp.pop))
		else:
			Prompt.Villa()