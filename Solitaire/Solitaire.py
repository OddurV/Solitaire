# -*- coding: utf-8 -*-
from Spilastokkur import *
from Spilari import *
from Reglur import *
from Prompt import *
import time
import shelve


if __name__=="__main__":
    #Stilli upp fyrsta leiknum
    Leikmadur=Spilari()
    Byrjun()
    
    #Leikjalykkja
    while True:
        Leikmadur.EndTime=time.time()
        Stada(Leikmadur)
        x=Adgerd()
        if Stoppa(x):
            Bless()
            break
        elif VilDraga(x):
            Leikmadur.Draga()
        elif VilHreyfa(x):
            HreyfaHvad(Leikmadur)
        elif VilFletta(x):
            FlettaHvad(Leikmadur)
        elif VilByrja(x):
            Leikmadurinn=Spilari()
            del Leikmadur
            Leikmadur=Leikmadurinn
            Byrjun()
        elif Hjalp(x):
            Leikreglur()
        else:
            Leikreglur()
        
        if Sigra(Leikmadur.G):
            Vinna()
            if Leikmadur.BreytaTopplista():
                Topplisti()