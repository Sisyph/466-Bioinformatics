# python packages
from bisect import bisect
from random import random

# original packages
import globals

def calculatePositionWeights(probabilityMatrix):
    positionWeights = []
    for startingPosition in range(0, globals.possibleMotifPositions):
        positionWeights.append(__calculatePositionWeight(globals.unchosenSequence, probabilityMatrix, startingPosition))
    return positionWeights

def __calculatePositionWeight(sequence, probabilityMatrix, startingPosition):
    sampleProbability = 1.0
    backgroundProbability = 1.0
    backgroundA = probabilityMatrix[0][0]
    backgroundT = probabilityMatrix[1][0]
    backgroundC = probabilityMatrix[2][0]
    backgroundG = probabilityMatrix[3][0]
    for x in range(0, globals.motifLength):
        position = startingPosition + x
        nucleotide = sequence[position]
        if nucleotide is 'A':
            sampleProbability = sampleProbability * probabilityMatrix[0][x + 1]
            backgroundProbability = backgroundProbability * backgroundA
        elif nucleotide is 'T':
            sampleProbability = sampleProbability * probabilityMatrix[1][x + 1]
            backgroundProbability = backgroundProbability * backgroundT
        elif nucleotide is 'C':
            sampleProbability = sampleProbability * probabilityMatrix[2][x + 1]
            backgroundProbability = backgroundProbability * backgroundC
        elif nucleotide is 'G':
            sampleProbability = sampleProbability * probabilityMatrix[3][x + 1]
            backgroundProbability = backgroundProbability * backgroundG
    return sampleProbability / backgroundProbability

def normalizePositionWeights(positionWeights):    
    normalizedPositionWeights = []
    total = 0.0
    for weight in positionWeights:
        total += weight
    for x in range(0, len(positionWeights)):
        normalizedPositionWeights.append(positionWeights[x] / total)
    return normalizedPositionWeights

def choosePosition(normalizedPositionWeights):
    # sample from all probabilities
    # cdf is a cumulative probability distribution array
    cdf = [normalizedPositionWeights[0]]
    for x in xrange(1, len(normalizedPositionWeights)):
        cdf.append(cdf[-1] + normalizedPositionWeights[x])
    randomIndex = bisect(cdf, random())
    return randomIndex
    
    # sample from best probability
    best = 0
    for x in xrange(1, len(normalizedPositionWeights)):
        if normalizedPositionWeights[x] > normalizedPositionWeights[best]:
            best = x
    return best
