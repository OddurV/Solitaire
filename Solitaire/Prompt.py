# -*- coding: utf-8 -*-
from Spilari import *

#Tilkynningar til, og skipanir frá notanda

#Fall sem biður notandann um inntak, og skilar því í lágstöfum
#N: x=Adgerd()
#F: Ekkert
#E: Staðalinntaki hefur verið skilað á lágstafaformi
def Adgerd():
    x=raw_input("Hvað viltu gera? ")
    return x.lower().strip()

#Fall sem prentar stöðuna í leiknum
#N: Stada(Spilari)
#F: Ekkert
#E: Staða spilsins 
def Stada(Spilari):
    #Sýni stigin og tímann
    print "Stig: ",Spilari.Stig,"    Tími: ",int(Spilari.EndTime-Spilari.StartTime)
    #Spilastokkurinn
    print "Fjöldi spila í spilastokknum: ", len(Spilari.S)

    #Endurvinnslubunkinn
    if len(Spilari.E)==0:
        print "(0)  E: []"
    else:
        print "(0)  E: ",Spilari.E[len(Spilari.E)-1]

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
        temp2="("+str(i+1)+")  "
        for j in range(len(temp[i])):
            temp2=temp2+str(temp[i][j])+" "
        print temp2

    print ""

    #Sýni efstu spilin í grunninum
    if len(Spilari.G[0])==0:
        print "(8)  []"
    else:
        print "(8)  ", Spilari.G[0][len(Spilari.G[0])-1]
    if len(Spilari.G[1])==0:
        print "(9)  []"
    else:
        print "(9)  ", Spilari.G[1][len(Spilari.G[1])-1]
    if len(Spilari.G[2])==0:
        print "(10) []"
    else:
        print "(10) ", Spilari.G[2][len(Spilari.G[2])-1]
    if len(Spilari.G[3])==0:
        print "(11) []"
    else:
        print "(11) ", Spilari.G[3][len(Spilari.G[3])-1]
        
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

#Fall sem athugar hvort notandinn vill snúa við spili
#N: VilFletta(x)
#F: x er strengur
#E: Fallið skilar True ef x táknar að leikmaðurinn vilji snúa við spili
def VilFletta(x):
    if x=="f" or x=="fletta" or x=="snúa":
        return True
    else:
        return False

#Fall sem athugar hvort notandinn vill byrja á nýjum leik
#N: VilByrja(x)
#F: x er strengur
#E: Fallið skilar True ef x táknar að leikmaðurinn vilji byrja á nýjum leik
def VilByrja(x):
    if x=="b" or x=="byrja" or x=="new" or x=="newgame":
        return True
    else:
        return False

#Fall sem spyr notandann í hvaða bunka spilið sem hann vill snúa er, 
#og kallar svo á Fletta(*)
#N: FlettaHvad(Spilari)
#F: Spilari er af taginu Spilari
#E: Kallað hefur verið á Fletta með þeim viðföngum sem notandinn skilgreindi
def FlettaHvad(Spilari):
    num=raw_input("Í hvaða bunka er spilið sem á að fletta? ")
    if num=="1" or num=="2" or num=="3" or num=="4" or num=="5" or num=="6" or num=="7":
        #Hleypi ekki inn rugl strengjum
        num=int(num)-1
    else:
        FlettaHvad(Spilari)
        return
    print ""
    
    if num<1 or num>6:
        Villa()
    else:
        if Spilari.Fletta(Spilari.UB[num],Spilari.B[num]):
            Spilari.Stig=Spilari.Stig+5
        else:
            Villa()

#Fall sem spyr notandann hvað hann vilji hreyfa, og kallar svo á Hreyfa(*)
#N: HreyfaHvad(Spilari)
#F: Spilari er af taginu Spilari
#E: Kallað hefur verið á Hreyfa(*) með þeim viðföngum sem notandinn skilgreindi
def HreyfaHvad(Spilari):
    b1=raw_input("Taka spil úr bunka númer: ")
    if b1=="0" or b1=="1" or b1=="2" or b1=="3" or b1=="4" or b1=="5" or b1=="6" or b1=="7" or b1=="8" or b1=="9" or b1=="10" or b1=="11":
        #Hleypi ekki inn rugl strengjum
        b1=int(b1)
    else:
        HreyfaHvad(Spilari)
        return
    if b1 != 0:
        num=raw_input("Byrja á spili númer: ")
        if num=="1" or num=="2" or num=="3" or num=="4" or num=="5" or num=="6" or num=="7" or num=="8" or num=="9" or num=="10" or num=="11" or num=="12" or num=="13":
            #Hleypi ekki inn rugl strengjum
            num=int(num)-1
            if num>len(Spilari.B[b1]):
                HreyfaHvad(Spilari)
                return
        else:
            HreyfaHvad(Spilari)
            return
    b2=raw_input("Setja í bunka númer: ")
    if b2=="0" or b2=="1" or b2=="2" or b2=="3" or b2=="4" or b2=="5" or b2=="6" or b2=="7" or b2=="8" or b2=="9" or b2=="10" or b2=="11":
        #Hleypi ekki inn rugl strengjum
        b2=int(b2)
    else:
        HreyfaHvad(Spilari)
        return
    print ""
    
    #Ef b1==0 þá er verið að taka efsta spilið úr endurvinnslubunkanum
    if b1==0:
        #Ef b2==0 þá er verið að reyna að setja spil í endurvinnslubunkan
        #Það er bannað.
        if b2==0:
            Villa()
        #Hér er verið að færa spil í einn af venjulegu bunkunum 7
        elif b2>0 and b2<8:
            if Spilari.Hreyfa(Spilari.E,Spilari.B[b2-1],Spilari.UB[b2-1], len(Spilari.E) - 1):
                Spilari.Stig=Spilari.Stig+5
            else:
                Villa()
        #Hér er verið að færa spil í einn af stöflunum 4
        else:
            if Spilari.LokaHreyfing(Spilari.E,Spilari.G[b2-8]):
                Spilari.Stig=Spilari.Stig+10
            else:
                Villa()
    #Ef 0<b1<8 þá er verið að færa spil úr einum af venjulegu bunkunum 7
    elif b1>0 and b1<8:
        #Bannað að setja í endurvinnslubunkan
        if b2==0:
            Villa()
        #Hér er verið að færa spil í einn af venjulegu bunkunum 7
        elif b2>0 and b2<8:
            if Spilari.Hreyfa(Spilari.B[b1-1],Spilari.B[b2-1],Spilari.UB[b2-1],num):
                pass
            else:
                Villa()
        #Hér er verið að færa spil í einn af stöflunum 4
        else:
            if Spilari.LokaHreyfing(Spilari.B[b1-1],Spilari.G[b2-8]):
                Spilari.Stig=Spilari.Stig+10
            else:
                Villa()
    #Ef b1>7 þá er verið að færa spil úr einum af stöflunum 4
    else:
        #Bannað að setja í endurvinnslubunkan
        if b2==0:
            Villa()
        #Hér er verið að færa spil í einn af venjulegu bunkunum 7
        elif b2>0 and b2<8:
            if Spilari.Hreyfa(Spilari.G[b1-8],Spilari.B[b2-1],Spilari.UB[b2-1],num):
                Spilari.Stig=Spilari.Stig-15
            else:
                Villa()
        #Það má ekki taka spil úr stafla og setja það í annan stafla
        else:
            Villa()

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
    print "Leyfilegar skipanir: Draga(D), Hreyfa(H), Fletta(F), Reglur(R), Byrja aftur(B), Hætta(Q)"
    print ""

#Fall sem prentar út "Ólöglegur leikur"
#N: Villa()
#F: Ekkert
#E: Strengurinn "Ólöglegur leikur" hefur verið skrifaður á staðalúttak
def Villa():
    print "Ólöglegur leikur!"
    print ""

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
#N: Vinna()
#F: Ekkert
#E: Notandinn hefur verið látinn vita að hann hafi sigrað kapalinn
def Vinna():
    print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    print "              _____  ______   _______   ___    __  _______     __             "
    print "             /  ___||_    _| /  ___  \ |  |   |  |/   __  \   |  |            "
    print "            |  /      |  |  /  /   \__||  |   |  ||  |  \  \  |  |            "
    print "            |  \__    |  |  |  |       |  |   |  ||  |__/  /  |  |            "
    print "             \__  \   |  |  |  |  ____ |  |   |  ||   __  \   |  |            "
    print "            __  |  |  |  |  |  | |_   ||  |   |  ||  |  \  \  |__|            "
    print "            | |_/  | _|  |_ \  \___/  ||  \___/  ||  |   \  \  __             "
    print "            \_____/ |______| \_______/  \_______/ |__|    \__||__|            "
    print "                                                                              "
    print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    print ""
    Leikreglur()

#Fall sem skrifar mynd á skjáinn þegar leikmaðurinn tapar
#N: Vinna()
#F: Ekkert
#E: Notandinn hefur verið látinn vita að hann hafi tapað
def Tapa():
    print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    print "                       ________  ______   _______    __                       "
    print "                      |__    __|/  __  \ /   __  \  |  |                      "
    print "                         |  |  /  /  \  \|  |  \  \ |  |                      "
    print "                         |  |  |  |__|  ||  |__/  / |  |                      "
    print "                         |  |  |   __   ||   ____/  |  |                      "
    print "                         |  |  |  |  |  ||  |       |__|                      "
    print "                         |  |  |  |  |  ||  |        __                       "
    print "                         |__|  |__|  |__||__|       |__|                      "
    print "                                                                              "
    print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    print ""
    Leikreglur()