# -*- coding: utf-8 -*-
import unittest
from Spilastokkur import *
from Solitaire import *
from Reglur import *
from Prompt import *
from Spilari import *

class Prufur(unittest.TestCase):
    def test_Spil_Eiginleikar(self):
        spil=Spil("H",1,"")
        self.assertEqual(spil.sort,"H")
        self.assertEqual(spil.gildi,1)
    
    def test_Spilastokkur_Lengd(self):
        S=Spilastokkur()
        self.assertEqual(len(S),52)
        spil=Spil("H",1,"")
    
    def test_Spilastokkur_Stokka1(self):
        #Athuga hvort að öll spilin séu enn í spilastokknum eftir stokkun
        S=Spilastokkur()
        A=[]
        for i in ["H","S","T","L"]:
            for j in range(1,14):
                A.append(Spil(i,j,""))
        
        for i in range(len(S)):
            flag=False
            for j in range(len(A)):
                flag=flag or S[i]==A[j]
            self.assertTrue(flag)
        
    
    def test_Spilastokkur_Stokka2(self):
        #Athuga hvort að spilastokkurinn hafi verið stokkaður
        S=Spilastokkur()
        A=[]
        for i in ["H","S","T","L"]:
            for j in range(1,14):
                A.append(Spil(i,j,""))
        for i in range(len(S)):
            flag=True
            flag=flag and (S[i].sort==A[i].sort and S[i].gildi==A[i].gildi)
        self.assertFalse(flag)
    
    def test_Spilastokkur_Taka(self):
        S=Spilastokkur()
        x=[S[len(S)-1].sort,S[len(S)-1].gildi]
        y=S.Taka()
        self.assertEqual(x[0],y.sort)
        self.assertEqual(x[1],y.gildi)
    
    def test_Spilastokkur_Leggja(self):
        S=Spilastokkur()
        x=Spil("H",1,"")
        S.Leggja(x)
        self.assertEqual(S[len(S)-1].sort,"H")
        self.assertEqual(S[len(S)-1].gildi,1)
    
    def test_Spilari_eiginleikar(self):
        Leikmadur=Spilari()
        self.assertTrue(len(Leikmadur.E)==0)
        print ""
        print "S[0]"
        print Leikmadur.S[0]
        print "len(E)"
        print len(Leikmadur.E)
        print "len(UB[0])"
        print len(Leikmadur.UB[0])
        print "UB"
        print Leikmadur.UB[1][0]
        print Leikmadur.UB[1][len(Leikmadur.UB[1])-1]
        print Leikmadur.UB[2][0]
        print Leikmadur.UB[3][0]
        print Leikmadur.UB[4][0]
        print Leikmadur.UB[5][0]
        print Leikmadur.UB[6][0]
        print "pop"
        #x=Leikmadur.UB[0].pop()
        #print x
        print "B"
        print Leikmadur.B[0][0]
        print Leikmadur.B[1][0]
        print Leikmadur.B[2][0]
        print Leikmadur.B[3][0]
        print Leikmadur.B[4][0]
        print Leikmadur.B[5][0]
        print Leikmadur.B[6][0]
        print "len(UB)"
        print len(Leikmadur.UB)
        
        
    
    def test_Spilari_Draga(self):
        Leikmadur=Spilari()
        x=Leikmadur.S[len(Leikmadur.S)-1]
        Leikmadur.Draga()
        self.assertEqual(x.sort,Leikmadur.E[0].sort)
        self.assertEqual(x.gildi,Leikmadur.E[0].gildi)
    
    def test_Spilari_Endurvinna(self):
        print ""
        Leikmadur=Spilari()
        Stada(Leikmadur)
        for i in range(24):
            Leikmadur.Draga()
        Stada(Leikmadur)
        Leikmadur.Endurvinna()
        Stada(Leikmadur)
        for i in range(24):
            Leikmadur.Draga()
        Stada(Leikmadur)
    
    def test_Spilari_Hreyfa(self):
        Leikmadur=Spilari()
        #Stada(Leikmadur)
        Byrja1=len(Leikmadur.B[0]) # = 1
        Byrja2=len(Leikmadur.B[1]) # = 2
         
        x = Leikmadur.B[0][0]
        y = Leikmadur.B[1][0]
        z = Leikmadur.B[2][0]
        th = Leikmadur.B[3][0]
        x.sort = "H"
        x.gildi = 13  # x er Hjartakóngur á bunka 0 frá vinstri
        y.sort = "L"
        y.gildi = 12 # y er Laufadrottning á bunka 1
        z.sort = "S"
        z.gildi = 11 # z er Spaðagosi á bunka 2
        th.sort = "L"
        th.gildi = 10 # th er Laufatía á bunka 3
        
        #Drottning sett á gosa - false vegna hærra og litar
        self.assertFalse(Leikmadur.Hreyfa(Leikmadur.B[1],Leikmadur.B[2],Leikmadur.UB[2],0))
        #Kóngur settur á gosa - false vegna hærra og langt í burtu
        self.assertFalse(Leikmadur.Hreyfa(Leikmadur.B[0],Leikmadur.B[2],Leikmadur.UB[2],0))
        #tía sett á gosa - false vegna litar
        self.assertFalse(Leikmadur.Hreyfa(Leikmadur.B[3],Leikmadur.B[2],Leikmadur.UB[2],0))
        # tía sett á kóng - false venga of langt í burtu
        self.assertFalse(Leikmadur.Hreyfa(Leikmadur.B[3],Leikmadur.B[1],Leikmadur.UB[1],0))
        # Kóngur settur á tíu - false vegna hærra, of langt í burtu og litar
        self.assertFalse(Leikmadur.Hreyfa(Leikmadur.B[0],Leikmadur.B[3],Leikmadur.UB[3],0))
        #Drottning sett á kóng - true
        self.assertTrue(Leikmadur.Hreyfa(Leikmadur.B[1],Leikmadur.B[0],Leikmadur.UB[0],0))
        #Tía settur á drottningu - false vegna of langt í burtu  og litar
        self.assertFalse(Leikmadur.Hreyfa(Leikmadur.B[3],Leikmadur.B[0],Leikmadur.UB[0],0))
        #gosi settur á Tíu - false vegna hærra
        self.assertFalse(Leikmadur.Hreyfa(Leikmadur.B[2],Leikmadur.B[3],Leikmadur.UB[3],0))
        
        #Stada(Leikmadur)
        Enda1=len(Leikmadur.B[0])
        Enda2=len(Leikmadur.B[1])
        self.assertEqual(Byrja1+1,Enda1)
        self.assertEqual(Byrja2,Enda2+1)
        
    def test_Spilari_Fletta(self):
        Leikmadur=Spilari()
        self.assertFalse(Leikmadur.Fletta(Leikmadur.UB[4],Leikmadur.B[4]))
        Leikmadur.B[4].pop()
        self.assertTrue(Leikmadur.Fletta(Leikmadur.UB[4],Leikmadur.B[4]))
    
    def test_Reglur_LeyfaFletta(self):
        Leikmadur = Spilari()
        Leikmadur.B[1].pop()
        self.assertTrue(LeyfaFletta(Leikmadur.UB[1],Leikmadur.B[1]))
        self.assertFalse(LeyfaFletta(Leikmadur.UB[3],Leikmadur.B[3]))
    
    def test_Reglur_LeyfilegHreyfing(self):
        Leikmadur=Spilari()
        Leikmadur.B[0].pop()
        Leikmadur.B[1][0]=Spil("H",2,"")
        Leikmadur.B[2][0]=Spil("L",3,"")
        Leikmadur.B[3][0]=Spil("H",1,"")
        Leikmadur.B[4][0]=Spil("S",13,"")
        self.assertFalse(LeyfilegHreyfing(Leikmadur.B[1],Leikmadur.UB[1],Leikmadur.B[3][0]))
        self.assertTrue(LeyfilegHreyfing(Leikmadur.B[2],Leikmadur.UB[2],Leikmadur.B[1][0]))
        self.assertFalse(LeyfilegHreyfing(Leikmadur.B[2],Leikmadur.UB[2],Leikmadur.B[4][0]))
        self.assertTrue(LeyfilegHreyfing(Leikmadur.B[0],Leikmadur.UB[0],Leikmadur.B[4][0]))

    def test_Reglur_Sigra(self):
        Leikmadur=Spilari()
        self.assertFalse(Sigra(Leikmadur.G))
        S=Spilastokkur()
        for i in range(4):
            for j in range(13):
                Leikmadur.G[i].append(S.Taka())
        self.assertTrue(Sigra(Leikmadur.G))
    
    def test_Reglur_Tapa(self):
        pass
    
    def test_Prompt_Stada(self):
        print ""
        Leikmadur=Spilari()
        Stada(Leikmadur)
    
    def test_Prompt_Byrjun(self):
        print ""
        Byrjun()
        
if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)