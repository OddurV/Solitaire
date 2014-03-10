# This Python file uses the following encoding: utf-8

import random
import sys
import math

def toString_spil(spil):
    sort = spil[0]
    gildi = spil[1]
    toString_sort = {
        'H' : "Hjarta-", 
        'S' : "Spadha-",
        'T' : "Tiegul-",
        'L' : "Laufa -", #betra ef noefn allra sorta eru jafnloeng
    }
    toString_gildi = {
        1 : "Aes",
        2 : "tvistur",
        3 : "thristur",
        4 : "fjarki",
        5 : "fimma",
        6 : "sexa",
        7 : "sjoea",
        8 : "aetta",
        9 : "niea",
        10: "tiea",
        11: "Gosi",
        12: "Drottning",
        13: "Koungur",
    }
    return toString_sort[sort] + toString_gildi[gildi]

class Spilari(object):
    def __init__(self):
        self.Hendi = []
        self.Stokkur = zip(['H']*13 + ['S']*13 + ['T']*13 + ['L']*13, range(1,14)*4)
        self.SetjaAftastFremst = 0 #telur hve oft spilari hefur fengidh adh setja aftasta spil handar sinnar fremst. Mae bara einu sinni.
        random.shuffle(self.Stokkur)
    
    def toString_Hendi(self):
        HendiString = ""
        for i, spil in enumerate(self.Hendi):
            HendiString += "(Nr." + str(i+1) + ")"
            HendiString += toString_spil(spil)
            if i < len(self.Hendi)-2:
                HendiString += ", " + "\n" #adh hafa newline er margfallt lajsilegra
            if i == len(self.Hendi)-2:
                HendiString += " og "  + "\n" 
            if i == len(self.Hendi)-1:
                HendiString += "."
        return HendiString
    
    #Fyrir: len(self.Stokkur) > 0
    #Eftir: Efsta spili stokksins hefur veridh bajtt vidh hendina. Skilar streng spilsins 
    def dragaSpil(self):
        spil = self.Stokkur.pop()
        self.Hendi.append(spil)
        return toString_spil(spil)
    
    # Fyrir: len(self.Hendi) >= frae > 0 og len(self.Hendi) >= til > frae 
    # Eftir: skilar True ef thad var toukst adh henda spilunum - m.oe.o. var loeglegt -, skilar annars False
    def hendaSpilum(self, frae, til): 
        frae -= 1
        til -= 1 #notandinn hugsar nuemeringuna frae 1 en ekki 0
        if  frae != 0 and til != len(self.Hendi)-1 and til-frae == 1 and self.Hendi[frae-1][0] == self.Hendi[til+1][0]: 
        # ef spilin eru milli spila af soemu sort og eru tvoe    
            del self.Hendi[frae : til+1] 
            # del listi[a:b] deletar stoekum frae og medh a til og medh b-1
            return True
        
        if til-frae == 3 and self.Hendi[frae][1] == self.Hendi[til][1]:
        # ef eru fjoegur og annadh og thridhja theirra eru ae milli spila medh sama gildi
            del self.Hendi[frae : til+1]
            return True    
            
        return False

#Fyrir: S er hlutur af tagi Spilari
#Eftir: Skilar True ef Spilari hefur unnidh, False annars. 
def victoryCheck(S):
    return len(S.Stokkur)==0 and (len(S.Hendi)==0 or len(S.Hendi)==2)

#Eftir: Prentar ASCII poendu
def printPanda():
        print "                              _,add8ba,"
        print "                            ,d888888888b,"
        print "                           d8888888888888b                        _,ad8ba,_"
        print "                          d888888888888888)                     ,d888888888b,"
        print "                          I8888888888888888 _________          ,8888888888888b"
        print "                __________`Y88888888888888P\"\"\"\"\"\"\"\"\"\"\"baaa,__ ,888888888888888,"
        print "            ,adP\"\"\"\"\"\"\"\"\"\"\"9888888888P\"\"^                 ^\"\"Y8888888888888888I"
        print "         ,a8\"^           ,d888P\"888P^                           ^\"Y8888888888P'"
        print "       ,a8^            ,d8888'                                     ^Y8888888P'"
        print "      a88'           ,d8888P'                                        I88P\"^"
        print "    ,d88'           d88888P'                                          \"b,"
        print "   ,d88'           d888888'                                            `b,"
        print "  ,d88'           d888888I                                              `b,"
        print "  d88I           ,8888888'            ___                                `b,"
        print " ,888'           d8888888          ,d88888b,              ____            `b,"
        print " d888           ,8888888I         d88888888b,           ,d8888b,           `b"
        print ",8888           I8888888I        d8888888888I          ,88888888b           8,"
        print "I8888           88888888b       d88888888888'          8888888888b          8I"
        print "d8886           888888888       Y888888888P'           Y8888888888,        ,8b"
        print "88888b          I88888888b      `Y8888888^             `Y888888888I        d88,"
        print "Y88888b         `888888888b,      `\"\"\"\"^                `Y8888888P'       d888I"
        print "`888888b         88888888888b,                           `Y8888P^        d88888"
        print " Y888888b       ,8888888888888ba,_          _______        `\"\"^        ,d888888"
        print " I8888888b,    ,888888888888888888ba,_     d88888888b               ,ad8888888I"
        print " `888888888b,  I8888888888888888888888b,    ^\"Y888P\"^      ____.,ad88888888888I"
        print "  88888888888b,`888888888888888888888888b,     \"\"      ad888888888888888888888'"
        print "  8888888888888698888888888888888888888888b_,ad88ba,_,d88888888888888888888888"
        print "  88888888888888888888888888888888888888888b,`\"\"\"^ d8888888888888888888888888I"
        print "  8888888888888888888888888888888888888888888baaad888888888888888888888888888'"        
        print "  Y8888888888888888888888888888888888888888888888888888888888888888888888888P"
        print "  I888888888888888888888888888888888888888888888P^  ^Y8888888888888888888888'"
        print "  `Y88888888888888888P88888888888888888888888888'     ^88888888888888888888I"
        print "   `Y8888888888888888 `8888888888888888888888888       8888888888888888888P'"
        print "    `Y888888888888888  `888888888888888888888888,     ,888888888888888888P'"
        print "     `Y88888888888888b  `88888888888888888888888I     I888888888888888888'"
        print "       \"Y8888888888888b  `8888888888888888888888I     I88888888888888888'"
        print "         \"Y88888888888P   `888888888888888888888b     d8888888888888888'"
        print "            ^\"\"\"\"\"\"\"\"^     `Y88888888888888888888,    888888888888888P'"
        print "                             \"8888888888888888888b,   Y888888888888P^"
        print "                             `Y888888888888888888b   `Y8888888P\"^"
        print "   TIL HAMINGJU!                \"Y8888888888888888P     `\"\"\"\"^"
        print "                                  `\"YY88888888888P'"
        print "       THUE VANNST                    ^\"\"\"\"\"\"\"\"'\n\n"

# Fyrir: S er Spilari
# Eftir: Spilari hefur unnið leikinn eða gefist upp
def terminalSpilun(S):
        
    def prentaReglur():
        print "\nReglur:"
        print "\tThue vinnur ef stokkurinn er bueinn og thue ert medh tvoe edha ekkert spil ae hendi." 
        print "Thue maett henda tveimur spilum ef thau eru einu spilin ae milli tveggja spila af soemu sort."
        print "Thue maett henda fjourum spilum ef thau eru oell hlidh vidh hlidh og fyrsta og  spilidh hafa sama gildi.\n\n"
     
    # Eftir: Spilum hefur veridh hent einu sinni (tveimur edha fjourum) edha spilari hajtti vidh 
    def HendaSpilumTerminal(S):
        if len(S.Hendi) < 4:
            print "Thu tharft adh hafa a.m.k. 4 spil ae hendi til adh geta hent einhverju."
            prentaReglur()
            return
        
        print "Hvadha spilum viltu henda? (Skrifadhu nuemer)"
        frae = raw_input("Frae Nr.: ")
        while not frae.isdigit() or int(frae) >= len(S.Hendi) or int(frae) < 1 :
            #Fyrirskilyrdhum Spilari.hendaSpilum uppfyllt
            frae = raw_input("Skrifadhu toelustaf frae 1 til " + str((len(S.Hendi)-1)) + ": ")    
        til = raw_input("Til Nr.: ")
        while not til.isdigit() or int(til) > len(S.Hendi) or int(til) < int(frae) :
            #Fyrirskilyrdhum Spilari.hendaSpilum uppfyllt
            til = raw_input("Skrifadhu toelustaf frae " + str(int(frae)+1) + " til " + str(len(S.Hendi))+ ": ")
        
        while not S.hendaSpilum(int(frae),int(til)) : #<-------
            print "Ekki er loeglegt adh henda spilum nr." + str(frae) + " til nr." + str(til)
            prentaReglur()
            
            val = raw_input("Viltu velja oennur spil? (J/N)")
            while len(val)<1 or (val[0].lower() != 'j' and val[0].lower() != 'n'):
                val = raw_input("Skil ekki, svaradhu Jae edha Nei: ")
            
            if val == 'n':
                return
            
            frae = raw_input("Frae Nr.: ")
            while not frae.isdigit() or int(frae) >= len(S.Hendi) or int(frae) < 1 :
                frae = raw_input("Skrifadhu toelustaf frae 1 til " + str((len(S.Hendi)-1)) + ": ")
            til = raw_input("Til Nr.: ")
            while not til.isdigit() or int(til) > len(S.Hendi) or int(til) <= int(frae) :
                til = raw_input("Skrifadhu toelustaf frae " + str(int(frae)+1) + " til " + str(len(S.Hendi)) + ": ")    
                
        print "Spilum hent."
        print "Hoendin thien er :\n" + S.toString_Hendi()
    
    # Hjer hefst leikurinn
    print "\nThue dregur fjoegur spil:"
    for i in range(0,4):
        print "Spilidh sem thue drougst er " + S.dragaSpil()
    
    #Leikjalykkjan
    while not victoryCheck(S) :    
        if S.SetjaAftastFremst < 1 and len(S.Stokkur)==0:
            print "Stokkurinn er bueinn."
            val = raw_input("Viltu setja aftasta spil handarinnar fremst? (J/N): ")
            while len(val)<1 or (val[0].lower() != 'j' and val[0].lower() != 'n'):
                val = raw_input("Skil ekki, svaradhu Jae edha Nei: ")
            if val[0].lower() == 'j':
                S.SetjaAftastFremst += 1 #er thae ordhid 1 og breytist ekki aftur
                snagi = S.Hendi.pop()
                S.Hendi.reverse()
                S.Hendi.append(snagi)
                S.Hendi.reverse()
            print "Hoendin thien er: \n" + S.toString_Hendi()
        if len(S.Stokkur)==0:
            val = raw_input("Hvort viltu Henda spilum edha gefast upp? (H/G): ")    
            while len(val)<1 or (val[0].lower() != 'h' and val[0].lower() != 'g'):
                val = raw_input("Skil ekki, svaradhu Henda edha Gefast upp (H/G): ")         
            if val == 'h':
                HendaSpilumTerminal(S)  #<---------
            else: 
                break
        else:
            val = raw_input("Viltu Henda spilum edha Draga annadh? (H/D)")
            while len(val)<1 or (val[0].lower() != 'h' and val[0].lower() != 'd'):
                val = raw_input("Skil ekki, svaradhu Henda edha Draga: ")
            if val[0].lower() == 'd':
                print "Spilidh sem thue drougst er " + S.dragaSpil() #<---------
                print "Thadh eru ae bilinu " + str(int(10*math.floor(len(S.Stokkur)/10.0))) + " og " + str(int(10*math.ceil((1+len(S.Stokkur))/10.0))) + " spil eftir." 
                print "Hoendin thien er: \n" + S.toString_Hendi() 
            else:
                HendaSpilumTerminal(S) #<---------
    
    if victoryCheck(S):
        printPanda()
    else:
        print "Thue hefur tapadh.\n"
        
    
if __name__ == "__main__":
    print "(Þetta forrit notast við tvíhljóðaskrift (á : ae, æ : aj, ó = ou, ö = oe, osfv.) útaf takmörkunum hins íslenska lyklaborðs og leti forritarans) \n\n"
    print "Velkomin ie Poendu-Kapal\n"
    val = raw_input("Ajtlardhu adh spila? (J/N): ")
    while len(val)<1 or (val[0].lower() != 'j' and val[0].lower() != 'n'):
        val = raw_input("Skil ekki, svaradhu Jae edha Nei: ")
    if val[0].lower() == 'n':
        print "Bless."
        sys.exit()
    S = Spilari()
    terminalSpilun(S) #<---------
    val = raw_input("Taka annan?")
    while len(val)<1 or (val[0].lower() != 'j' and val[0].lower() != 'n'):
        val = raw_input("Skil ekki, svaradhu Jae edha Nei: ")
    while val == 'j':
        S = Spilari()
        terminalSpilun(S) # <------
        val = raw_input("Taka annan?")
        while len(val)<1 or (val[0].lower() != 'j' and val[0].lower() != 'n'):
            val = raw_input("Skil ekki, svaradhu Jae edha Nei: ")
    print "Bless."
    sys.exit()