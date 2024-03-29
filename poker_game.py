# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:49:47 2020

@author: dhruv
"""


import random
import copy
import collections
from operator import itemgetter
import math


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
# p=Deal().GetComCard()
# print(p)
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
        self.all_status=False
        self.player_pot=0

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

    def getAllStat(self):
        return self.all_status
    
    def getPot(self):
        return self.player_pot
        

    def All_in(self):
        self.all_status=True

    def addCash(self,amount):
        self.cash+=amount
    
    def addPot(self,amount):
        self.player_pot+=amount

    def removeCash(self,amount):
        self.cash-=amount

    def Call(self,call):
        self.removeCash(call)

    def Fold(self):
        self.fold_status=True

    def Raise(self,raise_amount):
        self.removeCash(raise_amount)
        
    def ResetHand(self):
        self.Cards={}
        self.Hand_order=0
        self.MaxVal=0
        self.kicker=0
        self.fold_status=False
        self.all_status=False
        self.player_pot=0






def BestHand(player_card):

    cards=copy.deepcopy(player_card)
    values=[]
    suits=[]
    for card in cards:
        temp_list=cards[card]
        values.append(temp_list[0])
        suits.append(temp_list[1])
                          
                        
    def RoyalFlush():
        rank=copy.deepcopy(values)
        colour=copy.deepcopy(suits)
        if len(rank)<5:
            return (False,0,0,0)
        heart=[]
        diamond=[]
        spade=[]
        club=[]
        royal_straight="1011121314"
        hand_order=0
        flush_stat=False
        
        

        for a in range(len(values)):
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
            return (flush_stat,hand_order,0,0)


        max_colour.sort()
        result_straight=""
        for a in max_colour:
            result_straight +=str(a)

        if royal_straight in result_straight:
            hand_order=10
            flush_stat=True

        return (flush_stat,hand_order,0,0)

    # k=RoyalFlush()
    # print(k)



 
    def StraightFlush():
        rank=copy.deepcopy(values)
        colour=copy.deepcopy(suits)
        if len(rank)<5:
            return (False,0,0,0)
        heart=[]
        diamond=[]
        spade=[]
        club=[]
       
        flush_stat=False
        hand_order=0
        MaxVal=0

        
        
        
        normal_straight=[]
        normal_straight.append("234514")

        for i in range(2,14):
            result=""
            if i+5<15:

                for j in range(5):
                    result +=str(i+j)
                normal_straight.append(result)




       

        for a in range(len(values)):
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
            return (flush_stat,hand_order,MaxVal,0)


        max_colour.sort()
        result_straight=""
        for a in max_colour:
            result_straight +=str(a)


        for b in normal_straight:
            if b in result_straight:
                hand_order=9
                flush_stat=True
                last_digit=int(b[-1])
                if last_digit in (6,7,8,9):
                    MaxVal=last_digit
                else:
                    last_digit +=10
                    MaxVal=last_digit
                break
                
        return (flush_stat,hand_order,MaxVal,0)
    
    # k=StraightFlush()
    # print(k)


    def FourKind():
        rank=copy.deepcopy(values)
        if len(rank)<5:
            return (False,0,0,0)
        hand_order=0
        MaxVal=0
        kicker=0
        four_kind_stat=False
        
        count=collections.Counter(rank)
        
        for key in count:
            if count[key]==4:
                hand_order=8
                MaxVal=key
                four_kind_stat=True
        
        if hand_order==8:
            for i in range(4):
                rank.remove(MaxVal)
            kicker=max(rank)



        return (four_kind_stat,hand_order,MaxVal,kicker)
    
    # k=FourKind()
    # print(k)


    def FullHouse():
        rank=copy.deepcopy(values)
        if len(rank)<5:
            return (False,0,0,0)
        hand_order=0
        MaxVal=0
        kicker=0
        count=collections.Counter(rank)
        three_kind_stat=False
    
        full_house_stat=False
        
        for key in count:
            if count[key]==3:
                three_kind_stat=True
                if key>MaxVal:
                    MaxVal=key
        
        
        if three_kind_stat:
            count.pop(MaxVal)
            for key in count:
                    if count[key]>=2 and key>kicker:
                        kicker=key
                        hand_order=7
                        full_house_stat=True


        return (full_house_stat,hand_order,MaxVal,kicker)
    
    # k=FullHouse()
    # print(k)


    def Flush():
        rank=copy.deepcopy(values)
        colour=copy.deepcopy(suits)
        if len(rank)<5:
            return (False,0,0,0)
        heart=[]
        diamond=[]
        spade=[]
        club=[]

        hand_order=0
        MaxVal=0
        flush_stat=False
        

        for a in range(len(values)):
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
            return (flush_stat,hand_order,MaxVal,0)
        
        
        flush_stat=True
        hand_order=6
        MaxVal=max(max_colour)
        return (flush_stat,hand_order,MaxVal,0)
    
    # k=Flush()
    # print(k)


    
        
    def Straight():
        rank=copy.deepcopy(values)
        if len(rank)<5:
            return (False,0,0,0)
        hand_order=0
        MaxVal=0
        straight=[]
        straight_stat=False
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
        
        if len(unique_rank)>=5:
            

            unique_rank.sort()
            unique_rank=unique_rank[-5:]
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
                    straight_stat=True
                    break



        return (straight_stat,hand_order,MaxVal,0)
    
    # k=Straight()
    # print(k)

  
    def ThreeKind():
        rank=copy.deepcopy(values)
        if len(rank)<3:
            return (False,0,0,0)
        hand_order=0
        MaxVal=0
        kicker1=0
        kicker2=0
        kicker=0
        count=collections.Counter(rank)
        three_stat=False
        
        for key in count:
            if count[key]==3:
                three_stat=True
                if key>MaxVal:
                    MaxVal=key
        

        if three_stat:
            for a in range(3):
                rank.remove(MaxVal)
            rank.sort()
            hand_order=4
            kicker1=rank[-1]
            kicker2=rank[-2]
            kicker=int(str(kicker1)+str(kicker2))



        return (three_stat,hand_order,MaxVal,kicker)
    
    # k=ThreeKind()
    # print(k)
    


    def TwoPair():
        rank=copy.deepcopy(values)
        if len(rank)<4:
            return (False,0,0,0)
        count=collections.Counter(rank)
        hand_order=0
        MaxVal=0
        kicker=0
        kicker1=0
        kicker2=0
        pairs=[]
        two_stat=False

        for key in count:
            if count[key]==2:
                pairs.append(key)


        if len(pairs)>=2:
            two_stat=True
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


        return (two_stat,hand_order,MaxVal,kicker)
    
    # k=TwoPair()
    # print(k)





    def OnePair():
        rank=copy.deepcopy(values)
        count=collections.Counter(rank)
        hand_order=0
        MaxVal=0
        kicker=0
        kicker1=0
        kicker2=0
        kicker3=0
        pairs=[]
        pair_stat=False

        for key in count:
            if count[key]==2:
                pairs.append(key)

        if len(pairs)==1:
            pair_stat=True
            hand_order=2
            MaxVal=pairs[0]


            for b in range(2):
                rank.remove(MaxVal)
            rank.sort()
            kicker1=rank[-1]
            kicker2=rank[-2]
            kicker3=rank[-3]
            kicker=int(str(kicker1)+str(kicker2)+str(kicker3))




        return (pair_stat,hand_order,MaxVal,kicker)
    # k=OnePair()
    # print(k)




    def HighCard():
        rank=copy.deepcopy(values)
        hand_order=1
        rank.sort()
        kicker=0
        MaxVal=rank[-1]
        kicker1=rank[-2]
        kicker2=rank[-3]
        kicker3=rank[-4]
        kicker4=rank[-5]
        kicker=int(str(kicker1)+str(kicker2)+str(kicker3)+str(kicker4))

        return (True,hand_order,MaxVal,kicker)
    # k=OnePair()
    # print(k)
    

    k=RoyalFlush()
    # print(k)
    if not k[0]:
        k=StraightFlush()
    
    if not k[0]:
        k=FourKind()
        
    if not k[0]:
        k=FullHouse()
        
    if not k[0]:
        k=Flush()

    if not k[0]:
        k=Straight()
        
    if not k[0]:
        k=ThreeKind()
        
    if not k[0]:
        k=TwoPair()
        
    if not k[0]:
        k=OnePair()
    if not k[0]:
        k=HighCard()
        
    
    return k[1:]

### use an active player list of player indexes instead of checking for each player in a loop???
class poker_table():
    def __init__(self,players,dealer,big_blind,small_blind):
        self.players=players
        self.big_blind=big_blind
        self.small_blind=small_blind
        self.deal=dealer
        self.pot=0
        self.call=0
        self.big_pos=0
        self.small_pos=0
        self.active_index=0
        self.active_player_count=len(self.players)
        self.dealer=0
        self.game_end_stat=False
    
    def set_blind_pos(self):
        small_blind=self.dealer+1
        if small_blind>=len(self.players):
            small_blind=0
        
        big_blind=small_blind+1
        if big_blind>=len(self.players):
            big_blind=0
        
        self.small_pos=small_blind
        self.big_pos=big_blind

    def add_player(self,player):
        self.players.append(player)
    
    def remove_player(self,player):
        self.players.remove(player)
    
    def check_fold_stat(self,player_index):
        return self.players[player_index].getFoldStat()
    
    def check_all_in_stat(self,player_index):
        return self.players[player_index].getAllStat()
    
    def set_big_blind(self,amount):
        self.big_blind=amount
    
    def set_small_blind(self,amount):
        self.small_blind=amount
    
    def blind_if_player_removed(self):
        self.dealer=random.randint(0, len(self.players)-1)
    
    def showdown(self):
        show=[]
        for player in self.players:
            if not player.getFoldStat():
                com_card=self.deal.GetComCard()
                player_card=player.getCards()
                best_list=BestHand({**player_card,**com_card})
                best_list=list(best_list)
                player_index=self.players.index(player)
                best_list.append(player_index)
                show.append(best_list)
        
        show_sort=sorted(show,reverse=True,key=itemgetter(0,1,2))
        print(show_sort)
        
        hand_list=[]
        max_hand=show_sort[0][0]
        for item in show_sort:
            if max_hand==item[0]:
                hand_list.append(item)
        
        if len(hand_list)!=1:
            val_list=[]
            max_val=hand_list[0][1]
            for item in hand_list:
                if max_val==item[1]:
                    val_list.append(item)
            
            if len(val_list)!=1:
                kick_list=[]
                max_kick=val_list[0][2]
                for item in val_list:
                    if max_kick==item[2]:
                        kick_list.append(item)
                winners=kick_list
            else:
                winners=val_list
        else:
            winners=hand_list
        
        winner_index=[]
        for item in winners:
            winner_index.append(item[3])
        
        return winner_index
    
    def reset_table(self):
        self.pot=0
        self.call=0
        self.active_index=self.small_pos
        self.active_player_count=len(self.players)
        self.dealer_update()
        
        self.game_end_stat=False
        
        for player in self.players:
            player.ResetHand()
        
        self.deal.DeckReset()
        
    def dealer_update(self):
        self.dealer+=1
        if self.dealer>=len(self.players):
            self.dealer=0
    
    def pot_winner(self,winner_index):
        if type(winner_index)==type(5):
            pot_share=self.pot
            self.players[winner_index].addCash(pot_share)
            print(str(self.players[winner_index].getName())+" won "+str(pot_share))
        else:
            
            
            l=len(winner_index)
            
            pot_share=math.floor(self.pot/l)
            print('---------------------------------')
            
            
            for index in winner_index:
                print(str(self.players[index].getName())+" won "+str(pot_share))
                self.players[index].addCash(pot_share)
        self.game_end_stat=True
        
    
    def place_blinds(self):
        self.players[self.big_pos].removeCash(self.big_blind)
        self.players[self.small_pos].removeCash(self.small_blind)
        self.players[self.big_pos].addPot(self.big_blind)
        self.players[self.small_pos].addPot(self.small_blind)
        amt=self.small_blind+self.big_blind
        self.add_pot(amt)
        
    
    def active_player_update(self):
        self.active_index+=1
        if self.active_index>=len(self.players):
            self.active_index=0
    
    def add_pot(self,amount):
        self.pot+=amount
    
    
    def action_logic(self,player_index):
        
        action_dict={"fold":True,"check":False,"match_bet":False,"raise_bet":True,"all_in":True}
        
        
        
        player_pot=self.players[player_index].getPot()
        
        if self.call>player_pot:
            action_dict["match_bet"]=True
            
        elif self.call==player_pot:
            action_dict["check"]=True
        
       
        legal_action=True
        self.print_player_detail(player_index)
        while legal_action:
            for action in action_dict:
                if action_dict[action]:
                    print(str(action),end=" ")
    
            taken=str(input("Choose a suitable action: ")).lower()
            
            if action_dict[taken]:
                legal_action=False
            else:
                print("action not allowed")
        
        return taken
            
        
    
    
    def action(self,input_action,player_index):
        input_action=input_action.lower()
        
        player_pot=self.players[player_index].getPot()
        player_cash=self.players[player_index].getCash()
        
        
        if input_action=="fold":
            self.players[player_index].Fold()
            self.active_player_count-=1
            
            
        elif input_action=="match_bet":
            print(self.call)
            amount=self.call-player_pot
            if amount<player_cash:
                self.players[player_index].Call(amount)
                self.players[player_index].addPot(amount)
                self.add_pot(amount)
            elif amount>=player_cash:
                self.players[player_index].Call(player_cash)
                
                self.players[player_index].All_in()
                self.players[player_index].addPot(player_cash)
                self.add_pot(player_cash)
                
        
        elif input_action=="all_in":
            self.players[player_index].Call(player_cash)
            self.players[player_index].addPot(player_cash)
            self.players[player_index].All_in()
            self.add_pot(player_cash)
            updated_pot=self.players[player_index].getPot()
            self.call=max(self.call,updated_pot)
        
            
            
        elif input_action=="raise_bet":
            raise_amount=int(input("cash to be raised"))
            if raise_amount<player_cash:
                self.players[player_index].Call(raise_amount)
                self.players[player_index].addPot(raise_amount)
                self.add_pot(raise_amount)
        
            else:
                self.players[player_index].Call(player_cash)
                self.players[player_index].All_in()
                self.players[player_index].addPot(player_cash)
                self.add_pot(player_cash)
            
            
            updated_pot=self.players[player_index].getPot()
            self.call=max(self.call,updated_pot)
      
            
     
        
    def check_last_man(self):
        if self.active_player_count==1:
            return True
        else:
            return False
    
    def pot_last_man(self):
        for player in self.players:
            if not player.getFoldStat():
                return self.players.index(player)
            
            
            
    
    def check_equal_bet_stat(self):
        for player in self.players:
            if not player.getFoldStat():
                if not player.getAllStat():
                    player_pot=player.getPot()
                    
                    if player_pot!=self.call:
                        return False
        return True
        
    
    
    
    
    def check_player_part_stat(self,player_count):
        if player_count>=self.active_player_count:
            return True
        else:
            return False
    
    def all_in_stat(self):
        count=0
        for player in self.players:
            if player.getAllStat():
                count+=1
        
        if count==self.active_player_count or count==self.active_player_count -1:
            return True
        else:
            return False
            
    
        
        
    
    
    def betting_round(self,start_index):
        
        self.active_index=start_index
        player_part_stat=False
        
        equal_bet_stat=False
        round_cond=False
        
        player_count=0
        all_in_stat=self.all_in_stat()
        
        if not all_in_stat:
    
            while not round_cond:
                last_man_stat=self.check_last_man()
                if last_man_stat:
                    winner_index=self.pot_last_man()
                    self.pot_winner(winner_index)
                    break
                
                    
                else:
                  fold_stat=self.check_fold_stat(self.active_index)
                  if not fold_stat:
                    player_count+=1
                    all_stat=self.check_all_in_stat(self.active_index)
                           
                    if not all_stat:
                        action=self.action_logic(self.active_index)
                        self.action(action,self.active_index)
                        
                        
                        self.active_player_update()
                        player_part_stat=self.check_player_part_stat(player_count)
                        
                        equal_bet_stat=self.check_equal_bet_stat()
                        print('player_part_stat ',player_part_stat)
                        print('equal bet stat ',equal_bet_stat)
                        round_cond=player_part_stat and equal_bet_stat
                        print('round_end_stat',round_cond)
                        
    
    def first_round(self,start_index):
        self.betting_round(start_index)
        self.deal.DealFlopCards()
        # print("first round")
     
    
    def second_round(self,start_index):
        self.betting_round(start_index)
        self.deal.DealFourth()
        # print("second round")
        
    
    def third_round(self,start_index):
        self.betting_round(start_index)
        self.deal.DealFifth()
        # print("third round")
      
    
    def fourth_round(self,start_index):
        self.betting_round(start_index)
        winner_index=self.showdown()
        self.pot_winner(winner_index)
        # print("fourth round")
        
        
    
    def find_start_index(self):
        start_index_stat=False
        
        start_index=self.dealer
        while not start_index_stat:
            start_index+=1
            if start_index>=len(self.players):
                start_index=0
            
            player_stat=self.check_fold_stat(start_index)
            
            if not player_stat:
                start_index_stat=True
        
        return start_index
    
    def print_player_detail(self,index):
        player_card=self.players[index].getCards()
        player_card=list(player_card.keys())
        player_name=self.players[index].getName()
        player_cash=self.players[index].getCash()
        com_card=self.deal.GetComCard()
        com_card=list(com_card.keys())
        
        print("-----------------------------------------------")
        print("Pot value: "+str(self.pot))
        print("Player name: "+str(player_name))
        print('Player Available Cash '+str(player_cash))
        print('Hole Cards')
        print(player_card)
        print('Community Cards')
        print(com_card)
        print("------------------------------------------------")
    
    
        
        

                
            
    
    def play_game(self):
        self.set_blind_pos()
        self.deal.DealHoles(self.players)
        self.place_blinds()
        self.call=self.big_blind
        
    
        start_index=self.find_start_index()
        self.first_round(start_index)
        
        if not self.game_end_stat:
            print(self.game_end_stat)
            print("second round")
            start_index=self.find_start_index()
            self.second_round(start_index)
        
        if not self.game_end_stat:
            print(self.game_end_stat)
            print("third round")
            start_index=self.find_start_index()
            self.third_round(start_index)
            
        if not self.game_end_stat:
            print("fourth round")
           
            start_index=self.find_start_index()
            self.fourth_round(start_index)
        
        self.reset_table()
            
            

            
#########intialize##############
deal=Deal()
p1=Player("DK", 10000)
p2=Player('PK', 10000)
p3=Player('JK', 10000)
players=[]
players.append(p1)
players.append(p2)
players.append(p3)

poker_table=poker_table(players,deal,100,50)
poker_table.play_game()
        
        
        
            
        
        
            
                   
                   
               

            



           
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
    
    
                
            
        
        
                
            
            
            
            
            
            
            
            
        
        
        
            
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
     
                
        
            
                
        
        
        
        
        
        
        
                
            
                
                
                
                
    
        
        
        
        
            

    







        
        
    
    
    
    
        


    
    
    
    
    
    
    
    
