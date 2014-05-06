# python packages
from bisect import bisect
from random import random

# original packages
import globals

def calculatePositionWeights(probabilityMatrix):
    positionWeights = []
    for x in range(0, globals.possibleMotifPositions):
        positionWeights.append(__calculatePositionWeight(globals.initialSequence, probabilityMatrix, x))
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
        elif nucleotide is 'T':
            sampleProbability = sampleProbability * probabilityMatrix[1][x]
            backgroundProbability = backgroundProbability * probabilityMatrix[1][0]
        elif nucleotide is 'C':
            sampleProbability = sampleProbability * probabilityMatrix[2][x]
            backgroundProbability = backgroundProbability * probabilityMatrix[2][0]
        elif nucleotide is 'G':
            sampleProbability = sampleProbability * probabilityMatrix[3][x]
            backgroundProbability = backgroundProbability * probabilityMatrix[3][0]
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
    best = 0
    for x in xrange(1, len(normalizedPositionWeights)):
        if normalizedPositionWeights[x] > normalizedPositionWeights[best]:
            best = x
    return best


    # cdf is a cumulative probability distribution array
    cdf = [normalizedPositionWeights[0]]
    for x in xrange(1, len(normalizedPositionWeights)):
        cdf.append(cdf[-1] + normalizedPositionWeights[x])
    randomIndex = bisect(cdf, random())
    return randomIndex
