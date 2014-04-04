# -*- coding: utf-8 -*-
import pygame
import sys
from GUI_hlutir import *
from GUI_abstract import Stillingar
from pygame.locals import *
import random

class tvismellur:
    def __init__(self):
        self.tvi_smellur=pygame.time.Clock()
        self.time=0
        self.fyrri_smellur=True
        self.varTS=False
    
    def erTS(self,event):
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            smell_timi=self.tvi_smellur.tick()
            if not self.fyrri_smellur:
                if smell_timi>Stillingar.Hradi: self.fyrri_smellur=True
                else: self.time=smell_timi
        
        if event.type==MOUSEBUTTONUP and event.button==1:
            if not self.fyrri_smellur:
                smell_timi=self.tvi_smellur.tick()
                self.fyrri_smellur=True
                if smell_timi+self.time<Stillingar.Hradi:
                    self.varTS=True
                    return True
            else: self.fyrri_smellur=False
        self.varTS=False
        return False

class Leikur:
    def __init__(self):
        pygame.init()
        random.seed()
        self.skjar=self.setjaSkja()
        self.tvi_smellur=tvismellur()
        self.hreyfa_stafla=geymsla("geymsla")
        
        self.spilalisti=self.hladaSpilum()
        self.staflar=self.hladaStafla()
    
    def setjaSkja(self):
        x_dim=(Stillingar.Spassia*2)+(Stillingar.Upplausn[0]*7)+(Stillingar.Upphafs_bil*6)
        y_dim=Stillingar.Spassia+(Stillingar.Upplausn[1]*2) + Stillingar.Linubil
        y_dim +=(Stillingar.Flis_litid_bil*6)+(Stillingar.Flis_stort_bil*12)
        return pygame.display.set_mode((x_dim,y_dim))
        
    def hladaSpilum(self):
        Spil.HladaBakhlid("Myndir/Bakhlid.jpg")
        spilalisti=[]
        for i in ["h","s","t","l"]:
            for j in range(1,14):
                spilalisti.append(Spil(i,j,(0,0)))
        random.shuffle(spilalisti)
        return spilalisti
        
    def hladaStafla(self):
        staflar=[]
        lokastaflar=[]
        lokaStafli.heildarfjoldi_spila=0
        
        merki=0
        x=Stillingar.Spassia
        y=Stillingar.Spassia+Stillingar.Upplausn[1]+Stillingar.Linubil
        for i in range(1,8):
            staflanafn="Megin"+str(i)
            spilalisti=self.spilalisti[merki:i+merki]
            staflar.append(MeginStafli(staflanafn,(x,y),"Myndir/Bakhlid.jpg",Stillingar.Flis_litid_bil,Stillingar.Flis_stort_bil,spilalisti))
            if i>3: lokastaflar.append(lokaStafli("Lokastafli"+str(i-3),(x,Stillingar.Spassia),"Myndir/Bakhlid.jpg"))
            x += staflar[-1].rammi.w+Stillingar.Upphafs_bil
            merki +=i
        
        spilalisti=self.spilalisti[merki:52]
        staflar.append(Upphafsstafli("Upphafsstafli",(Stillingar.Spassia,Stillingar.Spassia),Stillingar.Upphafs_bil,"Myndir/Bakhlid.jpg",spilalisti))
        
        staflar.extend(lokastaflar)
        return staflar
        
    def smellturStafli(self,event):
        for stafli in self.staflar:
            if stafli.hefStadsetningu(event.stadsetning): return stafli
        
    def leikjalykkja(self):
        while True:
            if self.sigurskilyrdi():
                self.browninanHreyfing(2)
            
            for event in pygame.event.get():
                if (event.type==MOUSEBUTTONUP or event.type==MOUSEBUTTONDOWN) and event.button==1:
                    self.tvi_smellur.erTS(event)
                
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type==KEYUP and event.key==K_r:
                    self.reset()
                
                if self.sigurskilyrdi():
                    if event.type==MOUSEBUTTONUP and event.button==1:
                        self.endurraesa()
                
                else:
                    if event.type==MOUSEBUTTONUP and event.button==1:
                        hreyfa_stafla_allan=self.hreyfa_stafla.hefSpil()
                        
                        if hreyfa_stafla_allan:
                            valinn_stafli=None
                            for stafli in self.staflar:
                                if stafli.leyfaFleiriSpil(self.hreyfa_stafla.spilalisti):
                                    valinn_stafli=stafli
                                    break
                            if valinn_stafli: self.hreyfa_stafla.leggjaIStafla(valinn_stafli)
                            else: self.hreyfa_stafla.skilaSpilum()
                            
                        if self.tvi_smellur.varTS: self.aTvismelli(event)
                        
                        if not hreyfa_stafla_allan and not self.tvi_smellur.varTS:
                            valinn_stafli=self.smellturStafli(event)
                            
                    if event.type==MOUSEBUTTONDOWN and event.button==1:
                        valinn_stafli=self.smellturStafli(event)
                        
                        if valinn_stafli:
                            taka_spil=valinn_stafli.aSmelli(event)
                            if taka_spil: self.hreyfa_stafla.hreyfaStadsetningu(event.rel)
                            
            self.skjar.fill((0,0,0))
            self.teikna()
            pygame.display.flip()
        
    def aTvismelli(self,event):
        smelltur_stafli=self.smellturStafli(event)
        
        if smelltur_stafli:
            taka_spil=smelltur_stafli.aTvismelli(event)
            if taka_spil:
                ekki_heima=True
                for stafli in self.staflar[-4:]:
                    if stafli.leyfaFleiriSpil(taka_spil,False):
                        stafli.leggjaSpil(taka_spil)
                        ekki_heima=False
                        break;
                if ekki_heima: taka_spil[0].stafli.leggjaSpil(taka_spil)
            
    def teikna(self):
        for stafli in self.staflar:
            stafli.teikna(self.skjar)
        self.hreyfa_stafla.teikna(self.skjar)
        
    def byrja(self):
        self.leikjalykkja()
        
    def sigurskilyrdi(self):
        return lokaStafli.heildarfjoldi_spila==len(self.spilalisti)
    
    def browninanHreyfing(self, lengd):
                for stafli in self.staflar :
                        x_hreyfa= random.randint(-lengd, lengd)
                        y_hreyfa= random.randint(-lengd, lengd)
                        stafli.hreyfaStadsetningu((x_hreyfa, y_hreyfa))
        
    def endurraesa(self):
        self.spilalisti=self.hladaSpilum()
        self.staflar=self.hladaStafla()
        
if __name__ == "__main__":
    l=Leikur()
    l.byrja()