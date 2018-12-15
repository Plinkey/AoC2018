""" Advent Of Code Day 15"""
"""  This one is going to be difficult."""

import numpy as np

with open('Inputs\Day15.input', 'r') as f:
    rawData = f.read().splitlines()

curMap = np.zeros((len(rawData),len(rawData[0])),'str')

for idx, line in enumerate(rawData):
    for jdx, char in enumerate(line):
        curMap[(idx, jdx)] = char


def DisplayMap():
    for line in curMap:
        print ''.join(line)
        # TODO: for each line, print unit and HP (like in examples from site)

DisplayMap()
