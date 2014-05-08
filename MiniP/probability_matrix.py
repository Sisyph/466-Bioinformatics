# python packages
from copy import copy, deepcopy
import math

# original packages
import globals


def createProbabilityMatrix(profileMatrix):
    probabilityMatrix = deepcopy(profileMatrix)
    for x in range(0, 4):
        probabilityMatrix[x][0] = __backgroundFrequencyCount(profileMatrix, x)
        for y in range(1, globals.motifLength + 1):
            probabilityMatrix[x][y] = __frequencyCount(profileMatrix, x, y, globals.numberOfSequences - 1)
    return probabilityMatrix

def __frequencyCount(profileMatrix, x, y, numberOfUnchosenSequences):
    pseudoCount = 0.9
    totalOfPseudoCount = pseudoCount * 4
    count = profileMatrix[x][y]
    return (count + pseudoCount) / (numberOfUnchosenSequences + totalOfPseudoCount)


def __backgroundFrequencyCount(profileMatrix, x):
    pseudoCount = 0.9
    totalOfPseudoCount = pseudoCount * 4
    count = profileMatrix[x][0]
    total = 0.0
    for row in range(0, 4):
        total += profileMatrix[row][0]
    return (count + pseudoCount) / (total + totalOfPseudoCount)

def calculateInformationContent(probabilityMatrix, positions):
    sequences = globals.sequences
    informationContent = 0.0
    backgroundA = probabilityMatrix[0][0]
    backgroundT = probabilityMatrix[1][0]
    backgroundC = probabilityMatrix[2][0]
    backgroundG = probabilityMatrix[3][0]
    for sequenceIndex in range(0, len(sequences)):
        sequence = list(sequences[sequenceIndex])
        for x in range(0, globals.motifLength):
            position = positions[sequenceIndex] + x
            nucleotide = sequence[position]
            if nucleotide == 'A':
                residual = probabilityMatrix[0][x + 1]
                informationContent += residual * math.log(residual / backgroundA)
            elif nucleotide == 'T':
                residual = probabilityMatrix[1][x + 1]
                informationContent += residual * math.log(residual / backgroundT)
            elif nucleotide == 'C':
                residual = probabilityMatrix[2][x + 1]
                background = probabilityMatrix[2][0]
                informationContent += residual * math.log(residual / backgroundC)
            elif nucleotide == 'G':
                residual = probabilityMatrix[3][x + 1]
                informationContent += residual * math.log(residual / backgroundG)
    return informationContent
            
            
                
    
    
    
    
    
