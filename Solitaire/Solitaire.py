# -*- coding: utf-8 -*-
import Spilastokkur
import Reglur
import Prompt

#Dreg spil úr spilastokknum og set það efst í endurvinnslubunkann
#Ef stokkurinn er tómur, þá er endurvinnslubunkinn endurunninn
def Draga(S,E):
	if len(S)==0:
		if len(E)==0:
			return
		else:
			Endurvinna
	else:
		E.Leggja(S.Taka())

#
def Endurvinna(S,E):
	for i in range(0,len(E)-1,1):
		S.Leggja(E.Taka())
	
def Hreyfa():
	pass

if __name__=="__main__":
	#Stilli upp fyrsta leiknum
	S=Spilastokkur()
	E=Bunki()
	
	#Bunki 1-7
	B1=Bunki()
	B2=Bunki()
	B3=Bunki()
	B4=Bunki()
	B5=Bunki()
	B6=Bunki()
	B7=Bunki()
	
	#UndirBunki 1-7
	UB1=Bunki()
	UB2=Bunki()
	UB3=Bunki()
	UB4=Bunki()
	UB5=Bunki()
	UB6=Bunki()
	UB7=Bunki()
	
	#Grunnur 1-4
	G1=Bunki()
	G2=Bunki()
	G3=Bunki()
	G4=Bunki()
	
	
	
	#Leikjalykkja
	while True:
		pass
	
		if Stoppa():
			break