# -*- coding: utf-8 -*-
import pygame.image
import pygame.rect
import os.path
from Spilastokkur import Spil

#Stillingar fyrir myndirnar
class Stillingar:
    Upplausn=(124,174)
    Upphafs_bil=10
    Linubil=30
    Spassia=20
    Flis_litid_bil=5
    Flis_stort_bil=15
    Hradi=500

#Fall sem hleður inn myndum
def HladaMynd(nafn_spils) :
    mynd =  pygame.image.load(nafn_spils.path)
    return image.convert_alpha()

#Einfaldur klasi sem allir aðrir hlutir nota
class AbstractHlutur(object):
    def __init__(self, nafn, stadsetning):
        #Nafn hlutsins
        self.nafn=nafn
        #Staðsetning hlutsins (byrjar sem 0-víddar rétthyrningur)
        self.rammi=pygame.Rect(stadsetning[0],stadsetning[1],0,0)
        
    #Athuga hvort að x,y staðsetning er í hlutnum
    def hefStadsetningu(self, stadsetning):
        if not self.synilegt:return False
        return self.rammi.collidepoint(stadsetning)
    
    #Athuga hvort að það er árekstur
    def hefArekstur(self, hlutur):
        return self.rammi.colliderect(hlutur.rammi)
    
    #Skilar x,y staðsetningunni úr self.rammi
    def faStadsetningu(self):
        return (self.rammi.x, self.rammi.y)
    
    #Set staðsetningu
    def setjaStadsetningu(self,stadsetning):
        self.rammi.x, self.rammi.y = stadsetning[0], stadsetning[1]
    
    #Hreyfi staðsetninguna
    def hreyfaStadsetningu(self,hreyfa):
        self.rammi.move_ip(hreyfa)

#Hlutur sem hefur mynd tengda við hann
class AbstractMynd(AbstractHlutur):
    def __init__(self, nafn, stadsetning, mynd):
        AbstractHlutur.__init__(self, nafn, stadsetning)
        #Allir hlutir hafa skilgreinda mynd
        self.mynd=self.setjaMynd(mynd)
        #Á að teikna hlutinn eða ekki
        self.synilegt=True
        
    #Einföld teikniskipun sem þarf undirklasa til að vera gagnleg
    def teikna(self, skjar):
        if self.synilegt:
            skjar.blit(mynd, self.rammi)
    
    #Hver hlutur er tengdur við mynd. Um leið og myndinni hefur verið
    #hlaðið inn þarf að uppfæra self.rammi tilviksbreytuna
    def setjaMynd(self,mynd):
        hlada=HladaMynd(mynd)
        self.rammi.w,self.rammi.h=hlada.get_width(),hlada.get_height()
        return hlada

