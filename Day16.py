""" Advent of Code Day 16 """
import numpy as np

#################
# Functions
#################

stack = np.zeros(4, 'int')

# Addition
def ADDR(a,b,c):
    stack[c] = stack[a] + stack[b]

def ADDI(a,b,c):
    stack[c] = stack[a] + b

# Multiplication
def MULR(a,b,c):
    stack[c] = stack[a] * stack[b]

def MULI (a,b,c):
    stack[c] = stack[a] * b

def BORR(a,b,c):
    stack[c] = stack[a] | stack[b]

def BORI(a,b,c):
    stack[c] = stack[a] | b

# Assignment
def SETR(a,b,c):
    stack[c] = stack[a]
    # ignore b

def SETI(a,b,c):
    stack[c] = a
    # ignore c

# Greater thant tests
def GTIR(a,b,c):
    if a > stack[b]:
        stack[c] = 1
    else:
        stack[c] = 0

def GTRI(a,b,c):
    if stack[a] > b:
        stack[c] = 1
    else:
        stack[c] = 0

def GTRR(a,b,c):
    if stack[a] > stack[b]:
        stack[c] = 1
    else:
        stack[c] = 0

# Equality
def EQIR(a,b,c):
    if a == stack[b]:
        stack[c] = 0
    else:
        stack[c] = 0

def EQRI(a,b,c):
    if stack[a] == b:
        stack[c] = 1
    else:
        stack[c] = 0

def EQRR(a,b,c):
    if stack[a] == stack[b]:
        stack[c] = 1
    else:
        stack[c] = 0
