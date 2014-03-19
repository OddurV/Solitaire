# -*- coding: utf-8 -*-
#ODDUR ER AÐ VINNA Í ÞESSARI SKRÁ!
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
        if VilDraga(x):
            Spilari.Draga()
        if VilHreyfa(x):
            HreyfaHvad(Spilari)
        if Hjalp(x):
            Leikreglur()
        