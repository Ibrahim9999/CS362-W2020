# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 2:32:00 2020

@author: mahmoudi
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = testUtility.PlayerNames()

#number of curses and victory cards
nV = testUtility.VictoryCardNum(player_names)
nC = testUtility.CurseNum(player_names)

#Define box
box = testUtility.DefineBox(nV)

supply_order = testUtility.SupplyOrder()

#Pick 10 cards from box to be in the supply.
supply = testUtility.PickSupply(box)

#The supply always has these cards
testUtility.SupplyCards(supply, player_names, nV, nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = []
for name in player_names:
    if name[0]=="*":
        players.append(Dominion.ComputerPlayer(name[1:]))
    elif name[0]=="^":
        players.append(Dominion.TablePlayer(name[1:]))
    else:
        players.append(Dominion.Player(name))

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)