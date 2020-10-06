# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 02:16:01 2020

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
        self.listx=[]
    
    
    
    def MakeDeck(self):
        i=2
        for rank in self.ranks:
            for suit in self.suits:
                self.CardDeck[rank+suit]=[]
                self.CardDeck[rank+suit].append(i)
                self.CardDeck[rank+suit].append(suit)
            i +=1
        
        
        
        
        
    
    def DealComCards(self):
        
        self.listx=self.CardDeck.keys()
        self.listx=list(self.listx)
        
        for i in range(5):
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
            Players[i].GameCard(PlayerCards,self.ComCard)
            
            
            
            
            
            
            
            
class Player():
    def __init__(self,name):
        self.name=name
        self.Cards={}
        self.Hand_order=0
        self.MaxVal=0
        self.kicker=0
        
    def GameCard(self,Hole_card,Community_card):
        self.Cards={**Hole_card,**Community_card}
    
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


    
    
    










class BestHand():
    def __init__(self,player_card):
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
        
        
        
    
    
    
            
            
            
        
        
        
class PokerHand():
    def __init__(self):
        self.players=[]
        self.game=Deal()
        self.best_hand_order=0
        self.best_kicker=0
        self.best_MaxVal=0
        
        self.winner=[]
        
    def AddPlayer(self,name):
        self.players.append(Player(name))
        
    def Game(self):
        self.game.MakeDeck()
        self.game.DealComCards()
        self.game.DealHoles(self.players)
        
        for play in self.players:
            cards=play.getCards()
            
            
            
            
            p=BestHand(cards)
            
            if p.CheckRoyalFlush():
                hand_order,MaxVal,kicker=p.RoyalFlush()
            elif p.CheckStraightFlush():
                hand_order,MaxVal,kicker=p.StraightFlush()
            elif p.CheckFourKind():
                hand_order,MaxVal,kicker=p.FourKind()
            elif p.CheckFullHouse():
                hand_order,MaxVal,kicker=p.FullHouse()
            elif p.CheckFlush():
                hand_order,MaxVal,kicker=p.Flush()
            elif p.CheckStraight():
                hand_order,MaxVal,kicker=p.Straight()
            elif p.CheckThreeKind():
                hand_order,MaxVal,kicker=p.ThreeKind()
            elif p.CheckTwoPair():
                hand_order,MaxVal,kicker=p.TwoPair()
            elif p.CheckOnePair():
                hand_order,MaxVal,kicker=p.OnePair()
            else:
                hand_order,MaxVal,kicker=p.HighCard()
            
            
            play.setHand_order(hand_order)
            play.setMaxVal(MaxVal)
            play.setKicker(kicker)
            
        
        
        for play in self.players:
            
            player_hand_order=play.getHand_order()
            player_kicker=play.getKicker()
            player_MaxVal=play.getMaxVal()
            
            
            
            if player_hand_order > self.best_hand_order:
                self.best_hand_order=player_hand_order
                self.best_MaxVal=player_MaxVal
                self.best_kicker=player_kicker
                
            
            if player_hand_order==self.best_hand_order:
                if player_MaxVal > self.best_MaxVal:
                    self.best_hand_order=player_hand_order
                    self.best_MaxVal=player_MaxVal
                    self.best_kicker=player_kicker
                if player_MaxVal==self.best_MaxVal:
                    if player_kicker>=self.best_kicker:
                        self.best_hand_order=player_hand_order
                        self.best_MaxVal=player_MaxVal
                        self.best_kicker=player_kicker
        
        
    def ShowDown(self):
        for play in self.players:
            player_name=play.getName()
            player_hand_order=play.getHand_order()
            player_kicker=play.getKicker()
            player_MaxVal=play.getMaxVal()
            
            
            if player_hand_order==self.best_hand_order and player_MaxVal==self.best_MaxVal and player_kicker==self.best_kicker:
                self.winner.append(play)
                
        
    def PrintResult(self):
        print("----------Result---------")
        WinningHands={1:"HighCard",2:"OnePair",3:"TwoPair",4:"Three of a Kind",5:"Straight",6:"Flush",7:"FullHouse",8:"Four of a kind",9:"StraightFlush",10:"RoyalFlush"}
        CardValue={2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:'Nine',10:'Ten',11:"Jack",12:"Queen",13:"King",14:"Ace"}
        for play in self.winner:
            print(play.getCards())
            player_name=play.getName()
            player_hand_order=play.getHand_order()
            player_kicker=play.getKicker()
            player_MaxVal=play.getMaxVal
            player_card=play.getCards()
            
            print(player_name+" won the game with "+WinningHands[player_hand_order])
            
            
    def getHand_order(self):
        return self.best_hand_order
    
    
    def getWinner(self):
        return self.winner
    
    def getPlayer(self):
        return self.players
    
    
    









def PokerSimulation(numHands,toPrint=False):
  
    numHighcard=0
    numOnepair=0
    numTwopair=0
    numThreekind=0
    numStraight=0
    numFlush=0
    numFullhouse=0
    numFourkind=0
    numStraightflush=0
    numRoyalflush=0
    a=[]
    
    
    for b in range(numHands):
        p=PokerHand()
        p.AddPlayer("Player 1")
        p.AddPlayer("Player 2")
        p.AddPlayer("Player 3")
        p.AddPlayer("Player 4")
        p.AddPlayer("Player 5")
        p.Game()
        p.ShowDown()
        
        hand_order=p.getHand_order()
        
        
        
        if hand_order==1:
            numHighcard +=1
            
        elif hand_order==2:
            numOnepair +=1
            
        elif hand_order==3:
            numTwopair +=1
            
        elif hand_order==4:
            numThreekind +=1
            
        elif hand_order==5:
            numStraight +=1
            
        elif hand_order==6:
            numFlush +=1
            
        elif hand_order==7:
            numFullhouse +=1
            
        elif hand_order==8:
            numFourkind +=1
            
        elif hand_order==9:
            numStraightflush +=1
            
        elif hand_order==10:
            numRoyalflush +=1
            
            
            
            
    
    if toPrint:
        print("highcards ",numHighcard)
        print("One pair",numOnepair)
        print("Two Pair ",numTwopair)
        print("Three of a kind",numThreekind)
        print("Straight",numStraight)
        print("Flush",numFlush)
        print("Fullhouse",numFullhouse)
        print("Four of a Kind",numFourkind)
        print("straight Flush",numStraightflush)
        print("Royal Flush",numRoyalflush)
    
    
    a.append(numHighcard)
    a.append(numOnepair)
    a.append(numTwopair)
    a.append(numThreekind)
    a.append(numStraight)
    a.append(numFlush)
    a.append(numFullhouse)
    a.append(numFourkind)
    a.append(numStraightflush)
    a.append(numRoyalflush)
        
        
        
        
        
        
    return a








def PokerTrials(numHands,numTrials,toPrint=False):
    Highcard=[]
    Onepair=[]
    TwoPair=[]
    Threekind=[]
    Straight=[]
    Flush=[]
    Fullhouse=[]
    Fourkind=[]
    Straightflush=[]
    Royalflush=[]
    simu_list=[]
    
    for b in range(numTrials):
        
        simu_list=PokerSimulation(numHands)
        Highcard.append(simu_list[0])
        Onepair.append(simu_list[1])
        TwoPair.append(simu_list[2])
        Threekind.append(simu_list[3])
        Straight.append(simu_list[4])
        Flush.append(simu_list[5])
        Fullhouse.append(simu_list[6])
        Fourkind.append(simu_list[7])
        Straightflush.append(simu_list[8])
        Royalflush.append(simu_list[9])
        
        
    
    
    
    meanHighcard=(sum(Highcard)/numTrials)
    meanOnepair=sum(Onepair)/numTrials
    meanTwopair=(sum(TwoPair)/numTrials)
    meanThreekind=(sum(Threekind)/numTrials)
    meanStraight=(sum(Straight)/numTrials)
    meanFlush=(sum(Flush)/numTrials)
    meanFullhouse=(sum(Fullhouse)/numTrials)
    meanFourkind=(sum(Fourkind)/numTrials)
    meanStraightflush=(sum(Straightflush)/numTrials)
    meanRoyalflush=(sum(Royalflush)/numTrials)
    
    
    if toPrint:
        print("Simulating",numHands,"number of poker hands ",numTrials,"times")
        
        print(" HighCard Win %",(meanHighcard*100/numHands))
        print(" One Pair Win %",(meanOnepair*100/numHands))
        print(" Two Pair Win %",(meanTwopair*100/numHands))
        print(" Three of a kind Win %",(meanThreekind*100/numHands))
        print(" Straight Win %",(meanStraight*100/numHands))
        print(" Flush Win %",(meanFlush*100/numHands))
        print(" FullHouse Win %",(meanFullhouse*100/numHands))
        
        print(" Four of a kind Win %",(meanFourkind*100/numHands))
        print(" Straight Flush  Win %",(meanStraightflush*100/numHands))
        print(" Royal Flush Win %",(meanRoyalflush*100/numHands))
              
        
        
        
        
        
        

        



def PlayerSimul(numHands,num_player,toPrint=False):
    
    numHighcard=0
    numOnepair=0
    numTwopair=0
    numThreekind=0
    numStraight=0
    numFlush=0
    numFullhouse=0
    numFourkind=0
    numStraightflush=0
    numRoyalflush=0
    numHighcardwin=0
    numOnepairwin=0
    numTwopairwin=0
    numThreekindwin=0
    numStraightwin=0
    numFlushwin=0
    numFullhousewin=0
    numFourkindwin=0
    numStraightflushwin=0
    numRoyalflushwin=0
    
    
    a=[]
    c=[]
    
    
    for b in range(numHands):
        p=PokerHand()
        p.AddPlayer("DK")
        player_name="DK"
        for i in range(num_player-1):
            p.AddPlayer("Player"+str(i))
        
        p.Game()
        p.ShowDown()
        poker_winner=p.getWinner()
        winner=[]
        hand_order=p.getPlayer()[0].getHand_order()
        for b in poker_winner:
            winner.append(b.getName())
       
        
        if player_name in winner:
            poker_hand=p.getHand_order()
            if poker_hand==1:
                numHighcardwin +=1
            
            elif poker_hand==2:
                numOnepairwin +=1
                
            elif poker_hand==3:
                numTwopairwin +=1
                
            elif poker_hand==4:
                numThreekindwin +=1
                
            elif poker_hand==5:
                numStraightwin +=1
                
            elif poker_hand==6:
                numFlushwin +=1
            elif poker_hand==7:
                numFullhousewin +=1
                
            elif poker_hand==8:
                numFourkindwin +=1
                
            elif poker_hand==9:
                numStraightflushwin +=1
                
            elif poker_hand==10:
                numRoyalflushwin +=1
            
            
            
        
        
        if hand_order==1:
            numHighcard +=1
            
        elif hand_order==2:
            numOnepair +=1
            
        elif hand_order==3:
            numTwopair +=1
            
        elif hand_order==4:
            numThreekind +=1
            
        elif hand_order==5:
            numStraight +=1
            
        elif hand_order==6:
            numFlush +=1
        elif hand_order==7:
            numFullhouse +=1
            
        elif hand_order==8:
            numFourkind +=1
            
        elif hand_order==9:
            numStraightflush +=1
            
        elif hand_order==10:
            numRoyalflush +=1
            
            
            
            
    
    if toPrint:
        print("highcards ",numHighcard)
        print("One pair",numOnepair)
        print("Two Pair ",numTwopair)
        print("Three of a kind",numThreekind)
        print("Straight",numStraight)
        print("Flush",numFlush)
        print("Fullhouse",numFullhouse)
        print("Four of a Kind",numFourkind)
        print("straight Flush",numStraightflush)
        print("Royal Flush",numRoyalflush)
    
    
    a.append(numHighcard)
    a.append(numOnepair)
    a.append(numTwopair)
    a.append(numThreekind)
    a.append(numStraight)
    a.append(numFlush)
    a.append(numFullhouse)
    a.append(numFourkind)
    a.append(numStraightflush)
    a.append(numRoyalflush)
    
    
    c.append(numHighcardwin)
    c.append(numOnepairwin)
    c.append(numTwopairwin)
    c.append(numThreekindwin)
    c.append(numStraightwin)
    c.append(numFlushwin)
    c.append(numFullhousewin)
    c.append(numFourkindwin)
    c.append(numStraightflushwin)
    c.append(numRoyalflushwin)
    
    
        
        
        
        
        
    return (a,c)
    
    
    
     
        
        
    
    
            
        
        
        
    
    


    
def PlayerSimulTrial(numHands,numTrials,num_player,toPrint):
    Highcard=[]
    Onepair=[]
    TwoPair=[]
    Threekind=[]
    Straight=[]
    Flush=[]
    Fullhouse=[]
    Fourkind=[]
    Straightflush=[]
    Royalflush=[]
    Highcardwin=[]
    Onepairwin=[]
    TwoPairwin=[]
    Threekindwin=[]
    Straightwin=[]
    Flushwin=[]
    Fullhousewin=[]
    Fourkindwin=[]
    Straightflushwin=[]
    Royalflushwin=[]
    simu_list=[]
    win_list=[]
    
    for b in range(numTrials):
        
        simu_list,win_list=PlayerSimul(numHands,num_player)
        Highcard.append(simu_list[0])
        Onepair.append(simu_list[1])
        TwoPair.append(simu_list[2])
        Threekind.append(simu_list[3])
        Straight.append(simu_list[4])
        Flush.append(simu_list[5])
        Fullhouse.append(simu_list[6])
        Fourkind.append(simu_list[7])
        Straightflush.append(simu_list[8])
        Royalflush.append(simu_list[9])
        Highcardwin.append(win_list[0])
        Onepairwin.append(win_list[1])
        TwoPairwin.append(win_list[2])
        Threekindwin.append(win_list[3])
        Straightwin.append(win_list[4])
        Flushwin.append(win_list[5])
        Fullhousewin.append(win_list[6])
        Fourkindwin.append(win_list[7])
        Straightflushwin.append(win_list[8])
        Royalflushwin.append(win_list[9])
        
        
    
    
    
    meanHighcard=(sum(Highcard)/numTrials)
    meanOnepair=sum(Onepair)/numTrials
    meanTwopair=(sum(TwoPair)/numTrials)
    meanThreekind=(sum(Threekind)/numTrials)
    meanStraight=(sum(Straight)/numTrials)
    meanFlush=(sum(Flush)/numTrials)
    meanFullhouse=(sum(Fullhouse)/numTrials)
    meanFourkind=(sum(Fourkind)/numTrials)
    meanStraightflush=(sum(Straightflush)/numTrials)
    meanRoyalflush=(sum(Royalflush)/numTrials)
    meanHighcardwin=(sum(Highcardwin)/numTrials)
    meanOnepairwin=sum(Onepairwin)/numTrials
    meanTwopairwin=(sum(TwoPairwin)/numTrials)
    meanThreekindwin=(sum(Threekindwin)/numTrials)
    meanStraightwin=(sum(Straightwin)/numTrials)
    meanFlushwin=(sum(Flushwin)/numTrials)
    meanFullhousewin=(sum(Fullhousewin)/numTrials)
    meanFourkindwin=(sum(Fourkindwin)/numTrials)
    meanStraightflushwin=(sum(Straightflushwin)/numTrials)
    meanRoyalflushwin=(sum(Royalflushwin)/numTrials)
    

    
    PHighcard=meanHighcardwin/meanHighcard*100
    POnepair=meanOnepairwin/meanOnepair*100
    PTwopair=meanTwopairwin/meanTwopair*100
    PThreekind=meanThreekindwin/meanThreekind*100
    PStraight=meanStraightwin/meanStraight*100
    PFlush=meanFlushwin/meanFlush*100
    PFullhouse=meanFullhousewin/meanFullhouse*100
    PFourkind=meanFourkindwin/meanFourkind*100
    PStraightflush=meanStraightflushwin/meanStraightflush*100
    try:
        PRoyalflush=meanRoyalflushwin/meanRoyalflush*100
    except ZeroDivisionError:
        PRoyalflush=100
    
        
        
        
    
    Plist=[]
    Plist.append(PHighcard)
    Plist.append(POnepair)
    Plist.append(PTwopair)
    Plist.append(PThreekind)
    Plist.append(PStraight)
    Plist.append(PFlush)
    Plist.append(PFullhouse)
    Plist.append(PFourkind)
    Plist.append(PStraightflush)
    Plist.append(PRoyalflush)
    
    
    
    
    
    
    if toPrint:
        print("Simulating",numHands,"number of poker hands ",numTrials,"times  with",num_player,"players")
        print(" The players best hand ")
        print("HighCard  %", (meanHighcard*100/numHands))
        print(" One Pair  %",(meanOnepair*100/numHands))
        print(" Two Pair  %",(meanTwopair*100/numHands))
        print(" Three of a kind  %",(meanThreekind*100/numHands))
        print(" Straight  %",(meanStraight*100/numHands))
        print(" Flush  %",(meanFlush*100/numHands))
        print(" FullHouse  %",(meanFullhouse*100/numHands))
        print(" Four of a kind  %",(meanFourkind*100/numHands))
        print(" Straight Flush  %",(meanStraightflush*100/numHands))
        print(" Royal Flush  %",(meanRoyalflush*100/numHands))
        print("====================================================")
        print("Percentages of hands that player won the game with")
        print(" HighCard win %",(meanHighcardwin*100/numHands))
        print(" One Pair win %",(meanOnepairwin*100/numHands))
        print(" Two Pair win %",(meanTwopairwin*100/numHands))
        
        print(" Three of a kind win %",(meanThreekindwin*100/numHands))
        print(" Straight win %",(meanStraightwin*100/numHands))
        print(" Flush win %",(meanFlushwin*100/numHands))
        print(" FullHouse win %",(meanFullhousewin*100/numHands))
        print(" Four of a kind win  %",(meanFourkindwin*100/numHands))
        print(" Straight Flush win %",(meanStraightflushwin*100/numHands))
        print(" Royal Flush win  %",(meanRoyalflushwin*100/numHands))
        
        print("====================================")
    
        print("Probability of winning given player has highcard",meanHighcardwin/meanHighcard*100)
        print("Probability of winning given player hasOne pair",meanOnepairwin/meanOnepair*100)
        print("Probability of winning given player has Two pair",meanTwopairwin/meanTwopair*100)
        print("Probability of winning given player has Three of kind",meanThreekindwin/meanThreekind*100)
        
        print("Probability of winning given player has Straight",meanStraightwin/meanStraight*100)
        print("Probability of winning given player has Flush",meanFlushwin/meanFlush*100)
        print("Probability of winning given plyer has Full House",meanFullhousewin/meanFullhouse*100)
        print("Probability of winning given players has FOur of a kind",meanFourkindwin/meanFourkind*100)
        print("Probability of winning given player has Straight Flush",meanStraightflushwin/meanStraightflush*100)
        print("Probability of winning given player has Royal Flush",meanRoyalflushwin/meanRoyalflush*100)
        
        
    
    
    
    return Plist
        
        
        
    
    
    
    
              


def MultiplePlayers(numHands,numTrials):
     num_player=range(2,10)
     Highcard=[]
     Onepair=[]
     Twopair=[]
     Threekind=[]
     Straight=[]
     Flush=[]
     Fullhouse=[]
     Fourkind=[]
     Straightflush=[]
     Royalflush=[]
     for player in num_player:
         print("Now running simulation for "+str(player)+" players")
         Plist=PlayerSimulTrial(numHands, numTrials, player, False)
         Highcard.append(Plist[0])
         Onepair.append(Plist[1])
         Twopair.append(Plist[2])
         Threekind.append(Plist[3])
         Straight.append(Plist[4])
         Flush.append(Plist[5])
         Fullhouse.append(Plist[6])
         Fourkind.append(Plist[7])
         Straightflush.append(Plist[8])
         Royalflush.append(Plist[9])
     Handlist=[]
     Handlist.append(Highcard)
     Handlist.append(Onepair)
     Handlist.append(Twopair)
     Handlist.append(Threekind)
     Handlist.append(Straight)
     Handlist.append(Flush)
     Handlist.append(Fullhouse)
     Handlist.append(Fourkind)
     Handlist.append(Straightflush)
     Handlist.append(Royalflush)
     
     
     for hand in Handlist:
         pylab.plot(num_player,hand,"r-")
         pylab.xlabel("Number of players")
         pylab.ylabel("Winning Probability")
         pylab.ylim(0,110)
         pylab.figure()
     
      
         
     
     
        
        
    

    

            
        
        
    
            
            
        
        



# PokerTrials(10, 100,True)

PlayerSimulTrial(1000, 100, 2, True)                                                  
# MultiplePlayers(1000, 100)
         
            
     

            
        
        



























                
        
    
            
        
        
        
        
                        
      
            
                    
                        
                        
                        
            
                    
            
                    
                
                
            
            
            
            
            
                
            
            
            
            
            
        
        
        
        
       
    
        
            
            
            
            
                    
    
        
        
        
       
                
                    
        
        
            
            
    
                    
                    
        
                
                
            
            
            
            
        
                
        
        
        
        
        
    
    
        
                        
                        
                        
                        
                        
                        
        
                        
        
    
                       
                  
                    
                
                    
                        
                    
                
            
        
            
            
            
            
            
            
        
        
        
    
        
            
            

    
                
        

    
    
    
            
            
        
        
 
        
        
        
                
    
                
        
                
    
        
        
            
        
                
        
                
        
        
    
    

       
        
       
       
        
    
        
            
            
            
            
        
    
        
        
        
        
        
    

            
            













































            
        

        
        
        
        
        
    
    







        
        
        
    
            

        
            
            
    
            
            
            
        
            
            
        
        
        
        
            
        

        
        
        
        

        
        

                
    

        
        
                    
                    
        

    
    
    

        


        
          
