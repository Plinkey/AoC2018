""" Advent of Code Day 18


NOTES:
    lumber area is 50 x 50
    . ground
    | trees
    # lumberyard
    scan of the area is puzzle input

    looks at surrounding 8 NW N NE
                            W    E
                           SW S SE
    
    if 3 or more are |:
        . -> |
    else:
        nothing

    if nSurroundTrees >= 3:
        . becomes |
    else:
        nothing

#########################
    if 3 or more are #
        | -> #
    else:
        nothing

    if nsurroundLumber >= 3:
        | becomes #
    else:
        nothing


#########################
    if 1 or more are # AND 1 or more |:
        # remains
    else:
        # -> . 


    if nSurroundLumber >= 1 AND nSurroundTrees >= 1:
        nothing
    else:
        # becomes .

    everything happens simultaneouslys

"""
import numpy as np

with open('Inputs\Day18TEST.input', 'r') as f:
    rawData = f.read().splitlines()

Map = np.zeros([len(rawData), len(rawData[0])], 'str')
for idx, line in enumerate(rawData):
    for jdx, value in enumerate(line):
        Map[idx, jdx] = value 

print Map


##################
# Helper functions
##################

def GetSurround(ydx,xdx):
    yLen, xLen = Map.shape 
    # NORTHWEST
    if ydx > 0 and xdx > 0:
        NW = Map[(ydx-1, xdx-1)]
    else:
        NW = ' '

    # NORTH
    if ydx > 0:
        N  = Map[(ydx-1, xdx)]
    else:
        N = ' '

    # NORTHEAST
    if ydx > 0 and xdx < xLen-2:
        NE = Map[(ydx-1, xdx+1)]
    else:
        NE = ' '

    # WEST
    if xdx > 0:
        W  = Map[(ydx, xdx-1)]
    else:
        W = ' '

    # EAST
    if xdx < xLen-2:
        E  = Map[(ydx, xdx+1)]
    else:
        E = ' '


    # SOUTHWEST
    if ydx < yLen-2 and xdx > 0:
        SW = Map[(ydx+1, xdx-1)]
    else:
        SW = ' '

    #SOUTH
    if ydx < yLen-2:
        S  = Map[(ydx+1, xdx)]
    else:
        S = ' '

    # SOOUTHEAST
    if ydx < yLen-2 and xdx < xLen-2:
        SE = Map[(ydx+1, xdx+1)]
    else:
        SE = ' '
    return [NW, N, NE, W, E, SW, S, SE]

print 'Testing GetSurround with Day18TEST.input'
print 'The line below should equal [\' \', \' \', \' \', \' \', \'#\', \' \', \'.\', \'.\']'
print GetSurround(0,0)


def CountTrees(idx, jdx):
    surround = GetSurround(idx, jdx)
    return surround.count('|')

print "Testing CountTrees with Day18TEST.input"
print "The line below should = 0"
print CountTrees(0,0)
print ''
print 'The line below should = 2'
print CountTrees(3,1)

def CountLumber(idx, jdx):
    surround = GetSurround(idx, jdx)
    return surround.count('#')

print "Testing CountLumber with Day18TEST.input"
print "The line below should = 1"
print CountLumber(0,0)
print ''
print 'The line below should = 2'
print CountLumber(0,2)
print ''
print 'The line below should = 2'
print CountLumber(5,1)


