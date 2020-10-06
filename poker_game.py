# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:49:47 2020

@author: dhruv
"""

import pylab
import random
import copy
import collections


class Deal(object):
    def __init__(self):
        self.CardDeck={}
        self.ranks=("2","3","4","5","6","7","8","9",'10','11','12','13',"14")
        self.suits=('Heart','Diamond','Club',"Spade")
        self.ComCard={}
        i=2
        for rank in self.ranks:
            for suit in self.suits:
                self.CardDeck[rank+suit]=[]
                self.CardDeck[rank+suit].append(i)
                self.CardDeck[rank+suit].append(suit)
            i +=1
        self.listx=list(self.CardDeck.keys())


    def DealFlopCards(self):
        for i in range(3):
            random_card=random.choice(self.listx)
            self.ComCard[random_card]=self.CardDeck[random_card]
            self.listx.remove(random_card)

    def DealHoles(self,Players):
        for i in range(len(Players)):
            PlayerCards={}
            for a in range(2):
                rand_card=random.choice(self.listx)
                PlayerCards[rand_card]=self.CardDeck[rand_card]
                self.listx.remove(rand_card)
            Players[i].GameCard(PlayerCards)
    def DealFourth(self):
        random_card=random.choice(self.listx)
        self.ComCard[random_card]=self.CardDeck[random_card]
        self.listx.remove(random_card)


    def DealFifth(self):
        random_card=random.choice(self.listx)
        self.ComCard[random_card]=self.CardDeck[random_card]
        self.listx.remove(random_card)


    def DeckReset(self):
        self.listx=list(self.CardDeck.keys())
        self.ComCard={}

    def GetComCard(self):
        return self.ComCard


#####test####
p=Deal().GetComCard()
print(p)
##test#####



class Player():
    def __init__(self,name,cash):
        self.name=name
        self.Cards={}
        self.Hand_order=0
        self.MaxVal=0
        self.kicker=0
        self.cash=cash
        self.fold_status=False

    def GameCard(self,Hole_card):
        self.Cards=Hole_card

    def getCards(self):
        return self.Cards

    def setHand_order(self,hand_order):
        self.Hand_order=hand_order

    def setMaxVal(self,MaxVal):
        self.MaxVal=MaxVal

    def setKicker(self,kicker):
        self.kicker=kicker

    def getHand_order(self):
        return self.Hand_order

    def getMaxVal(self):
        return self.MaxVal

    def getKicker(self):
        return self.kicker

    def getName(self):
        return self.name

    def getCash(self):
        return self.cash

    def addCash(self,amount):
        self.cash+=amount

    def removeCash(self,amount):
        self.cash-=amount

    def Call(self,call):
        self.removeCash(call)

    def Fold(self):
        self.fold_status=True

    def Raise(self,raise):
        raise_amount=int(raise*self.cash)
        self.removeCash(raise_amount)

        return raise_amount

    def Action(self,action):
