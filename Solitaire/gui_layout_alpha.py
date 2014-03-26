# -*- coding: utf-8 -*-
import wx

class MyFrame(wx.Frame):
    """make a frame, inherits wx.Frame, add a panel and button"""
    def __init__(self,size):
        # create a frame, no parent, default to wxID_ANY
        wx.Frame.__init__(self, None, wx.ID_ANY, 'wxBitmapButton',
            pos=(300, 150), size=(1280, 720))
        # panel needed to display button correctly
        self.panel1 = wx.Panel(self, -1)
        self.size = size
        super(MyFrame, self).__init__(size)
        '''
        #Gerir Bakgrunn
        self.stippleimage = wx.Image("backgroundPlaceholder.jpg").ConvertToBitmap()
        idc = wx.MemoryDC(self.stippleimage)
        self.stipplebackground = wx.MemoryDC()
        self.stipplebackground.SelectObject(wx.EmptyBitmap(*self.size))
        x = y = 0
        while True:
            self.stipplebackground.Blit(x, y, self.stippleimage.GetWidth(), self.stippleimage.GetHeight(), idc, 0, 0)
            x = x + self.stippleimage.GetWidth()
            if x  > self.size[0]:
                x = 0
                y = y + Frame.stippleimage.GetHeight()
                if y > self.size[1]:
                    break
        self.InitBuffer()
        dc = wx.MemoryDC()
        dc.SelectObject(self.buffer)
        ###
        #Skilgreinir stadsettningu takka og tengir thad ad klikkað se a tha vid event
        '''
        B1 = "./Myndir/h1.jpg"
        image1 = wx.Image(B1, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button1 = wx.BitmapButton(self.panel1, id=-1, bitmap=image1,
            pos=(10, 348), size = (image1.GetWidth()+5, image1.GetHeight()+5))
        self.button1.Bind(wx.EVT_BUTTON, self.B1Click)
        
        B2 = "./Myndir/h2.jpg"
        image2 = wx.Image(B2, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button2 = wx.BitmapButton(self.panel1, id=-1, bitmap=image2,
            pos=(154, 348), size = (image2.GetWidth()+5, image2.GetHeight()+5))
        self.button2.Bind(wx.EVT_BUTTON, self.B2Click)

        B3 = "./Myndir/h3.jpg"
        image3 = wx.Image(B3, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button3 = wx.BitmapButton(self.panel1, id=-1, bitmap=image3,
            pos=(298, 348), size = (image3.GetWidth()+5, image3.GetHeight()+5))
        self.button3.Bind(wx.EVT_BUTTON, self.B3Click)

        B4 = "./Myndir/h4.jpg"
        image4 = wx.Image(B4, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button4 = wx.BitmapButton(self.panel1, id=-1, bitmap=image4,
            pos=(442, 348), size = (image4.GetWidth()+5, image4.GetHeight()+5))
        self.button4.Bind(wx.EVT_BUTTON, self.B4Click)

        B5 = "./Myndir/h5.jpg"
        image5 = wx.Image(B5, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button5 = wx.BitmapButton(self.panel1, id=-1, bitmap=image5,
            pos=(586, 348), size = (image5.GetWidth()+5, image5.GetHeight()+5))
        self.button5.Bind(wx.EVT_BUTTON, self.B5Click)

        B6 = "./Myndir/h6.jpg"
        image6 = wx.Image(B6, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button6 = wx.BitmapButton(self.panel1, id=-1, bitmap=image6,
            pos=(730, 348), size = (image6.GetWidth()+5, image6.GetHeight()+5))
        self.button6.Bind(wx.EVT_BUTTON, self.B6Click)

        B7 = "./Myndir/h7.jpg"
        image7 = wx.Image(B7, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button7 = wx.BitmapButton(self.panel1, id=-1, bitmap=image7,
            pos=(874, 348), size = (image7.GetWidth()+5, image7.GetHeight()+5))
        self.button7.Bind(wx.EVT_BUTTON, self.B7Click)

        S = "./Myndir/h8.jpg"
        image8 = wx.Image(S, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button1 = wx.BitmapButton(self.panel1, id=-1, bitmap=image8,
            pos=(10, 20), size = (image1.GetWidth()+5, image1.GetHeight()+5))
        self.button1.Bind(wx.EVT_BUTTON, self.SClick)

        E = "./Myndir/h9.jpg"
        image9 = wx.Image(E, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button2 = wx.BitmapButton(self.panel1, id=-1, bitmap=image9,
            pos=(154, 20), size = (image2.GetWidth()+5, image2.GetHeight()+5))
        self.button2.Bind(wx.EVT_BUTTON, self.EClick)

        G1 = "./Myndir/h10.jpg"
        image10 = wx.Image(G1, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button3 = wx.BitmapButton(self.panel1, id=-1, bitmap=image10,
            pos=(442, 20), size = (image3.GetWidth()+5, image3.GetHeight()+5))
        self.button3.Bind(wx.EVT_BUTTON, self.G1Click)
        
        G2 = "./Myndir/h11.jpg"
        image11 = wx.Image(G2, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button3 = wx.BitmapButton(self.panel1, id=-1, bitmap=image11,
            pos=(586, 20), size = (image3.GetWidth()+5, image3.GetHeight()+5))
        self.button3.Bind(wx.EVT_BUTTON, self.G2Click)

        G3 = "./Myndir/h12.jpg"
        image12 = wx.Image(G3, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button3 = wx.BitmapButton(self.panel1, id=-1, bitmap=image12,
            pos=(730, 20), size = (image3.GetWidth()+5, image3.GetHeight()+5))
        self.button3.Bind(wx.EVT_BUTTON, self.G3Click)

        G4 = "./Myndir/h13.jpg"
        image13 = wx.Image(G4, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button3 = wx.BitmapButton(self.panel1, id=-1, bitmap=image13,
            pos=(874, 20), size = (image3.GetWidth()+5, image3.GetHeight()+5))
        self.button3.Bind(wx.EVT_BUTTON, self.G4Click)

            # show the frame
        self.Show(True)

    #Placeholder fyrir events thegar klikkad er a takkana

    def B1Click(self,event):
        self.SetTitle("B1 clicked")

    def B2Click(self,event):
        self.SetTitle("B2 clicked")

    def B3Click(self,event):
        self.SetTitle("B3 clicked")

    def B4Click(self,event):
        self.SetTitle("B4 clicked")

    def B5Click(self,event):
        self.SetTitle("B5 clicked")

    def B6Click(self,event):
        self.SetTitle("B6 clicked")
 
    def B7Click(self,event):
        self.SetTitle("B7 clicked")
 
    def SClick(self,event):
        self.SetTitle("S clicked")

    def EClick(self,event):
        self.SetTitle("E clicked")

    def G1Click(self,event):
        self.SetTitle("G1 clicked")

    def G2Click(self,event):
        self.SetTitle("G2 clicked")

    def G3Click(self,event):
        self.SetTitle("G3 clicked")
 
    def G4Click(self,event):
        self.SetTitle("G4 clicked")


application = wx.PySimpleApp()
# call class MyFrame
window = MyFrame()
# start the event loop
application.MainLoop()


