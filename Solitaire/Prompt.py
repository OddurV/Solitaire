# -*- coding: utf-8 -*-
from Spilari import *

#Tilkynningar til, og skipanir frá notanda

#Fall sem biður notandann um inntak, og skilar því í lágstöfum
#N: x=Adgerd()
#F: Ekkert
#E: Staðalinntaki hefur verið skilað á lágstafaformi
def Adgerd():
	x=raw_input("Hvað viltu gera? ")
	return x.lower()

#Fall sem prentar stöðuna í leiknum
#N: Stada(Spilari)
#F: Ekkert
#E: Staða spilsins 
def Stada(Spilari):
	#Spilastokkurinn
	print "Fjöldi spila í spilastokknum: ", len(Spilari.S)
	
	#Endurvinnslubunkinn
	if len(Spilari.E)==0:
		print "[]"
	else:
		print "E: ",Spilari.E[len(Spilari.E)-1]
	
	print ""
	
	#Set undirbunkana í temp
	temp=[[],[],[],[],[],[],[]]
	for i in range(7):
		for j in range(len(Spilari.UB[i])):
			temp[i].append("[*]")
	#Bæti bunkunum við í temp
	for i in range(7):
		for j in range(len(Spilari.B[i])):
			temp[i].append(Spilari.B[i][j])
	#Sýni undirbunkana og bunkana saman
	for i in range(7):
		temp2=""
		for j in range(len(temp[i])):
			temp2=temp2+str(temp[i][j])+" "
		print temp2
	
	print ""
	
	#Sýni efstu spilin í grunninum
	if len(Spilari.G[0])==0:
		print "[]"
	else:
		print Spilari.G[0][len(Spilari.G[0])-1]
	if len(Spilari.G[1])==0:
		print "[]"
	else:
		print Spilari.G[1][len(Spilari.G[1])-1]
	if len(Spilari.G[2])==0:
		print "[]"
	else:
		print Spilari.G[2][len(Spilari.G[2])-1]
	if len(Spilari.G[3])==0:
		print "[]"
	else:
		print Spilari.G[3][len(Spilari.G[3])-1]
		
	print ""

#Fall sem athugar hvort notandinn vill draga spil
#N: VilDraga(x)
#F: x er strengur
#E: Fallið skilar True ef x táknar að leikmaðurinn vilji draga spil
def VilDraga(x):
	if x=="d" or x=="draga" or x=="draw":
		return True
	else:
		return False
		
#Fall sem athugar hvort notandinn vill hreyfa spila
#N: VilHreyfa(x)
#F: x er strengur
#E: Fallið skilar True ef x táknar að leikmaðurinn vilji hreyfa spil
def VilHreyfa(x):
	if x=="h" or x=="hreyfa" or x=="hreyfdu" or x=="hreyfðu":
		return True
	else:
		return False

#Fall sem spyr notandann hvað hann vilji hreyfa, og kallar svo á Hreyfa(*)
#N: HreyfaHvad(Spilari)
#F: 
#E: Kallað hefur verið á Hreyfa(*) með þeim viðföngum sem notandinn skilgreindi
def HreyfaHvad(Spilari):
	b1=raw_input("Bunki 1: ")
	b2=raw_input("Bunki 2: ")
	num1=raw_input("Spil 1: ")
	if b2=="g0" or b2=="g1" or b2=="g2" or b2=="g3":
		Spilari.Hreyfa(b1,b2,num1,num1)
	else:
		num2=raw_input("Spil 2: ")
		Spilari.Hreyfa(b1,b2,num1,num2)

#Fall sem segir forritinu að hætta leiknum
#N: Stoppa(x)
#F: x er strengur af lágstöfum
#E: Fallið skilar True ef x táknar að það eigi að hætta leiknum, annars False
def Stoppa(x):
	if x=="q" or x=="quit" or x=="stop" or x=="stopp" or x=="stoppa" or x=="hætta":
		return True
	else:
		return False

#Fall sem skilgreinir terminalspilun og leikjalúppu fyrir Spilara, notar öll promptföllin
#N: Terminalspilun(Spilari
#F: ?
#E: ?
def Terminalspilun(Spilari):
	pass

#Fall sem athugar hvort notandinn vill sjá leikreglurnar aftur
#N: Hjalp(x)
#F: x er strengur
#E: Skilar True ef x táknar að notandinn vilji sjá reglurnar, annars False
def Hjalp(x):
	if x=="hjalp" or x=="reglur" or x=="r":
		return True
	else:
		return False

#Fall sem prentar leikreglurnar á skjáinn
#N: Leikreglur()
#F: Ekkert
#E: Búið er að prenta leikreglurnar á skjáinn
def Leikreglur():
	print "Leyfilegar skipanir: Hreyfa(H), Reglur(R), Hætta(Q)"
	print ""

#Fall sem prentar út "Ólöglegur leikur"
#N: Villa()
#F: Ekkert
#E: Strengurinn "Ólöglegur leikur" hefur verið skrifaður á staðalúttak
def Villa():
	print "Ólöglegur leikur"

#Fall sem skrifar mynd og leikreglurnar á skjáinn þegar leikurinn hefst
#N: Byrjun()
#F: Ekkert
#E: Myndin og leikreglurnar hafa verið skrifaðar á staðalúttak
def Byrjun():
	print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	print "  _____   ______   __      ______  ______   ______   ______  _____     ______ "
	print " /  ___| /  __  \ |  |    |_    _||_    _| /  __  \ |_    _|/  __ \   |   ___|"
	print "|  /    /  /  \  \|  |      |  |    |  |  /  /  \  \  |  |  | |  \ \  |  |    "
	print "|  \__  |  |  |  ||  |      |  |    |  |  |  |__|  |  |  |  | |__/ /  |  |___ "
	print " \__  \ |  |  |  ||  |      |  |    |  |  |   __   |  |  |  |  __ \   |   ___|"
	print "__  |  ||  |  |  ||  |      |  |    |  |  |  |  |  |  |  |  | |  \ \  |  |    "
	print "| |_/  |\  \__/  /|  |___  _|  |_   |  |  |  |  |  | _|  |_ | |   \ \ |  |___ "
	print "\_____/  \______/ |______||______|  |__|  |__|  |__||______||_|    \_||______|"
	print "                                                                              "
	print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	print ""
	Leikreglur()

#Fall sem kveður notandann
#N: Bless()
#F: Ekkert
#E: Kveðja til notandans hefur verið skrifuð á staðalúttak
def Bless():
	print "Bless."
	
#Fall sem skrifar mynd á skjáinn þegar leikmaðurinn sigrar
def Vinna():
	pass

#Fall sem skrifar mynd á skjáinn þegar leikmaðurinn tapar
def Tapa():
	pass