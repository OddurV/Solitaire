# -*- coding: utf-8 -*-
import Spilastokkur
import Reglur

#Leikmaður
class Spilari:
	#Leikmaðurinn heldur á öllum bunkunum 
	#og getur hreyft spil á milli þeirra
	def __init__(self):
		S=Spilastokkur()
		E=[]
		
		#Bunki 1-7
		B1=[]
		B2=[]
		B3=[]
		B4=[]
		B5=[]
		B6=[]
		B7=[]
		
		#UndirBunki 1-7
		UB1=[]
		UB2=[]
		UB3=[]
		UB4=[]
		UB5=[]
		UB6=[]
		UB7=[]
		
		#Grunnur 1-4
		G1=[]
		G2=[]
		G3=[]
		G4=[]
	
	#Dreg spil úr spilastokknum og set það efst í endurvinnslubunkann
	#Ef stokkurinn er tómur, þá er endurvinnslubunkinn endurunninn
	def Draga(S,E):
		if len(S)==0:
			if len(E)==0:
				return
			else:
				Endurvinna
		else:
			E.append(S.Taka())

	#
	def Endurvinna(S,E):
		for i in range(0,len(E)-1,1):
			S.Leggja(E.pop())
		
	def Hreyfa():
		pass