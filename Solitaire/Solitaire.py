# -*- coding: utf-8 -*-
from Spilastokkur import *
from Spilari import *
from Reglur import *
from Prompt import *



if __name__=="__main__":
    #Stilli upp fyrsta leiknum
    Spilari=Spilari()
    Byrjun()
    
    
    #Leikjalykkja
    while True:
        Stada(Spilari)
        x=Adgerd()
        if Stoppa(x):
            Bless()
            break
        elif VilDraga(x):
            Spilari.Draga()
        elif VilHreyfa(x):
            HreyfaHvad(Spilari)
        elif VilFletta(x):
            FlettaHvad(Spilari)
        elif VilByrja(x):
            print ""
            print "Þessi skipun virkar ekki núna."
            print "Vinsamlegast endurræstu leikin til að byrja aftur."
            break
        #    Spilari=Spilari()
        #    Byrjun()
        elif Hjalp(x):
            Leikreglur()
        else:
            Leikreglur()