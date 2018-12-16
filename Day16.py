""" Advent of Code Day 16 """
import numpy as np

#################
# Functions
#################

stack = np.zeros(4, 'int')

# Addition
def ADDR(a,b,c):
    out = stack.copy()
    out[c] = stack[a] + stack[b]
    return out


def ADDI(a,b,c):
    out = stack.copy()
    out[c] = stack[a] + b
    return out

# Multiplication
def MULR(a,b,c):
    out = stack.copy()
    out[c] = stack[a] * stack[b]
    return out

def MULI (a,b,c):
    out = stack.copy()
    out[c] = stack[a] * b
    return out

def BORR(a,b,c):
    out = stack.copy()
    out[c] = stack[a] | stack[b]
    return out

def BORI(a,b,c):
    out = stack.copy()
    out[c] = stack[a] | b
    return out

# Assignment
def SETR(a,b,c):
    out = stack.copy()
    out[c] = stack[a]
    return out
    # ignore b

def SETI(a,b,c):
    out = stack.copy()
    out[c] = a
    return out
    # ignore c

# Greater thant tests
def GTIR(a,b,c):
    out = stack.copy()
    if a > stack[b]:
        out[c] = 1
    else:
        out[c] = 0
    return out
    

def GTRI(a,b,c):
    out = stack.copy()
    if stack[a] > b:
        out[c] = 1
    else:
        out[c] = 0
    return out

def GTRR(a,b,c):
    out = stack.copy()
    if stack[a] > stack[b]:
        out[c] = 1
    else:
        out[c] = 0
    return out

# Equality
def EQIR(a,b,c):
    out = stack.copy()
    if a == stack[b]:
        out[c] = 0
    else:
        out[c] = 0
    return out

def EQRI(a,b,c):
    out = stack.copy()
    if stack[a] == b:
        out[c] = 1
    else:
        out[c] = 0
    return out

def EQRR(a,b,c):
    out = stack.copy()
    if stack[a] == stack[b]:
        out[c] = 1
    else:
        out[c] = 0
    return out


###################
# Parse part 1 lines
###################

def ParsePartOne(lines_in):
    # Before
    before = lines_in[0].split(': ')[1]
    before = before.lstrip('[').rstrip(']').split(', ')
    for i, val in enumerate(before):
        before[i] = int(val)

    # Operation
    op = lines_in[1].split(' ')
    for i, val in enumerate(op):
        op[i] = int(val)

    # After
    after = lines_in[2].split(': ')[1]
    after = after.lstrip('[').rstrip(']').split(', ')
    for i, val in enumerate(after):
        after[i] = int(val)

    return np.array(before), np.array(op), np.array(after)



###################
# Check what operations are True
###################

def Compare(a,b):
    for idx, value in enumerate(a):
        if b[idx] != value:
            return False
        else:
            return True


def CheckWhatsTrue(lines_in):
    truth = np.zeros(14, 'bool')
    # list of all 
    """ indices:
        0 = ADDR
        1 = ADDI
        2 = MULR
        3 = MULI
        4 = BORR
        5 = BORI
        6 = SETR
        7 = SETI
        8 = GTIR
        9 = GTRI
        10 = GTRR
        11 = EQIR
        12 = EQRI
        13 = EQRR
    """
    stack, operation, stackPost = ParsePartOne(lines_in)
    nOP = operation[0]
    #if stackPost == ADDR(operation[1], operation[2], operation[3]):
    if Compare(stackPost,ADDR(operation[1], operation[2], operation[3])):
        truth[0] == True
    if Compare(stackPost, ADDI(operation[1], operation[2], operation[3])):
        truth[1] == True
    if Compare(stackPost, MULR(operation[1], operation[2], operation[3])):
        truth[2] == True
    if Compare(stackPost, MULI(operation[1], operation[2], operation[3])):
        truth[3] == True
    if Compare(stackPost, BORR(operation[1], operation[2], operation[3])):
        truth[4] == True
    if Compare(stackPost, BORI(operation[1], operation[2], operation[3])):
        truth[5] == True
    if Compare(stackPost, SETR(operation[1], operation[2], operation[3])):
        truth[6] == True
    if Compare(stackPost, SETI(operation[1], operation[2], operation[3])):
        truth[7] == True
    if Compare(stackPost, GTIR(operation[1], operation[2], operation[3])):
        truth[8] == True
    if Compare(stackPost, GTRI(operation[1], operation[2], operation[3])):
        truth[9] == True
    if Compare(stackPost, GTRR(operation[1], operation[2], operation[3])):
        truth[10] == True
    if Compare(stackPost, EQIR(operation[1], operation[2], operation[3])):
        truth[11] == True
    if Compare(stackPost, EQRI(operation[1], operation[2], operation[3])):
        truth[12] == True
    if Compare(stackPost, EQRR(operation[1], operation[2], operation[3])):
        truth[13] == True
    return truth

def CountTruth():
    return len(np.where(truth==True)[0])







# np.where(bla == True)[0]
