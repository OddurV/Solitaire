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
                 pos=wx.DefaultPosition, size=(500, 250),
                 style=wx.DEFAULT_FRAME_STYLE,
                 name="MyFrame"):
        super(MyFrame, self).__init__(parent, id, title, pos, size, style, name)

        self.panel = wx.Panel(self)

        self.btn=wx.Button(parent=self, id=-1, label="Go")
        
        self.delta = ((0, 0))
        self.Bind(wx.EVT_LEFT_DOWN, self.onDown)
        self.btn.Bind(wx.EVT_LEFT_DOWN, self.onButton)
        self.btn.Bind(wx.EVT_MOTION, self.onMove)
        self.btn.Bind(wx.EVT_LEFT_UP, self.onRelease)
        
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


    def onDown(self, event):
        event.Skip()

    def onButton(self, event):
        self.btn.CaptureMouse()
        self.btn.SetSize(self.btn.GetDefaultSize())
        x, y = self.ScreenToClient(self.btn.ClientToScreen(event.GetPosition()))
        originx, originy = self.btn.GetPosition()
        dx = x - originx
        dy = y - originy
        self.delta = ((dx, dy))

    def onMove(self, event):
        if event.Dragging():
            x, y = self.ScreenToClient(self.btn.ClientToScreen(event.GetPosition()))
            fp = (x-self.delta[0], y-self.delta[1])
            self.btn.Move(fp)

    def onRelease(self, event):
        if self.btn.HasCapture():
            self.btn.ReleaseMouse()

            
if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
