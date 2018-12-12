""" Advent of Code 2018 Day 12"""

#with open('Inputs\Day12TEST.input','r') as f:
    #rawData = f.read().splitlines()


with open('Inputs\Day12.input','r') as f:
    rawData = f.read().splitlines()

## Initial State
initialState = rawData[0].split(':')[1].lstrip(' ')


def ParseRules(line):
    inpt = line.split(' => ')[0]
    result = line.split(' => ')[1]
    return [inpt, result]

def Rules(strSplit):
    #The plant in question is always idx = 2 (3rd plant from left)
    rules = []
    for line in rawData[2:]:
        rules.append(ParseRules(line))
    for rule in rules:
        if strSplit == rule[0]:
            return rule[1]
    return '.'



# Seeding generation 0

MyPlants = []
stopGen = 21
MyPlants.append('................................................' + initialState + '....................................................................................')

def NextGen(curGen):
    newStr = ''
    for idx in range(len(curGen)):
        if idx - 2 > 0 and idx+3 < len(curGen):
            string = curGen[idx-2:idx+3]
            newChar = Rules(string)
            newStr = newStr + newChar
        else:
            newStr = newStr + '.'
    return newStr

for i in range(stopGen):
    MyPlants.append(NextGen(MyPlants[i]))

total = 0
for plant in MyPlants:
    print plant
    total = total + plant.count('#')
print total


""""
for GenIdx in range(stopGen):
    curGen = MyPlants[GenIdx]
    newStr = ''
    for plantIdx in range(len(curGen)):
        if plantIdx-2 > 0 and plantIdx+3 < len(curGen):
            string = curGen[plantIdx-2:plantIdx+3]
            newChar = Rules(string)
            newStr = newStr + newChar
        else:
            newStr = newStr + '.'
    print newStr
    MyPlants.append(newStr)
    """



"""
for GenIdx in range(stopGen-1):
    for plantIdx in range(2,len(MyPlants[GenIdx])-3):
        string = MyPlants[GenIdx][plantIdx-2:plantIdx+3]
        print string
        for rule in rules:
            newChar = RunRule(string, rule[0], rule[1])
            if newChar:
                newStr = MyPlants[GenIdx+1][:plantIdx] + newChar + MyPlants[GenIdx+1][plantIdx+1:]
                MyPlants[GenIdx+1] = newStr

        #for rule in rules:
        #    newChar = RunRule(string, rule[0], rule[1])
        #    print newChar
        #    newStr = MyPlants[GenIdx+1][:plantIdx] + newChar + MyPlants[GenIdx+1][plantIdx+1:]
"""
#print MyPlants[20][10-3:38]
#print RunRule('.....', rules[0][0],rules[0][1])


#for plant in MyPlants:
    #print plant[10-3:38]
