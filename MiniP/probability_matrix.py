# python packages
from copy import copy, deepcopy

# original packages
import globals
import math


def createProbabilityMatrix(profileMatrix):
    probabilityMatrix = deepcopy(profileMatrix)
    for x in range(0, 4):
        probabilityMatrix[x][0] = __backgroundFrequencyCount(profileMatrix, x)
        for y in range(1, globals.motifLength + 1):
            probabilityMatrix[x][y] = __frequencyCount(profileMatrix, x, y, globals.numberOfSequences - 1)
    return probabilityMatrix

def __frequencyCount(profileMatrix, x, y, numberOfUnchosenSequences):
    pseudoCount = 1.1
    totalOfPseudoCount = pseudoCount * 4
    count = profileMatrix[x][y]
    return (count + pseudoCount) / (numberOfUnchosenSequences + totalOfPseudoCount)


def __backgroundFrequencyCount(profileMatrix, x):
    pseudoCount = 1.1
    totalOfPseudoCount = pseudoCount * 4
    count = profileMatrix[x][0]
    total = 0.0
    for row in range(0, 4):
        total += profileMatrix[row][0]
    return (count + pseudoCount) / (total + totalOfPseudoCount)
    
def calculateInformationContent(probabilityMatrix):
    informationContent = 0
    for x in range(0, 4):
        for y in range(1, globals.motifLength + 1):
            baseFrequency = probabilityMatrix[x][y]
            chanceFrequency = probabilityMatrix[x][0]
            informationContent += baseFrequency * math.log(baseFrequency / chanceFrequency)
    return informationContent
