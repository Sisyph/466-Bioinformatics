import globals

def createProfileMatrix(sequences, initialPositions):
    profileMatrix = [[0 for x in xrange(globals.motifLength + 1)] for x in xrange(4)]
    totalAMotif, totalCMotif, totalTMotif, totalGMotif = 0, 0, 0, 0
    totalA, totalC, totalT, totalG = 0, 0, 0, 0

    # count occurences of each nucleotide in each position of the motif
    for x in range(0, globals.motifLength):
        for y in range(0, len(sequences)):
            sequenceList = list(sequences[y])
            initialPosition = initialPositions[y]
            nucleotide = sequenceList[initialPosition + x]
            if nucleotide is 'A':
                profileMatrix[0][x + 1] += 1
                totalAMotif += 1
            elif nucleotide is 'C':
                profileMatrix[1][x + 1] += 1
                totalCMotif += 1
            elif nucleotide is 'T':
                profileMatrix[2][x + 1] += 1
                totalTMotif += 1
            elif nucleotide is 'G':
                profileMatrix[3][x + 1] += 1
                totalGMotif += 1
    
    # count occurences of each nucleotide in entire sequence
    for x in range(0, len(sequences) - 1):
        sequenceList = list(sequences[x])
        totalA += sequenceList.count('A') 
        totalC += sequenceList.count('C')
        totalT += sequenceList.count('G')
        totalG += sequenceList.count('T')
    
    # count occurences of each nucleotide outside of the motif
    profileMatrix[0][0] = totalA - totalAMotif
    profileMatrix[1][0] = totalC - totalCMotif
    profileMatrix[2][0] = totalT - totalTMotif
    profileMatrix[3][0] = totalG - totalGMotif
        
    return profileMatrix
