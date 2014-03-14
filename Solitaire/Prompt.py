# -*- coding: utf-8 -*-

#Tilkynningar til, og skipanir frá notanda

#Fall sem prentar stöðuna í leiknum
#N: Stada(Spilari)
#F: Ekkert
#E: Staða spilsins 
def Stada(Spilari):
	print "Fjöldi spila í spilastokknum: ", len(Spilari.S)
	print "E: ",Spilari.E[len(Spilari.E)]
	print ""
	tempUB=[[],[],[],[],[],[],[]]
	for i in range(7):
		for j in range(len(Spilari.UB[i])):
			tempUB[i]=tempUB[i]+"[*] "
	tempB=[[],[],[],[],[],[],[]]
	for i in range(7):
		for j in range(len(Spilari.B[i])):
			tempB[i]=tempB[i]+Spilari.B[i][j]+" "
	for i in range(7):
		print tempUB[i]+tempB[i]
	print ""
	print G[0][len(G[0])-1]
	print G[1][len(G[1])-1]
	print G[2][len(G[2])-1]
	print G[3][len(G[3])-1]

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

#Fall sem prentar út "Ólöglegur leikur"
#N: Villa()
#F: Ekkert
#E: Strengurinn "Ólöglegur leikur" hefur verið skrifaður á staðalúttak
def Villa():
	print "Ólöglegur leikur"