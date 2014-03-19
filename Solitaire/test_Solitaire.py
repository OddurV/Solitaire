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
        Byrja1=len(Leikmadur.B[0])
        Byrja2=len(Leikmadur.B[1])
        x=Leikmadur.B[0][0]
        if x.sort=="S" or x.sort=="L":
            y=Spil("H",x.gildi-1,"")
        else:
            y=Spil("S",x.gildi-1,"")
        Leikmadur.B[1][0]=y
        #Stada(Leikmadur)
        Leikmadur.Hreyfa(Leikmadur.B[1],Leikmadur.B[0],Leikmadur.UB[0],0)
        #Stada(Leikmadur)
        Enda1=len(Leikmadur.B[0])
        Enda2=len(Leikmadur.B[1])
        self.assertEqual(Byrja1+1,Enda1)
        self.assertEqual(Byrja2,Enda2+1)
        
    def test_Spilari_Fletta(self):
        pass
    
    def test_Reglur_LeyfaFletta(self):
        Leikmadur = Spilari()
        Leikmadur.B[1].pop()
        # Bunki tómur, Undirbunki ekki tómur
        self.assertTrue(Leikmadur.UB[1], Leikmadur.B[1])
        # Bunki ekki tómur, Undirbunki tómur
        self.assertFalse(Leikmadur.UB[0],Leikmadur.B[0])
        # Hvorki bunki né undirbunki tómir
        self.assertFalse(Leikmadur.UB[2],Leikmadur.B[2])
        Leikmadur.B[0].pop()
        # Bæði bunki og undirbunki tómir
        self.assertFalse(Leikmadur.UB[0], Leikmadur.B[0])
    
    def test_Reglur_LeyfilegHreyfing(self):
        pass
        
    def test_Reglur_Sigra(self):
        pass
    
    def test_Reglur_Tapa(self):
        pass
    
    def test_Prompt_Stada(self):
        print ""
        Leikmadur=Spilari()
        Stada(Leikmadur)
    
    def test_Prompt_Byrjun(self):
        print ""
        Byrjun()
    
    
    """
    #Gömul próf (úr pöndukaplinum)
    def test_Hendi_Halda(self):
        S=Stokkur.Spilastokkur()
        H=Stokkur.Hendi()
        x=[S[0].sort,S[0].gildi]
        H.Halda(S.Taka())
        self.assertEqual(x[0],H[0].sort)
        self.assertEqual(x[1],H[0].gildi)
    
    def test_Hendi_Henda(self):
        S=Stokkur.Spilastokkur()
        H=Stokkur.Hendi()
        x=[S[0].sort,S[0].gildi]
        H.Halda(S.Taka())
        H.Halda(S.Taka())
        fyrir=len(H)
        H.Henda(len(H)-1)
        eftir=len(H)
        self.assertEqual(fyrir-eftir,1)
    
    def test_Kapall_Draga(self):
        S=Stokkur.Spilastokkur()
        H=Stokkur.Hendi()
        S_fyrir=len(S)
        H_fyrir=len(H)
        Kapall.Draga(S,H)
        S_eftir=len(S)
        H_eftir=len(H)
        self.assertEqual(S_fyrir-S_eftir,1)
        self.assertEqual(H_fyrir-H_eftir,-1)
        #Athuga hvort að spilið sem ég var að draga sé enn í stokknum
        for i in range(len(S)):
            flag=True
            flag=flag and (S[i].sort==H[0].sort and S[i].gildi==H[0].gildi)
        self.assertFalse(flag)
    
    def test_Kapall_Kasta(self):
        listi=[]
        for i in ["H","S","T","L"]:
            for j in range(1,14):
                listi.append(Stokkur.Spil(i,j,""))
        
        #Prófa að kasta 2 spilum
        H=Stokkur.Hendi()
        for i in range(4):
            H.Halda(listi[i])
        H_fyrir=len(H)
        Kapall.Kasta(listi,H,2)
        H_eftir=len(H)
        self.assertEqual(H_fyrir-H_eftir,2)
        self.assertEqual(H[0].sort,"H")
        self.assertEqual(H[0].gildi,1)
        self.assertEqual(H[1].sort,"H")
        self.assertEqual(H[1].gildi,4)
        
        #Prófa að kasta 4 spilum
        H.Halda(listi[4])
        H.Halda(listi[13])
        H_fyrir=len(H)
        Kapall.Kasta(listi,H,4)
        H_eftir=len(H)
        self.assertEqual(H_fyrir-H_eftir,4)
        self.assertEqual(len(H),0)
    
    def test_Kapall_Skipta(self):
        S=Stokkur.Spilastokkur()
        H=Stokkur.Hendi()
        for i in range(6):
            H.Halda(S[i])
        #"Tæmi" stokkinn, því skipta á bara að virka þegar stokkurinn er tómur
        S=[]
        x=[H[0].sort,H[0].gildi]
        y=[H[2].sort,H[2].gildi]
        Kapall.Skipta(S,H)
        self.assertEqual(H[len(H)-1].sort,x[0])
        self.assertEqual(H[len(H)-1].gildi,x[1])
        self.assertEqual(H[1].sort,y[0])
        self.assertEqual(H[1].gildi,y[1])
    """
if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)