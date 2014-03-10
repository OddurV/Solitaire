# This Python file uses the following encoding: utf-8

import pondukapall

# Gengur mjoeg illa adh skilja einingaproufanir
# Hjer er samt mainfall sem gerir eitthvadh ie semi-aettina

    
def KlasaProuf_Spilari():
    print "\n(Þetta forrit notast við tvíhljóðaskrift {á: ae, æ: aj, ó: ou, ö: oe, ð: dh osfv.} útaf takmörkunum hins íslenska lyklaborðs og leti forritarans) \n\n"
    print "Velkomin ie Poendu-Kapal! \n"  
    o_o = raw_input("\n~Thetta er KlasaProuf, til adh syena virkni Spilara-klasans sem er notadhur ie poendukapli thessum.(Yettu alltaf ae enter til adh halda aefram)")
    o_o = raw_input("\n~Bye til eitt instance af klasanum")
    S = pondukapall.Spilari()
    o_o = raw_input("\n~Thadh er medh property-in: \n\tStokkur, sem er listi af spilum, en hvert spil er bara tuple.\n\t Hendi, sem er listi af spilunum sem eru dregin og spilarinn hefur ae hendi.\n\t SetjaAftastFremst, sem heldur utan um hve oft spilarinn hefur fengidh adh setja aftasta spil handar sinnar fremst. En hann mae thadh bara einu sinni.")
    o_o = raw_input("\n~Nue prenta jeg allan stokkinn:")
    for spil in S.Stokkur:
        print pondukapall.toString_spil(spil)
    o_o = raw_input("\n~Spilarinn dregur 12 spil, nota til thess adhferdhina dragaSpil toulf sinnum:\n")
    for i in range(0,12) :
        print S.dragaSpil()
    o_o = raw_input("\n~Nue er stokkurinn bara:")
    for spil in S.Stokkur:
        print pondukapall.toString_spil(spil)
    o_o = raw_input("\n~Adhferdhin toString_Hendi() strengjar hendi spilarans svona:")
    print S.toString_Hendi()
    o_o = raw_input("\n~Nue verdhur theim spilum hent - medh adhferdhinni hendaSpilum - sem hajgt er adh henda, ef einhver:")
    a = False
    for i, spil in enumerate(S.Hendi): #Thessi lykkja virkar ekki alveg 100%. Thadh er viest ekki snidhugt adh eydha hlutum af lista sem veridh er adh iterate-a ie gegnum ie Python.
        if i >= len(S.Hendi)-5:
            break
        if spil[0] == S.Hendi[i+3][0]:
            print pondukapall.toString_spil(S.Hendi[i+1]) + " og " + pondukapall.toString_spil(S.Hendi[i+2]) + " er hent."
            a = a or S.hendaSpilum(i+1+1, i+2+1)
        elif spil[1] == S.Hendi[i+3][1]:
            print pondukapall.toString_spil(spil) + ", "+ pondukapall.toString_spil(S.Hendi[i+1]) + ", "+ pondukapall.toString_spil(S.Hendi[i+2]) + " og " + pondukapall.toString_spil(S.Hendi[i+3]) + " er hent."
            a = a or S.hendaSpilum(i+1,i+3+1)
    while (not a) and len(S.Stokkur) > 19: 
        o_o = raw_input("\n~Ekki toukst thetta, aetla adh draga 20 spil og reyna aftur:")
        for i in range(0,12) :
            S.dragaSpil()
        print S.toString_Hendi()
        for i, spil in enumerate(S.Hendi):
            if i >= len(S.Hendi)-5:
                break
            if spil[0] == S.Hendi[i+3][0]:
                print pondukapall.toString_spil(S.Hendi[i+1]) + " og " + pondukapall.toString_spil(S.Hendi[i+2]) + " er hent."
                a = a or S.hendaSpilum(i+1+1, i+2+1)
            elif spil[1] == S.Hendi[i+3][1]:
                print pondukapall.toString_spil(spil) + ", "+ pondukapall.toString_spil(S.Hendi[i+1]) + ", "+ pondukapall.toString_spil(S.Hendi[i+2]) + " og " + pondukapall.toString_spil(S.Hendi[i+3]) + " er hent."
                a = a or S.hendaSpilum(i+1,i+3+1)
    
    if not a:
        o_o = raw_input("\n~dem")
    
    print "\nNue er hendi spilarans:\n" + S.toString_Hendi()
    
    if not a:
        print "\nThae hafa oell property Spilara klasans veridh syend. Fyrir utan hendaSpilum, en huen verdhur notudh fullt ie Syenileiknum rjett strax"
    else:
        print "\nThae hafa oell property Spilara klasans veridh syend."
        


def TerminalProuf():  
    S = pondukapall.Spilari()
    S.Stokkur = [('H',4),('L',5),('S',13),('H',12),('T',1),('L',8),('H',1),('S',1)]
    o_o = raw_input("Thetta er syeningarleikur medh forsnidhnum stokk. Spilari byrjar ae adh draga fjoegur spil (Yettu alltaf ae enter til adh halda aefram)")
    print "Thue drougst " + S.dragaSpil()
    print "Thue drougst " + S.dragaSpil()
    print "Thue drougst " + S.dragaSpil()
    print "Thue drougst " + S.dragaSpil()
    print S.toString_Hendi()
    o_o = raw_input("\n~Spilari aekvedhur adh henda oellum spilum og draga svo fjoegur nye spil: \n")
    S.hendaSpilum(1,4)
    print "Thue drougst " + S.dragaSpil()
    print "Thue drougst " + S.dragaSpil()
    print "Thue drougst " + S.dragaSpil()
    print "Thue drougst " + S.dragaSpil()
    o_o = raw_input("\n~Stokkurinn er bueinn og spilari getur hent tveimur:\n")
    S.hendaSpilum(2,3)
    print S.toString_Hendi()
    o_o = raw_input("\n~Spilari hefur sigradh!\n")
    pondukapall.printPanda()
    
if __name__ == "__main__":
    KlasaProuf_Spilari()
    TerminalProuf()