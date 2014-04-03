import wx
import os


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Solitaire")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


class MyFrame(wx.Frame):    
    def __init__(self, parent, id=wx.ID_ANY, title="",
                 pos=wx.DefaultPosition, size=(1280, 720),
                 style=wx.DEFAULT_FRAME_STYLE,
                 name="MyFrame"):
        super(MyFrame, self).__init__(parent, id, title, pos, size, style, name)

        self.panel = wx.Panel(self)

        
        btn = "./Myndir/h1.jpg"
        image1 = wx.Image(btn, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.btn=wx.BitmapButton(self.panel, id=-1, bitmap=image1,
            pos=(10, 348), size = (image1.GetWidth()+5, image1.GetHeight()+5))
        self.btn.Bind(wx.EVT_LEFT_DOWN, self.B1Click)
        
       
        
        self.delta = ((0, 0))
        self.Bind(wx.EVT_LEFT_DOWN, self.onDown)
        self.btn.Bind(wx.EVT_LEFT_DOWN, self.onButton)
        self.btn.Bind(wx.EVT_MOTION, self.onMove)
        self.btn.Bind(wx.EVT_LEFT_UP, self.onRelease)
        self.btn.Bind(wx.EVT_LEAVE_WINDOW, self.onLeave)
        self.panel.Bind(wx.EVT_KEY_UP, self.upPressed) 
        
        self.panel.SetFocus()
        
        #Icon fyrir main glugga
        path = os.path.abspath("./Myndir/icon.jpeg")
        icon = wx.Icon(path, wx.BITMAP_TYPE_JPEG)
        self.SetIcon(icon)
        
        #Menu bar fyrir options
        menu_bar = wx.MenuBar()

        #drop down options fyrir adgerdir i leik
        options = wx.Menu()

        #adgerdir i leik
        menu_bar.Append(options, "Options")
        options.Append(wx.NewId(), "New Game")
        options.Append(wx.NewId(), "Highscore")
        options.Append(wx.NewId(), "Rules")
        self.SetMenuBar(menu_bar)
        
        #Add sizer
        panelSizer = wx.BoxSizer(wx.VERTICAL) 
        panelSizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizerAndFit(panelSizer)


    def B1Click(self,event):
        self.SetTitle("B1 clicked")

    def onDown(self, event):
        event.Skip()

    def onButton(self, event):
        print "buttpressstart"
        self.btn.CaptureMouse()
        x, y = self.ScreenToClient(self.btn.ClientToScreen(event.GetPosition()))
        originx, originy = self.btn.GetPosition()
        dx = x - originx
        dy = y - originy
        self.delta = ((dx, dy))
        print "buttpressdone"
        

    def onMove(self, event):
        if event.Dragging():
            print "dragstart"
            x, y = self.ScreenToClient(self.btn.ClientToScreen(event.GetPosition()))
            fp = (x-self.delta[0], y-self.delta[1])
            self.btn.Move(fp)

    def onRelease(self, event):
        print "onreleasestart"
        if self.btn.HasCapture():
            print "onreleasestarthascaptures"
            self.btn.ReleaseMouse()
            print "onreleasereleasemousedone"
            
    def onLeave(self, event):
        print "onleavestart"
        if self.btn.HasCapture():
            print "onleavestarthascapture"
            self.btn.ReleaseMouse()
            print "onleavereleasemousedone"
    def upPressed(self, event):
        print "uppressed"
                
if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
