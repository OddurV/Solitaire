#!/usr/bin/python

#PyGermanWhist 0.91b
#
#(C) 2010-2012 Jason Benjamin
#Email: hexusnexus@gmail.com
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#  
#Note:  Forgive me for not commenting a lot of this file. I assume a 
#       good understanding of wxPython as well as basic geometrics.  

import wx
from whist import *

class CardPlacement:
    
    """A data class for position and size data."""
    
    def __init__(self, clientSize, cardsize=(71,96), humanAmount=13, computerAmount=13):
        """Initialize card placement data."""
        self.clientSize = clientSize
        self.cardsize = cardsize
        self.amountCardscomputer = computerAmount
        self.amountCardshuman = humanAmount
        self.overlapSpace = 20
        #here follows some uneccessarily long lines:
        self.computerbeginPos = (self.clientSize[0]/2 - (self.overlapSpace*(self.amountCardscomputer-1)-self.cardsize[0]), 15)
        self.humanbeginPos = (self.clientSize[0]/2 - (self.overlapSpace*(self.amountCardshuman-1)-self.cardsize[0]), self.clientSize[1] - 15 - self.cardsize[1])

class Tally(wx.Dialog):

    """The tally dialog.

    Methods:

        - OnClose(evt)
    """
    
    def __init__(self, parent, computer, human, title):
        """Initialize and create tally dialog."""
        wx.Dialog.__init__(self, parent=parent, title=title, size=(250, 200))
        
        self.panel = wx.Panel(self)        
        id=wx.NewId()
        
        self.list1 = wx.ListCtrl(self,id,style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.Ok = wx.Button(self, wx.ID_OK)
        self.Ok.Bind(wx.EVT_BUTTON, self.OnClose)
        
        self.list1.SetMinSize((100, 80))
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.list1, 1, wx.EXPAND, 0)
        
        sizer_1.Add(self.Ok, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.SetSizer(sizer_1)
        
        self.list1.InsertColumn(0,"Computer")
        self.list1.InsertColumn(1,"You")

        pos = self.list1.InsertStringItem(0, str(computer))
        #add values in the other columns on the same row
        self.list1.SetStringItem(pos,1, str(human))
    def OnClose(self, evt):
        """Call on close event."""
        self.Destroy()
        
class CardGraphics(wx.Panel):

    """The graphics widget.

    Methods:

        - OnSize(evt)
        - updatePos(player, cards)
        - Click(evt)
        - offClick(evt)
        - Motion(evt)
        - InitBuffer()
        - DrawEverything()
        - OnPaint(evt)
        - DrawCards(dc, humanCards, computerCards)
        - DrawHumanCards(dc, humanCards)
        - DrawComputerCards(dc, computerCards)
        - DrawDeck(dc, pos)
    """
    
    def __init__(self, parent, id):
        """Initialize graphics widget (using wx.Panel)."""
        wx.Panel.__init__(self, parent, id)
        self.parent = parent
        self.human = None
        self.computer = None
        self.backimagepath = "cards/b1fv.gif"
        self.backimage = wx.Image(self.backimagepath).ConvertToBitmap()
        self.stippleimage = wx.Image("green020.jpg").ConvertToBitmap()
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.Click)
        self.Bind(wx.EVT_LEFT_UP, self.offClick)
        self.Bind(wx.EVT_MOTION, self.Motion)
        self.dealt = False
        self.I = False
        self.play_pos = {}
    def OnSize(self, evt):
        """Call on size event."""
        self.size = self.GetClientSize()
        self.data = CardPlacement(self.size)
        if not self.play_pos:
            self.play_pos['human'] = self.size[1]*.4
            self.play_pos['computer'] = self.size[1]*.4
        idc = wx.MemoryDC(self.stippleimage)
        self.stipplebackground = wx.MemoryDC()
        self.stipplebackground.SelectObject(wx.EmptyBitmap(*self.size))
        x = y = 0
        while True:
            self.stipplebackground.Blit(x, y, self.stippleimage.GetWidth(), self.stippleimage.GetHeight(), idc, 0, 0)
            x = x + self.stippleimage.GetWidth()
            if x  > self.size[0]:
                x = 0
                y = y + self.stippleimage.GetHeight()
                if y > self.size[1]:
                    break
        self.InitBuffer()
        dc = wx.MemoryDC()
        dc.SelectObject(self.buffer)
        dc.Blit(0, 0, self.size[0], self.size[1], self.stipplebackground, 0, 0)
        if self.human and self.computer:
            self.updatePos("human", self.human.hand.cards)
            self.updatePos("computer", self.computer.hand.cards)
            self.DrawEverything()
        #if there were a fast and easy way to stretch blit then
        #I would make the window resizable and resize everything in this handler
    def updatePos(self, player, cards):
        """Update the position of the cards, factoring in size ratios."""
        if not self.parent.deck.deck:
            handlength = 13 - len(cards)  #not literally the hand length
            lastcard = 1
        else:
            handlength = 0
            lastcard = 1
        #more long lines:
        if player == "human":
            for i in range(len(cards)):
                if cards[i].position[1] != self.play_pos[player]:
                    cards[i].position = (self.data.humanbeginPos[0] + i*self.data.overlapSpace + (handlength*self.data.overlapSpace)/2 + (lastcard*self.data.overlapSpace)/2, self.data.humanbeginPos[1])
                else:
                    if not self.parent.first:
                        cards[i].position = ((self.size[0] + self.data.cardsize[0])/2.5 + 40, self.size[1]*.4)
                    else:
                        cards[i].position = ((self.size[0] + self.data.cardsize[0])/2.5, self.size[1]*.4)
                    self.play_pos[player] = cards[i].position[1]
        elif player == "computer":
            for i in range(len(cards)):
                if cards[i].position[1] != self.play_pos[player]:
                    cards[i].position = (self.data.computerbeginPos[0] + i*self.data.overlapSpace + (handlength*self.data.overlapSpace)/2 + (lastcard*self.data.overlapSpace)/2, self.data.computerbeginPos[1])
                else:
                    if self.parent.first:
                        cards[i].position = ((self.size[0] + self.data.cardsize[0])/2.5 + 40, self.size[1]*.4)
                    else:
                        cards[i].position = ((self.size[0] + self.data.cardsize[0])/2.5, self.size[1]*.4)
                    self.play_pos[player] = cards[i].position[1]
    def Click(self, evt):
        """Call on click event."""
        if self.parent.turn != None and self.dealt:
            cards = self.human.hand.cards
            cardslength = len(self.human.hand.cards)
            x = evt.GetX()
            y = evt.GetY()
            for i in range(cardslength):
                #this uneccessarily long if statement checks for your card hotspots
                if cards[i].position[1] < y < cards[i].position[1] + self.data.cardsize[1] and cards[i].position[0] < x < cards[i].position[0]+self.data.overlapSpace or (i==len(cards)-1 and cards[-1].position[0] < x < cards[-1].position[0] + self.data.cardsize[0]):
                    if self.parent.turn == "human" and not self.parent.Hcard:
                        if not self.parent.first:
                            available = self.human.hand.inSuit(self.parent.lead.suit)
                            if not available:
                                available = self.human.hand.notInSuit(self.parent.lead.suit)
                                #mark these if it seems the player has run out of a suit
                                if cards[i].suit == 0 and not self.parent.computer.none_suit_h[0]:
                                    self.parent.computer.none_suit_h[0] = True
                                elif cards[i].suit == 1 and not self.parent.computer.none_suit_h[1]:
                                    self.parent.computer.none_suit_h[1] = True
                                elif cards[i].suit == 2 and not self.parent.computer.none_suit_h[2]:
                                    self.parent.computer.none_suit_h[2] = True
                                elif cards[i].suit == 3 and not self.parent.computer.none_suit_h[3]:
                                    self.parent.computer.none_suit_h[3] = True
                            if cards[i] in available:
                                self.parent.storeHposition = cards[i].position
                                cards[i].position = ((self.size[0] + self.data.cardsize[0])/2.5 + 40, self.size[1]*.4)
                                self.play_pos['human'] = self.size[1]*.4
                                self.parent.lead = self.parent.Hcard = cards[i]
                                if self.parent.Hcard.suit == self.parent.trump.suit:
                                    self.parent.trumpPlayed = True
                                self.parent.timer.Start(1000)
                            else:
                                cards[i].inverted = True
                                self.I = True
                                self.parent.statusbar.SetStatusText("Please follow suit")
                        else:
                            if cards[i].suit != self.parent.trump.suit or (self.parent.trumpPlayed or not self.human.hand.notInSuit(self.parent.trump.suit)):
                                self.parent.storeHposition = cards[i].position
                                cards[i].position = ((self.size[0] + self.data.cardsize[0])/2.5, self.size[1]*.4)
                                self.play_pos['human'] = self.size[1]*.4
                                self.parent.lead = self.parent.Hcard = cards[i]
                                if self.parent.Hcard.suit == self.parent.trump.suit:
                                    self.parent.trumpPlayed = True
                                self.parent.turn = "computer"
                                self.parent.timer.Start(1000)
                            else:
                                self.parent.statusbar.SetStatusText("Trump has not been played yet")
                                cards[i].inverted = True
                                self.I = True
                                self.parent.timer.Start(1000)
                        self.DrawEverything()
                    else:
                        self.parent.statusbar.SetStatusText("Sorry, it's the computer's turn")
                    break

    def offClick(self, evt):
        """Call on release of mouse button."""
        if self.human:
            cards = self.human.hand.cards
            cardslength = len(self.human.hand.cards)
            x = evt.GetX()
            y = evt.GetY()
            if self.I == True:
                for i in range(cardslength):
                    if cards[i].inverted:
                        cards[i].inverted = False
                        self.I = False
                self.DrawEverything()
    def Motion(self, evt):
        """Call on mouse move."""
        if self.human:
            cards = self.human.hand.cards
            cardslength = len(self.human.hand.cards)
            x = evt.GetX()
            y = evt.GetY()
            hitTest = False
            if self.I == True:
                for i in range(cardslength):                    
                    if cards[i].inverted and ((i!=len(cards)-1 and not cards[i].position[0] < x < cards[i].position[0]+self.data.overlapSpace) or (i==len(cards)-1 and not cards[-1].position[0] < x < cards[-1].position[0] + self.data.cardsize[0]) or not self.data.humanbeginPos[1] < y < self.data.humanbeginPos[1] + self.data.cardsize[1]):
                        cards[i].inverted = False
                        self.I = False
                self.DrawEverything()
    def InitBuffer(self):
        """Initialize bitmap buffer."""
        self.buffer = wx.EmptyBitmap(*self.size)
    def DrawEverything(self):
        """Draw all graphics."""
        dc = wx.MemoryDC()
        dc.SelectObject(self.buffer)
        dc.Blit(0, 0, self.size[0], self.size[1], self.stipplebackground, 0, 0)
        self.DrawCards(dc, self.human.hand.cards, self.computer.hand.cards)
        self.DrawDeck(dc)
        wx.ClientDC(self).Blit(0, 0, self.size[0], self.size[1], dc, 0, 0)
    def OnPaint(self, evt):
        """Call on paint event."""
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.buffer,0,0)
    def DrawCards(self, dc, humanCards, computerCards):
        """Draw the cards onto the device context."""
        if self.parent.first:
            self.DrawHumanCards(dc, humanCards)
            self.DrawComputerCards(dc, computerCards)
        else:
            self.DrawComputerCards(dc, computerCards)
            self.DrawHumanCards(dc, humanCards)
    def DrawHumanCards(self, dc, humanCards):
        """Draw the person's cards."""
        if humanCards:
            for c in humanCards:
                cardImage = wx.Image("cards/"+Card.SUIT[c.suit][0]+Card.RANK[c.rank][0]+".gif").ConvertToBitmap()
                if c.inverted:
                    idc = wx.MemoryDC(cardImage)
                    dc.Blit(c.position[0], c.position[1], cardImage.GetWidth(), cardImage.GetHeight(), idc, 0, 0, wx.SRC_INVERT)
                else:
                    dc.DrawBitmap(cardImage, c.position[0], c.position[1])
    def DrawComputerCards(self, dc, computerCards):
        """Draw the computer's cards."""
        if computerCards:
            for c in computerCards:
                if not c.showFace:
                    dc.DrawBitmap(self.backimage, c.position[0], c.position[1])
                else:
                    cardImage = wx.Image("cards/"+Card.SUIT[c.suit][0]+Card.RANK[c.rank][0]+".gif").ConvertToBitmap()
                    dc.DrawBitmap(cardImage, c.position[0], c.position[1])
    def DrawDeck(self, dc, top=None):
        """Draw the deck."""
        if self.parent.deck.deck:
            if top:
                self.top = top
            startdeck = (self.size[0]*.24, self.size[1]*.4)
            face = wx.Image("cards/"+Card.SUIT[self.parent.top.suit][0]+Card.RANK[self.parent.top.rank][0]+".gif").ConvertToBitmap()
            if len(self.parent.deck.deck) >= 6:
                for x in range(5):
                    dc.DrawBitmap(self.backimage, startdeck[0]+x*2, startdeck[1])
                dc.DrawBitmap(face, startdeck[0]+5*2, startdeck[1])
            else:
                for x in range(len(self.parent.deck.deck)):
                    dc.DrawBitmap(self.backimage, startdeck[0]+x*2, startdeck[1])
                dc.DrawBitmap(face, startdeck[0]+len(self.parent.deck.deck)*2, startdeck[1])

class MainWindow(wx.Frame):

    """The main game window.

    Methods:

        - changeBlue(evt)
        - changeRed(evt)
        - humanFirst(evt)
        - computerFirst(evt)
        - onAboutDlg(event)
        - gamesWon(event)
        - init_variables()
        - init_game()
        - newGame(evt)
        - OnExit(evt)
        - OnTimer(evt)
        - deal()
    """
    
    def __init__(self, face):
        """Initialize and create the game window.  Initialize game variables."""
        wx.Frame.__init__(self, None, title="German Whist", size=(640,480), style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        icon = wx.Icon("germanwhist.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        self.face = face
        #total games won
        self.computer_won = self.you_won = 0
        self.size = self.GetClientSizeTuple()
        self.statusbar = self.CreateStatusBar(style=0)
        self.comRadio = wx.RadioButton
        self.humRadio = wx.RadioButton
        self.menuBar = wx.MenuBar()
        menu = wx.Menu()
        menu2 = wx.Menu()
        menu3 = wx.Menu()
        new = menu.Append(wx.ID_ANY, "&New Game", "Start a new game")
        submenu = wx.Menu()
        submenu.AppendRadioItem(1, "You", "You are the first in a new game")
        submenu.AppendRadioItem(2, "Computer", "Computer is first in a new game")
        menu.AppendMenu(wx.ID_ANY, 'Starting', submenu)
        menu2.Append(wx.ID_ANY, "Card Deck", "Select below the card deck color")
        menu2.AppendSeparator()
        menu2.AppendRadioItem(3, "Blue")
        menu2.AppendRadioItem(4, "Red")
        _exit = menu.Append(wx.ID_ANY, "E&xit", "Exit the game")
        about = menu3.Append(wx.ID_ANY, "&About", "About this game")
        games_won = menu3.Append(wx.ID_ANY, "Games &won", "Score")
        self.menuBar.Append(menu, "&File")
        self.menuBar.Append(menu2, "&Options")
        self.menuBar.Append(menu3, "&Help")
        self.SetMenuBar(self.menuBar)
        self.Bind(wx.EVT_MENU, self.OnExit, _exit)
        self.Bind(wx.EVT_MENU, self.newGame, new)
        self.Bind(wx.EVT_MENU, self.onAboutDlg, about)
        self.Bind(wx.EVT_MENU, self.gamesWon, games_won)
        self.Bind(wx.EVT_MENU, self.humanFirst, id=1)
        self.Bind(wx.EVT_MENU, self.computerFirst, id=2)
        self.Bind(wx.EVT_MENU, self.changeBlue, id=3)
        self.Bind(wx.EVT_MENU, self.changeRed, id=4)
        self.selected = "human"
        self.init_variables()
        self.Draw = CardGraphics(self, wx.ID_ANY)
        menu.Bind(wx.EVT_MENU_OPEN, self.timerOff)
        menu.Bind(wx.EVT_MENU_CLOSE, self.timerOn)
        menu2.Bind(wx.EVT_MENU_OPEN, self.timerOff)
        menu2.Bind(wx.EVT_MENU_CLOSE, self.timerOn)
        menu3.Bind(wx.EVT_MENU_OPEN, self.timerOff)
        menu3.Bind(wx.EVT_MENU_CLOSE, self.timerOn)
        self.info = wx.AboutDialogInfo()
        self.info.Name = "PyGermanWhist"
        self.info.Version = "0.92b"
        self.info.Copyright = "(C) 2010-2012 Jason Benjamin"
        self.info.Description = "PyGermanWhist, a German Whist card game written in Python."
        self.info.WebSite = ("http://www.pagat.com/whist/german_whist.html", "Click here for standard rules")
        self.info.Developers = ["Jason Benjamin"]
        self.info.License = "See file entitled 'license.txt'"
        self.statusbar.SetStatusText("To begin, select 'New Game' from the File menu")
    def timerOn(self, evt):
        if self.turn:
            self.timer.Start(1000)
    def timerOff(self, evt):
        if self.turn:
            self.timer.Stop()
    def changeBlue(self, evt):
        """Call if card deck color is changed to blue."""
        if self.Draw.backimagepath == "cards/b2fv.gif":
            self.Draw.backimagepath = "cards/b1fv.gif"
            self.Draw.backimage = wx.Image(self.Draw.backimagepath).ConvertToBitmap()
            if self.turn != None:
                self.Draw.DrawEverything()
    def changeRed(self, evt):
        """Call if card deck color is changed to red."""
        if self.Draw.backimagepath == "cards/b1fv.gif":
            self.Draw.backimagepath = "cards/b2fv.gif"
            self.Draw.backimage = wx.Image(self.Draw.backimagepath).ConvertToBitmap()
            if self.turn != None:
                self.Draw.DrawEverything()
    def humanFirst(self, evt):
        """Call on the selection of 'You' as the first player."""
        if self.selected == "human":
            return
        else:
            self.selected = "human"
            if self.turn != None:
                dlg = wx.MessageDialog(self, "You selected a different player to begin. Start new game?", "New Game?", wx.YES_NO | wx.CENTRE | wx.NO_DEFAULT)
                if dlg.ShowModal() == wx.ID_YES:
                    self.init_variables()
                    self.init_game()
                dlg.Destroy()
    def computerFirst(self, evt):
        """Call on the selection of 'Computer' as the first player."""
        if self.selected == "computer":
            return
        else:
            self.selected = "computer"
            if self.turn != None:
                dlg = wx.MessageDialog(self, "You selected a different player to begin. Start new game?", "New Game?", wx.YES_NO | wx.CENTRE | wx.NO_DEFAULT)
                if dlg.ShowModal() == wx.ID_YES:
                    self.init_variables()
                    self.init_game()
                dlg.Destroy()
    def onAboutDlg(self, event):
        """Show the about box dialog."""
        wx.AboutBox(self.info)
    def gamesWon(self, event):
        """Show the tally dialog."""
        #here create a dialog with a table showing the scores
        tly = Tally(self, self.computer_won, self.you_won, title="Score")
        tly.ShowModal()
        tly.Destroy()
    def init_variables(self):
        """Initialize or reinitialize key variables."""
        self.trumpPlayed = False
        self.lead = None
        self.Hcard = None
        self.Ccard = None
        self.Hwin = None
        self.Cwin = None
        self.storeHposition = None
        self.storeCposition = None
        self.turn = None
        self.deck = Deck()
        self.human = Player(self.trumpPlayed)
        self.computer = ComputerPlayer(self.trumpPlayed)
    def init_game(self):
        """Begin the game."""
        self.turn = self.selected
        if self.turn == "human":
            self.first = True
        else:
            self.first = False
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(1000)
        self.deal()
        self.Draw.dealt = True
        self.trump = self.top = self.deck.turnTop()
        self.computer.hand.organize(self.trump)
        self.human.hand.organize(self.trump)
        self.Draw.updatePos("human", self.human.hand.cards)
        self.Draw.updatePos("computer", self.computer.hand.cards)
        self.Draw.computer = self.computer
        self.Draw.human = self.human
        self.Draw.DrawEverything()
    def newGame(self, evt):
        """Call on selection of new game."""
        self.init_variables()
        self.init_game()
    def OnExit(self, evt):
        """Call on exit event."""
        self.Close()
    def OnTimer(self, evt):
        """Call on timer event.  Handle animation and status bar."""
        if self.turn == "human":
            #here place an if statement to enact an alternate status if in second hand
            if not self.top:
                if self.human.tricks != 1:
                    tricktext = " tricks won"
                else:
                    tricktext = " trick won"
                self.statusbar.SetStatusText("Your turn: " + str(self.human.tricks) + tricktext)
            else:
                self.statusbar.SetStatusText("Your turn")
        else:
            self.statusbar.SetStatusText("")
        if self.turn != "human" and not self.Ccard:
            self.Ccard = self.computer.selectCard(self.lead, self.trump, self.top, self.first)
            cards = self.computer.hand.cards
            for c in cards:
                if c.name == self.Ccard.name:
                    c.showFace = True
                    if self.first:
                        self.storeCposition = c.position
                        c.position = ((self.Draw.size[0] + self.Draw.data.cardsize[0])/2.5 + 40, self.Draw.size[1]*.4)
                        break
                    else:
                        self.lead = self.Ccard
                        self.storeCposition = c.position
                        c.position = ((self.Draw.size[0] + self.Draw.data.cardsize[0])/2.5, self.Draw.size[1]*.4)
                        self.turn = "human"
                        break
                    self.Draw.play_pos['computer'] = self.Draw.size[1]*.4
            self.computer.hand.organize(self.trump)
            self.Draw.updatePos("computer", self.computer.hand.cards)
            self.Draw.DrawEverything()
        elif self.Ccard and self.Hcard:
            self.lead = None
            if self.Hcard.suit == self.Ccard.suit:
                if self.Ccard.rank > self.Hcard.rank:
                    self.Cwin = True
                    self.Hwin = False
                else:
                    self.Cwin = False
                    self.Hwin = True
            elif not self.first:
                if self.Hcard.suit != self.trump.suit:
                    self.Cwin = True
                    self.Hwin = False
                else:
                    self.Cwin = False
                    self.Hwin = True
            elif self.first:
                if self.Ccard.suit != self.trump.suit:
                    self.Cwin = False
                    self.Hwin = True
                else:
                    self.Cwin = True
                    self.Hwin = False
            if self.Cwin:
                self.first = False
                self.turn = "computer"
                if not self.top:
                    self.computer.wonTrick()
                else:
                    self.computer.receiveCard(self.top)
                    self.computer.hand.cards[-1].position = self.storeCposition
                    self.human.receiveCard(self.deck.draw())
                    self.human.hand.cards[-1].position = self.storeHposition

            elif self.Hwin:
                self.first = True
                self.turn = "human"
                if not self.top:
                    self.human.wonTrick()
                    if self.human.tricks != 1:
                        tricktext = " tricks won"
                    else:
                        tricktext = " trick won"
                    if self.statusbar.GetStatusText():
                        self.statusbar.SetStatusText("Your turn: " + str(self.human.tricks) + tricktext)
                else:
                    self.human.receiveCard(self.top)
                    self.human.hand.cards[-1].position = self.storeHposition
                    #if receiving a certain suit you didn't have before, remember
                    if self.top.suit == 0 and self.computer.none_suit_h[0]:
                        self.computer.none_suit_h[0] = False
                    elif self.top.suit == 1 and self.computer.none_suit_h[1]:
                        self.computer.none_suit_h[1] = False
                    elif self.top.suit == 2 and self.computer.none_suit_h[2]:
                        self.computer.none_suit_h[2] = False
                    elif self.top.suit == 3 and self.computer.none_suit_h[3]:
                        self.computer.none_suit_h[3] = False
                        
                    self.computer.receiveCard(self.deck.draw())
                    self.computer.hand.cards[-1].position = self.storeCposition

            self.computer.hand.cards[-1].showFace = self.face #Should be False
            self.computer.hand.remove(self.Ccard.name)
            self.human.hand.remove(self.Hcard.name)
            if self.Ccard.suit == self.trump.suit:
                self.computer.n_played_trumps += 1
            if self.Hcard.suit == self.trump.suit:
                self.computer.n_played_trumps += 1
            self.Cwin = None
            self.Hwin = None
            self.Ccard = None
            self.Hcard = None
            self.human.hand.organize(self.trump)
            self.computer.hand.organize(self.trump)
            self.Draw.updatePos("human", self.human.hand.cards)
            self.Draw.updatePos("computer", self.computer.hand.cards)
            if self.deck.deck:
                self.top = self.deck.turnTop()
            elif not self.deck.deck and self.top:
                self.top = None
                self.statusbar.SetStatusText("Playing for the trick")
            self.Draw.DrawEverything()
            
        if not self.human.hand.cards and not self.computer.hand.cards:
            self.statusbar.SetStatusText("Game completed")
            self.timer.Stop()
            self.turn = None
            if self.human.tricks > self.computer.tricks:
                wx.MessageBox("You win.", "Game outcome", wx.OK)
                #add to the number of games *you* have won
                self.you_won += 1
            elif self.computer.tricks > self.human.tricks:
                wx.MessageBox("Computer wins.", "Game outcome", wx.OK)
                #add to the number of games the computer has won
                self.computer_won += 1
    def deal(self):
        """Deal the cards."""
        self.deck.shuffle()
        for i in range(13):
            self.human.receiveCard(self.deck.draw())
            self.Draw.data.amountCardshuman = len(self.human.hand.cards)
            self.human.hand.cards[-1].position = (self.Draw.data.humanbeginPos[0] + i*self.Draw.data.overlapSpace, self.Draw.data.humanbeginPos[1])
            self.computer.receiveCard(self.deck.draw())
            self.Draw.data.amountCardscomputer = len(self.computer.hand.cards)
            self.computer.hand.cards[-1].position = (self.Draw.data.computerbeginPos[0] + i*self.Draw.data.overlapSpace, self.Draw.data.computerbeginPos[1])
            self.computer.hand.cards[-1].showFace = self.face  #Should be False

if __name__ == "__main__":
    from optparse import OptionParser
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("--show-faces", action="store_true", dest="face", default=False, help="Show all the card faces while playing")
    (options, args) = parser.parse_args()
    app = wx.App()
    frame = MainWindow(options.face)
    frame.Show()
    app.MainLoop()
