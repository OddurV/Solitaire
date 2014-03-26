#This file is part of PyGermanWhist (GermanWhist.py)
#
#PyGermanWhist is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random

class Card:
    
    """Class to represent a playing card."""
    
    RANK = ["2", "3", "4", "5",
            "6", "7", "8", "9",
            "ten", "jack", "queen",
            "king", "ace"]
    SUIT = ["spades","clubs","diamonds","hearts"]
    def __init__(self, rank, suit):
        """Initialize card data."""
        self.rank = rank
        self.suit = suit
        self.name = "%s of %s" % (Card.RANK[self.rank],
                                  Card.SUIT[self.suit])
        self.position = ()
        self.inverted = False
        self.showFace = True
    def __repr__(self):
        """Return 'official' string representation."""
        return "'" + self.name + "'"
    def __str__(self):
        """Return 'informal' string representation."""
        return self.name

class Deck:
    
    """Class to represent the playing deck.

    Methods:
    
        - turnTop()
        - shuffle()
        - draw()
    """
    
    def __init__(self):
        """Initialize the deck."""
        self.deck = []
        #assign every card (not including jokers) by rank and suit
        for i in range(52):
            self.deck.append(Card(i % 13, i / 13))
    def turnTop(self):
        """Draw a card."""
        return self.draw()
    def shuffle(self):
        """Shuffle the deck."""
        random.seed()
        random.shuffle(self.deck)
    def draw(self):
        """Take the top card off the deck and return it."""
        return self.deck.pop(0)
    def __len__(self):
        """For len().  Return the size of the deck."""
        return len(self.deck)

class Hand:

    """Class to represent a player's hand.

    Methods:

        - pull(pos)
        - remove(name)
        - pullName(name)
        - put(crd)
        - inSuit(suit)
        - notInSuit(suit)
        - sortSuitRank()
        - sortRankSuit()
        - amountrank(x)
        - cardsbyRank(trump)
        - cardsbyAmount(trump)
        - trumpCards(trump)
        - organize(trump)
    """
    
    def __init__(self):
        """Initialize the hand."""
        self.cards = []
    def pull(self, pos=0):
        """Return a card at the position."""
        return self.cards[pos]
    def remove(self, name):
        """Remove a card from the deck based on its name."""
        for p, crd in enumerate(self.cards):
            if crd.name == name:
                del self.cards[p]
                return
    def pullName(self, name):
        """Return a card based on its name."""
        pulled = None
        for p, crd in enumerate(self.cards):
            if crd.name == name:
                pulled = self.pull(p)  #note this won't delete the card
                break
        return pulled
    def put(self, crd):
        """Add the card to the hand."""
        self.cards.append(crd)
    def inSuit(self, suit):
        """Return a list of cards in the hand in this suit."""
        return [crd for crd in self.cards if crd.suit == suit]
    def notInSuit(self, suit):
        """Return a list of cards in the hand not in this suit."""
        return [crd for crd in self.cards if crd.suit != suit]
    def sortSuitRank(self):
        """Sort cards by suit first, then by rank."""
        self.cards.sort(key = lambda x: (x.suit, x.rank))
    def sortRankSuit(self):
        """Sort cards by rank first, then by suit."""
        self.cards.sort(key = lambda x: (x.rank, x.suit))
    def amountrank(self, x):
        """Key function to sort a list of cards by amount."""
        a = 0
        for crd in self.cards:
            if crd.suit == x.suit:
                a += 1
        #the resulting 'a' variable is the amount of the suit x is
        return (a, x.rank)
    def cardsbyRank(self, trump):
        """Return a list of non-trump cards sorted by rank."""
        ranklist = self.notInSuit(trump.suit)
        ranklist.sort(key = lambda x: (x.rank, x.suit))
        return ranklist
    def cardsbyAmount(self, trump):
        """Return a list of non-trump cards sorted by amount."""
        amountlist = self.notInSuit(trump.suit)
        amountlist.sort(key = self.amountrank)  #couldn't figure out lambda
        return amountlist
    def trumpCards(self, trump):
        """Return a sorted list of trump cards."""
        trumplist = self.inSuit(trump.suit)
        trumplist.sort(key = lambda x: x.rank)
        return trumplist
    def organize(self, trump):
        """Sort cards SuitRank, with trumps last."""
        self.sortSuitRank()
        trumps = [c for c in self.cards if c.suit == trump.suit]
        nontrumps = [c for c in self.cards if c.suit != trump.suit]
        self.cards = nontrumps + trumps
    def __len__(self):
        """For len().  Return the size of the hand."""
        return len(self.cards)


class Player:
    
    """Class to implement player.

    Methods:

        - receiveCard(crd)
        - wonTrick()
        - organize(trump)
    """
    
    def __init__(self, trumpPlayed):
        """Initialize player."""
        self.hand = Hand()
        self.tricks = 0
        self.trumpPlayed = trumpPlayed
    def receiveCard(self, crd):
        """Receive a card."""
        self.hand.put(crd)
    def wonTrick(self):
        """Increase number of tricks player has won."""
        self.tricks += 1
    def organize(self, trump):
        """Organize player's cards."""
        self.hand.organize(trump)

class ComputerPlayer(Player):

    """Class to implement computer player.

    Methods:

        - selectCard(lead, trump, top, turn)
    """
    
    def __init__(self, trumpPlayed):
        """Initialize the computer player."""
        #inherits __init__ methods from Player
        Player.__init__(self, trumpPlayed)
        self.lead = self.trump = self.top = None
        #human doesn't have the 'True' suits
        self.none_suit_h = [False, False, False, False]
        self.n_played_trumps = 0
    def __must_trump__(self):
        """Returns True if it is advantageous to play a trump card."""
        flag = False
        trump_amount = 0
        for crd in self.hand.cards:
            if crd.suit == crd.suit:
                trump_amount += 1
                continue
            if crd.rank >= 10:
                flag = True
                break
        #if having no high cards and having less trumps than opponent
        if not flag and trump_amount < (13 - trump_amount -self.n_played_trumps) and not self.top:
            return True
        else:
            return False
    def __play_trump__(self):
        """Returns a trump card in most cases.  Otherwise returns another function."""
        only_trumps = self.hand.trumpCards(self.trump)
        
        trump_len = len(only_trumps)

        #must have trumps to use this function
        if not trump_len:
            return
            
        if not self.top:
            if self.turn:
                if self.lead.suit != self.trump.suit:
                    return only_trumps[0]
                elif self.lead.suit == self.trump.suit:
                    for trmp in only_trumps:
                        if trmp.rank > self.lead.rank:
                            return trmp
            else:
                #an arbitrary rank-based method on how to pick trumps
                if only_trumps[-1].rank > 8:
                    upperlimit = 6
                elif only_trumps[-1].rank > 5:
                    upperlimit = 3
                else:
                    upperlimit = 13  #skips the next for statement
                if upperlimit < 13:
                    for trmp in only_trumps:
                        if trmp.rank < upperlimit:
                            continue
                        return trmp
                #the fall-through default
                return only_trumps[-1]
        else:
            #these are for the first hand
            if self.turn and only_trumps[0].rank < self.top.rank and self.top.suit == self.trump.suit:
                return only_trumps[0]
            elif not (len(self.hand.cards) - trump_len):  #no choice
                return only_trumps[0]
            else:
                return self.__comp_lose__()
    def __comp_win__(self):
        """Returns a winning card if possible."""
        trump_len = len(self.hand.inSuit(self.trump.suit))
        if not self.turn:
            if self.__must_trump__() and self.trumpPlayed and trump_len:
                return self.__play_trump__()
            ranksorted = self.hand.cardsbyRank(self.trump)
            
            if ranksorted:
                #try highest to lowest
                for crd in reversed(ranksorted):
                    #check that the card is possessed by opponent and not trump
                    if not self.none_suit_h[crd.suit] and crd.suit != self.trump.suit:
                        return crd
                #these are if the previous falls through:
                if trump_len and self.trumpPlayed:
                    return self.__play_trump__()
                else:
                    return self.__comp_lose__()
            #no non-trumps
            else:
                return self.__play_trump__()
        else:
            if self.hand.inSuit(self.lead.suit):
                ret_card = None
                #try to play the lowest card that still wins
                for crd in self.hand.cards:
                    if crd.rank > self.lead.rank and crd.suit == self.lead.suit:
                        ret_card = crd
                        break
                if not ret_card:
                    #no dice? lose
                    return self.__comp_lose__()
                else:
                    return ret_card
            else:
                #don't possess that suit
                if trump_len:
                    return self.__play_trump__()
                else:
                    return self.__comp_lose__()
    def __comp_lose__(self):
        """Returns a losing card in most cases."""
        if not self.turn:
            ranksorted = self.hand.cardsbyRank(self.trump)
            if self.top:
                #play a slightly higher card (not too high) if a non-trump ace
                #slight strategy change from .91b (used to be == 12 instead of > 10)
                if self.top.rank > 10 and self.top.suit != self.trump.suit:
                    if len(ranksorted) >= 3:
                        rng_start = 2
                    else:
                        rng_start = len(ranksorted) - 1
                    for i in range(rng_start, 0, -1):
                        if ranksorted[i].rank > 3:
                            continue
                        elif not self.none_suit_h[ranksorted[i].suit]:
                            return ranksorted[i]
            for crd in ranksorted:
                if not self.none_suit_h[crd.suit]:
                    return crd
            return ranksorted[0]
        else:
            if self.hand.inSuit(self.lead.suit):
                ret_card = None
                #just play the lowest possible in the suit
                for crd in self.hand.cards:
                    if crd.suit != self.lead.suit:
                        continue
                    if crd.rank < self.lead.rank:
                        ret_card = crd
                        break
                if ret_card:
                    return ret_card
                else:
                    #but may have to play a higher card
                    return self.__force_high__()
            else:
                trump_len = len(self.hand.inSuit(self.trump.suit))
                #have only trump cards
                if not self.hand.notInSuit(self.trump.suit) or (not self.top and trump_len):
                    return self.__play_trump__()
                
                ranksorted = self.hand.cardsbyRank(self.trump)
                amountsorted = self.hand.cardsbyAmount(self.trump)

                #try to play a card based on amount more than rank
                #these could be _higher_ cards, but not too high
                if len(amountsorted) >= 3:
                    rng_start = 2
                else:
                    rng_start = len(amountsorted) - 1
                for i in range(rng_start, 0, -1):
                    if amountsorted[i].rank < 8:
                        return amountsorted[i]
                #default to lowest rank
                return ranksorted[0]
    def __force_high__(self):
        """Returns the lowest card possible in the same suit as the competitor."""
        same_suit = []

        #get a list of all cards in the lead suit
        for crd in self.hand.cards:
            if crd.suit == self.lead.suit:
                same_suit.append(crd)
        return same_suit[0]
    def selectCard(self, lead, trump, top, turn):
        """Returns the best card to play."""
        self.lead = lead
        self.trump = trump
        self.top = top
        self.turn = turn
        choice = None
        if not self.top:
            choice = self.__comp_win__()
        else:
            if self.top.suit == self.trump.suit:
                choice = self.__comp_win__()
            else:
                choice = self.__comp_lose__()  #will not necessarily lose
        return choice
