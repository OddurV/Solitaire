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
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE,
                 name="MyFrame"):
        super(MyFrame, self).__init__(parent, id, title, pos, size, style, name)

        self.panel = wx.Panel(self)

        path = os.path.abspath("./Myndir/icon.jpeg")
        icon = wx.Icon(path, wx.BITMAP_TYPE_JPEG)
        self.SetIcon(icon)

        #Menu bar fyrir options
        menu_bar = wx.MenuBar()

        #Options fyrir adgerdir i leik
        options = wx.Menu()

        menu_bar.Append(options, "Options")
        options.Append(wx.NewId(), "New Game")
        options.Append(wx.NewId(), "Highscore")
        options.Append(wx.NewId(), "Rules")
        self.SetMenuBar(menu_bar)

    
if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
