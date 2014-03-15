# -*- coding: utf-8 -*-

#Tilkynningar til, og skipanir frá notanda

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

#Fall sem segir forritinu að hætta leiknum
#N: Stoppa(Spilari)
#F: ?
#E: ?
def Stoppa(Spilari):
    pass

#Fall sem skilgreinir terminalspilun og leikjalúppu fyrir Spilara, notar öll promptföllin
#N: Terminalspilun(Spilari
#F: ?
#E: ?
def Terminalspilun(Spilari):
	pass

#Fall sem prentar leikreglurnar á skjáinn
#N: Leikreglur()
#F: Ekkert
#E: Búið er að prenta leikreglurnar á skjáinn
def Leikreglur():
	pass

#Fall sem prentar út "Ólöglegur leikur"
#N: Villa()
#F: Ekkert
#E: Strengurinn "Ólöglegur leikur" hefur verið skrifaður á staðalúttak
def Villa():
	print "Ólöglegur leikur"

#Fall sem skrifar mynd og leikreglurnar á skjáinn þegar leikurinn hefst
def Byrjun():
	print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	print " ______   ______   __      ______  ______   ______   ______  _____     ______ "
	print "/   ___| /  __  \ |  |    |_    _||_    _| /  __  \ |_    _|/  __ \   |   ___|"
	print "|  |    /  /  \  \|  |      |  |    |  |  /  /  \  \  |  |  | |  \ \  |  |    "
	print "|  \__  |  |  |  ||  |      |  |    |  |  |  |  |  |  |  |  | |   | | |  |    "
	print "\___  \ |  |  |  ||  |      |  |    |  |  |  |__|  |  |  |  | |__/ /  |  |___ "
	print "    |  ||  |  |  ||  |      |  |    |  |  |   __   |  |  |  |  __ \   |   ___|"
	print "__  |  ||  |  |  ||  |      |  |    |  |  |  |  |  |  |  |  | |  \ \  |  |    "
	print "| |_/  |\  \__/  /|  |___  _|  |_   |  |  |  |  |  | _|  |_ | |   \ \ |  |___ "
	print "\_____/  \______/ |______||______|  |__|  |__|  |__||______||_|    \_||______|"
	print "                                                                              "
	print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	print ""
	Leikreglur()

#Fall sem skrifar mynd á skjáinn þegar leikmaðurinn sigrar
def Vinna():
	pass

#Fall sem skrifar mynd á skjáinn þegar leikmaðurinn tapar
def Tapa():
	pass