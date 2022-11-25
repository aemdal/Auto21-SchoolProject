import drawCard
from drawCard import drawCard
import cv2
import os
import autojack
from autojack import playerchoice
from autojack import dealerchoice
from autojack import scorecompare
import serial
import time
import comTest
from comTest import write
from comTest import read
from comTest import wr

# importing the referance pictures and making a list of the card values taken from the pictures name.
directory = "maskImg"
maskImgList = []
deck = []
pictureFolder = os.listdir(directory)



for picture in pictureFolder:
    imgCur = cv2.imread(f"{directory}/{picture}", cv2.IMREAD_UNCHANGED)
    maskImgList.append(imgCur)
    deck.append(os.path.splitext(picture)[0])

drawCardCount = int
drawCardCount = 0
    

playerscores = [2000000,2000000,2000000,2000000]




numberOfPlayers = 1
#send number f player to arduino
tempID = ord('d')
playerID = []
for i in range(numberOfPlayers):
    playerID.append(chr(tempID))
    tempID += 1


dealer = numberOfPlayers
time.sleep(3)
#write('d') 
#print(read())
#print(wr('d'))

while True:
    player1hand = []
    player2hand = []
    player3hand = []
    player4hand = []
    player5hand = []
    players = [player1hand, player2hand, player3hand, player4hand, player5hand]
    for i in range(0, 2):
        for j in range(0, numberOfPlayers + 1):
            cardValue, drawCardCount = drawCard(drawCardCount, deck, maskImgList)
            (players[j]).append(cardValue)
            #send to serial to dispense card
            #sleep until card disp right position
    print("Ready")
    for i in range(numberOfPlayers):
        
        drawCardCount = playerchoice(playerID[i], players[i], drawCardCount, deck, maskImgList)
        
    drawCardCount = dealerchoice(players[dealer], drawCardCount, deck, maskImgList)

    for i in range(numberOfPlayers):
        
        scorecompare(playerID[i], players[i], players[dealer], playerscores[i])
        
    # while !Input - some input to restart gameloop. Or turn off to end game/restart