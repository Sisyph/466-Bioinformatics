# python packages
from copy import copy, deepcopy

# original packages
import globals


def createProbabilityMatrix(profileMatrix):
    probabilityMatrix = deepcopy(profileMatrix)
    for x in range(0, 4):
        probabilityMatrix[x][0] = __backgroundFrequencyCount(profileMatrix, x)
        for y in range(1, globals.motifLength + 1):
            probabilityMatrix[x][y] = __frequencyCount(profileMatrix, x, y, globals.unchosenSequences)
    return probabilityMatrix

def __frequencyCount(profileMatrix, x, y, unchosenSequences):
    pseudoCount = 0.5
    totalOfPseudoCount = 2
    count = profileMatrix[x][y]
    return (count + pseudoCount) / (unchosenSequences + totalOfPseudoCount)

def __backgroundFrequencyCount(profileMatrix, x):
    pseudoCount = 0.5
    totalOfPseudoCount = 2
    count = profileMatrix[x][0]
    total = 0
    for row in range(0, 4):
        total += profileMatrix[row][0]
    return (count + pseudoCount) / (total + totalOfPseudoCount)

def calculatePositionWeights(probabilityMatrix):
    positionWeights = []
    for x in range(0, globals.possibleMotifPositions):
        positionWeights.append(__calculatePositionWeight(globals.initialSequence, probabilityMatrix, x))
    print positionWeights
    return positionWeights
    

def __calculatePositionWeight(sequence, probabilityMatrix, startingPosition):
    sampleProbability = 1
    backgroundProbability = 1
    for x in range(0, globals.motifLength):
        position = startingPosition + x
        nucleotide = sequence[position]
        if nucleotide is 'A':
            sampleProbability = sampleProbability * probabilityMatrix[0][x]
            backgroundProbability = backgroundProbability * probabilityMatrix[0][0]
        elif nucleotide is 'C':
            sampleProbability = sampleProbability * probabilityMatrix[1][x]
            backgroundProbability = backgroundProbability * probabilityMatrix[1][0]
        elif nucleotide is 'T':
            sampleProbability = sampleProbability * probabilityMatrix[2][x]
            backgroundProbability = backgroundProbability * probabilityMatrix[2][0]
        elif nucleotide is 'G':
            sampleProbability = sampleProbability * probabilityMatrix[3][x]
            backgroundProbability = backgroundProbability * probabilityMatrix[3][0]
    return sampleProbability / backgroundProbability
        
    
    
    
