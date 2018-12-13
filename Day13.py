""" Advent of Code Day 13"""
import numpy as np

with open('Inputs\Day13TEST.input','r') as f:
    rawData = f.read().splitlines()

#with open('Inputs\Day12.input','r') as f:
    #rawData = f.read().splitlines()

#
#
#
#
#  NOTE TO MYSELF: X is LEFT AND RIGHT +ve RIGHT
#                  Y is UP AND DOWN    +ve DOWN
#
#
#



############
#  Helper Functions/Classes
############

def PrintMap(MyMap):
    for i in MyMap:
        print ''.join(i)

class Cart:
    def __init__(self,char, initX, initY):
        # Position
        self.curX = initX
        self.curY = initY
        # Pointing
        if char == '<': # pointing left
            self.curPoint = 'Left'
        elif char == '^': # pointing Up
            self.curPoint = 'Up'
        elif char == '>': # pointing Right
            self.curPoint = 'Right'
        elif char == 'v': # pointing Down
            self.curPoint = 'Down'
        else:
            print "Shit. Something broke when determining initial pointing"
        self.turns = ['Left','Straight','Right']

    def MoveCart(self):
        if curPoint == 'Left':
            self.curX -= 1
        elif curPoint == 'Right':
            self.curX += 1
        elif curPoint == 'Up':
            self.curY -= 1
        elif curPoint == 'Down':
            self.curY += 1
    
    def WhichWay(self):
        # When encountering an intersection, returns which way the cart should go
        answer = self.turns[0]
        self.turns = self.turns[1:] + self.turns[:1]
        return answer

    def EncounterIntersection(self):
        # When cart lands on intersection, it'll first turn left, then straight, then right
        # This all happens instantly, the next turn it will move the next spot in that dir
        TurnCart(WhichWay())

    def EncounterTurn(self):
        # When cart lands on turn in the track, turn the cart in that direction 
        trackPiece = MyMap[curY][curX]
        if trackPiece == '/': # left turn or right turn, depending on direction
            if self.curPoint == 'Left': # then you're turning Left
                TurnCart('Left')
            elif self.curPoint == 'Up': # then you're turning RIGHT
                TurnCart('Right')
            elif self.curPoint == 'Right' # then you're turning LEFT
                TurnCart('Left')
            elif self.curPoint == 'Down' # then you're turning RIGHT
                Turn Cart('Right')
        elif trackPiece == '\\':
            if self.curPoint == 'Left': # then you're turning Left
                TurnCart('Right')
            elif self.curPoint == 'Up': # then you're turning RIGHT
                TurnCart('Left')
            elif self.curPoint == 'Right' # then you're turning LEFT
                TurnCart('Right')
            elif self.curPoint == 'Down' # then you're turning RIGHT
                Turn Cart('Left')


    def TurnCart(self, direction):
        pointing




############
#  Initialize
############



mapSizeY = len(rawData)
mapSizeX = len(rawData[0])

# Seed empty CartMap of correct size.  Spaces represent nothing
# Will fill in map with cart lines in separate process
CartMap = np.full([mapSizeY, mapSizeX], ' ',dtype=str)




############
#  Read Map, Create Cart
############

# Fill in Cart Map
for ydx, line in enumerate(rawData): # for each line in rawData
    for xdx, char in enumerate(line): #for each character in line 
        if char not in ['<','>','^','v']: # will handle track under carts differently
            CartMap[ydx][xdx] = char
        elif char in ['<','>']: # replace with horizontal track
            CartMap[ydx][xdx] = '-'
            # TODO: Cart Found, create cart
        elif char in ['^','v']: # replace with vertical track
            CartMap[ydx][xdx] = '|'
            # TODO: Cart Found, create cart
        else:
            print "Shit. Something Broke when reading MAP."

PrintMap(CartMap)
