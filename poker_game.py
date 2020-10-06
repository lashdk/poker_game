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
    def getFoldStat(self):
        return self.fold_status

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
    def ResetHand(self):
        self.Cards={}
        self.Hand_order=0
        self.MaxVal=0
        self.kicker=0
        self.fold_status=False


def BestHand(player_card):

    self.cards=copy.deepcopy(player_card)
    self.values=[]
    self.suits=[]
    for card in self.cards:
        temp_list=self.cards[card]
        temp_list=list(temp_list)
        self.values.append(temp_list[0])
        self.suits.append(temp_list[1])


    def getValue(self):
        return self.values



    def getSuit(self):
        return self.suits

    def RoyalFlush(self):
        rank=copy.deepcopy(self.values)
        colour=copy.deepcopy(self.suits)
        heart=[]
        diamond=[]
        spade=[]
        club=[]
        royal_straight="1011121314"
        hand_order=0
        MaxVal=0
        kicker=0



        for a in range(len(self.values)):
            if colour[a]=="Heart":
                heart.append(rank[a])
            elif colour[a]=="Diamond":
                diamond.append(rank[a])
            elif colour[a]=="Spade":
                spade.append(rank[a])
            else:
                club.append(rank[a])

        if len(heart)>=5:
            max_colour=copy.deepcopy(heart)
        elif len(diamond)>=5:
            max_colour=copy.deepcopy(diamond)

        elif len(spade)>=5:
            max_colour=copy.deepcopy(spade)
        elif len(club)>=5:
            max_colour=copy.deepcopy(club)
        else:
            return (0,0,0)


        max_colour.sort()
        result_straight=""
        for a in max_colour:
            result_straight +=str(a)

        if royal_straight in result_straight:
            hand_order =10


        return (hand_order,MaxVal,kicker)



    def CheckRoyalFlush(self):
        rank=copy.deepcopy(self.values)
        colour=copy.deepcopy(self.suits)
        heart=[]
        diamond=[]
        spade=[]
        club=[]
        royal_straight="1011121314"
        hand_order=0
        MaxVal=0
        kicker=0



        for a in range(len(self.values)):
            if colour[a]=="Heart":
                heart.append(rank[a])
            elif colour[a]=="Diamond":
                diamond.append(rank[a])
            elif colour[a]=="Spade":
                spade.append(rank[a])
            else:
                club.append(rank[a])

        if len(heart)>=5:
            max_colour=copy.deepcopy(heart)
        elif len(diamond)>=5:
            max_colour=copy.deepcopy(diamond)

        elif len(spade)>=5:
            max_colour=copy.deepcopy(spade)
        elif len(club)>=5:
            max_colour=copy.deepcopy(club)
        else:
            return False


        max_colour.sort()
        result_straight=""
        for a in max_colour:
            result_straight +=str(a)

        if royal_straight in result_straight:
            hand_order=10
            return True




        return False








    def StraightFlush(self):
        rank=copy.deepcopy(self.values)
        colour=copy.deepcopy(self.suits)
        heart=[]
        diamond=[]
        spade=[]
        club=[]
        normal_straight=[]
        normal_straight.append("234514")

        for i in range(2,14):
            result=""
            if i+5<15:

                for j in range(5):
                    result +=str(i+j)
                normal_straight.append(result)




        hand_order=0
        MaxVal=0
        kicker=0



        for a in range(len(self.values)):
            if colour[a]=="Heart":
                heart.append(rank[a])
            elif colour[a]=="Diamond":
                diamond.append(rank[a])
            elif colour[a]=="Spade":
                spade.append(rank[a])
            else:
                club.append(rank[a])

        if len(heart)>=5:
            max_colour=copy.deepcopy(heart)
        elif len(diamond)>=5:
            max_colour=copy.deepcopy(diamond)

        elif len(spade)>=5:
            max_colour=copy.deepcopy(spade)
        elif len(club)>=5:
            max_colour=copy.deepcopy(club)
        else:
            return (0,0,0)


        max_colour.sort()
        result_straight=""
        for a in max_colour:
            result_straight +=str(a)


        for b in normal_straight:
            if b in result_straight:
                hand_order=9
                last_digit=int(b[-1])
                if last_digit in (6,7,8,9):
                    MaxVal=last_digit
                else:
                    last_digit +=10
                    MaxVal=last_digit






        return (hand_order,MaxVal,kicker)



    def CheckStraightFlush(self):
        rank=copy.deepcopy(self.values)
        colour=copy.deepcopy(self.suits)
        heart=[]
        diamond=[]
        spade=[]
        club=[]
        normal_straight=[]
        normal_straight.append("234514")

        for i in range(2,14):
            result=""
            if i+5<15:

                for j in range(5):
                    result +=str(i+j)
                normal_straight.append(result)




        hand_order=0
        MaxVal=0
        kicker=0



        for a in range(len(self.values)):
            if colour[a]=="Heart":
                heart.append(rank[a])
            elif colour[a]=="Diamond":
                diamond.append(rank[a])
            elif colour[a]=="Spade":
                spade.append(rank[a])
            else:
                club.append(rank[a])

        if len(heart)>=5:
            max_colour=copy.deepcopy(heart)
        elif len(diamond)>=5:
            max_colour=copy.deepcopy(diamond)

        elif len(spade)>=5:
            max_colour=copy.deepcopy(spade)
        elif len(club)>=5:
            max_colour=copy.deepcopy(club)
        else:
            return False


        max_colour.sort()
        result_straight=""
        for a in max_colour:
            result_straight +=str(a)


        for b in normal_straight:
            if b in result_straight:
                hand_order=9
                last_digit=int(b[-1])
                return True
                if last_digit in (6,7,8,9):
                    MaxVal=last_digit
                else:
                    last_digit +=10
                    MaxVal=last_digit






        return False


    def FourKind(self):
        rank=copy.deepcopy(self.values)
        max_times=0
        card_value=0
        hand_order=0
        MaxVal=0
        kicker=0
        for a in rank:
            times=rank.count(a)
            if times>=max_times:
                max_times=times
                card_value=a

        if max_times==4:
            hand_order=8
            MaxVal=card_value
        else:
            return (0,0,0)

        for i in range(4):
            rank.remove(MaxVal)

        rank.sort()
        kicker=rank[-1]



        return (hand_order,MaxVal,kicker)



    def CheckFourKind(self):
        rank=copy.deepcopy(self.values)
        max_times=0
        card_value=0
        hand_order=0
        MaxVal=0
        kicker=0
        for a in rank:
            times=rank.count(a)
            if times>=max_times:
                max_times=times
                card_value=a

        if max_times==4:
            hand_order=8
            MaxVal=card_value
            return True
        else:
            return False








    def FullHouse(self):
        rank=copy.deepcopy(self.values)
        max_times=0
        card_value=0
        hand_order=0
        MaxVal=0
        pair=0
        kicker=0
        count=collections.Counter(rank)

        for key in count:
            if count[key]>max_times:
                max_times=count[key]
                card_value=key
            elif count[key]==max_times:
                if key>card_value:
                    card_value=key







        if max_times==3:


            for key in count:
                if key!=card_value:
                    if count[key]>=2 and key>pair:
                        pair=key
                        hand_order=7
                        MaxVal=card_value
                        kicker=pair


        else:
            return(0,0,0)


        return (hand_order,MaxVal,kicker)


    def CheckFullHouse(self):
        rank=copy.deepcopy(self.values)
        max_times=0
        card_value=0
        hand_order=0
        MaxVal=0
        pair=0
        kicker=0
        count=collections.Counter(rank)

        for key in count:
            if count[key]>max_times:
                max_times=count[key]
                card_value=key
            elif count[key]==max_times:
                if key>card_value:
                    card_value=key

        if max_times==3:


            for key in count:
                if key!=card_value:
                    if count[key]>=2 and key>pair:
                        pair=key
                        hand_order=7
                        MaxVal=card_value
                        kicker=pair
                        return True

        return False











    def Flush(self):
        rank=copy.deepcopy(self.values)
        colour=copy.deepcopy(self.suits)
        heart=[]
        diamond=[]
        spade=[]
        club=[]

        hand_order=0
        MaxVal=0
        kicker=0



        for a in range(len(self.values)):
            if colour[a]=="Heart":
                heart.append(rank[a])
            elif colour[a]=="Diamond":
                diamond.append(rank[a])
            elif colour[a]=="Spade":
                spade.append(rank[a])
            else:
                club.append(rank[a])

        if len(heart)>=5:
            max_colour=copy.deepcopy(heart)
        elif len(diamond)>=5:
            max_colour=copy.deepcopy(diamond)

        elif len(spade)>=5:
            max_colour=copy.deepcopy(spade)
        elif len(club)>=5:
            max_colour=copy.deepcopy(club)
        else:
            return (0,0,0)


        max_colour.sort()
        hand_order=6
        MaxVal=max_colour[-1]





        return (hand_order,MaxVal,kicker)


    def CheckFlush(self):
        rank=copy.deepcopy(self.values)
        colour=copy.deepcopy(self.suits)
        heart=[]
        diamond=[]
        spade=[]
        club=[]

        hand_order=0
        MaxVal=0
        kicker=0



        for a in range(len(self.values)):
            if colour[a]=="Heart":
                heart.append(rank[a])
            elif colour[a]=="Diamond":
                diamond.append(rank[a])
            elif colour[a]=="Spade":
                spade.append(rank[a])
            else:
                club.append(rank[a])

        if len(heart)>=5:
            max_colour=copy.deepcopy(heart)
        elif len(diamond)>=5:
            max_colour=copy.deepcopy(diamond)

        elif len(spade)>=5:
            max_colour=copy.deepcopy(spade)
        elif len(club)>=5:
            max_colour=copy.deepcopy(club)
        else:
            return False


        max_colour.sort()
        hand_order=6
        MaxVal=max_colour[-1]





        return True



    def Straight(self):
        rank=copy.deepcopy(self.values)
        hand_order=0
        kicker=0
        MaxVal=0
        straight=[]
        straight.append("234514")
        for i in range(1,10):
            result=""
            if i+5<15:

                for j in range(1,6):
                    result +=str(i+j)
                straight.append(result)




        unique_rank=[]
        for i in rank:
            if i not in unique_rank:
                unique_rank.append(i)

        unique_rank.sort()
        result=""
        for a in unique_rank:
            result +=str(a)


        for b in straight:
            if b in result:
                hand_order=5
                last_digit=int(b[-1])
                if last_digit in (6,7,8,9):
                    MaxVal=last_digit
                else:
                    last_digit +=10
                    MaxVal=last_digit



        return (hand_order,MaxVal,kicker)

    def CheckStraight(self):
        rank=copy.deepcopy(self.values)
        hand_order=0
        kicker=0
        MaxVal=0
        straight=[]
        straight.append("234514")
        for i in range(1,10):
            result=""
            if i+5<15:

                for j in range(1,6):
                    result +=str(i+j)
                straight.append(result)




        unique_rank=[]
        for i in rank:
            if i not in unique_rank:
                unique_rank.append(i)

        unique_rank.sort()
        result=""
        for a in unique_rank:
            result +=str(a)


        for b in straight:
            if b in result:
                hand_order=5
                last_digit=int(b[-1])
                if last_digit in (6,7,8,9):
                    MaxVal=last_digit
                else:
                    last_digit +=10
                    MaxVal=last_digit

                return True


        return False



    def ThreeKind(self):
        rank=copy.deepcopy(self.values)
        max_times=0
        card_value=0
        hand_order=0
        MaxVal=0
        kicker1=0
        kicker2=0
        kicker=0
        count=collections.Counter(rank)

        for key in count:
            if count[key]>max_times:
                max_times=count[key]
                card_value=key
            elif count[key]==max_times:
                if key>card_value:
                    card_value=key

        if max_times==3:
            for a in range(3):
                rank.remove(card_value)

            rank.sort()
            hand_order=4
            MaxVal=card_value
            kicker1=rank[-1]
            kicker2=rank[-2]
            kicker=int(str(kicker1)+str(kicker2))



        return (hand_order,MaxVal,kicker)

    def CheckThreeKind(self):
        rank=copy.deepcopy(self.values)
        max_times=0
        card_value=0
        hand_order=0
        MaxVal=0
        kicker=0
        count=collections.Counter(rank)

        for key in count:
            if count[key]>max_times:
                max_times=count[key]
                card_value=key
            elif count[key]==max_times:
                if key>card_value:
                    card_value=key

        if max_times==3:

            for a in range(3):
                rank.remove(card_value)

            rank.sort()
            hand_order=4
            MaxVal=card_value
            kicker=rank[-1]
            return True
        else:
            return False





    def TwoPair(self):
        rank=copy.deepcopy(self.values)
        count=collections.Counter(rank)
        hand_order=0
        MaxVal=0
        kicker=0
        kicker1=0
        kicker2=0
        pairs=[]

        for key in count:
            if count[key]==2:
                pairs.append(key)


        if len(pairs)>=2:

            pairs.sort()
            pairs=pairs[-2:]
            MaxVal=max(pairs)
            kicker1=pairs[0]
            hand_order=3

            for a in pairs:
                for b in range(2):
                    rank.remove(a)

            kicker2=max(rank)
            kicker=int(str(kicker1)+str(kicker2))
        else:
            return(0,0,0)




        return (hand_order,MaxVal,kicker)



    def CheckTwoPair(self):
        rank=copy.deepcopy(self.values)
        count=collections.Counter(rank)

        hand_order=0
        MaxVal=0
        kicker1=0
        kicker2=0
        pairs=[]

        for key in count:
            if count[key]==2:
                pairs.append(key)


        if len(pairs)>=2:

            return True
            pairs.sort()
            pairs=pairs[-2:]
            MaxVal=max(pairs)
            kicker1=pairs[0]
            hand_order=3

            for a in pairs:
                for b in range(2):
                    rank.remove(a)

            kicker2=max(rank)




        return False



    def OnePair(self):
        rank=copy.deepcopy(self.values)
        count=collections.Counter(rank)
        hand_order=0
        MaxVal=0
        kicker=0
        kicker1=0
        kicker2=0
        kicker3=0
        pairs=[]

        for key in count:
            if count[key]==2:
                pairs.append(key)

        if len(pairs)==1:

            pairs.sort()
            pairs=pairs[-1:]
            MaxVal=max(pairs)

            hand_order=2

            for a in pairs:
                for b in range(2):
                    rank.remove(a)
            rank.sort()
            kicker1=rank[-1]
            kicker2=rank[-2]
            kicker3=rank[-3]
            kicker=int(str(kicker1)+str(kicker2)+str(kicker3))




        return (hand_order,MaxVal,kicker)



    def CheckOnePair(self):
        rank=copy.deepcopy(self.values)
        count=collections.Counter(rank)
        hand_order=0
        MaxVal=0
        kicker1=0
        kicker2=0
        kicker3=0
        pairs=[]

        for key in count:
            if count[key]==2:
                pairs.append(key)

        if len(pairs)==1:
            return True
            pairs.sort()
            pairs=pairs[-1:]
            MaxVal=max(pairs)

            hand_order=2

            for a in pairs:
                for b in range(2):
                    rank.remove(a)
            rank.sort()
            kicker1=rank[-1]
            kicker2=rank[-2]
            kicker3=rank[-3]




        return False


    def HighCard(self):
        rank=copy.deepcopy(self.values)
        hand_order=1
        rank.sort()
        kicker=0
        MaxVal=rank[-1]
        kicker1=rank[-2]
        kicker2=rank[-3]
        kicker3=rank[-4]
        kicker4=rank[-5]
        kicker=int(str(kicker1)+str(kicker2)+str(kicker3)+str(kicker4))




        return (hand_order,MaxVal,kicker)
