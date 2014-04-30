def createProfileMatrix(sequences, motifLength, initialPositions):
    profileMatrix = [4][motifLength + 1]
    totalAMotif, totalCMotif, totalTMotif, totalGMotif = 0
    totalA, totalC, totalT, totalG = 0

    # count occurences of each nucleotide in each position of the motif
    for x in range(0, motifLength - 1):
        for y in range(0, len(sequences) - 1):
            sequenceList = list(sequences[y])
            nucleotide = sequenceList[initialPositions[y] + x]
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
        sequenceList = len(sequences[x])
        totalA += sequencesList.count('A') 
        totalC += sequencesList.count('C')
        totalT += sequencesList.count('G')
        totalG += sequencesList.count('T')
    
    # count occurences of each nucleotide outside of the motif
    profileMatrix[0][0] = totalA - totalAMotif
    profileMatrix[0][1] = totalC - totalCMotif
    profileMatrix[0][2] = totalT - totalTMotif
    profileMatrix[0][3] = totalG - totalGMotif
        
    return profileMatrix
