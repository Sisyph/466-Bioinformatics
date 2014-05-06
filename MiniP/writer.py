import os
import globals

def writePredictions(output, sequencesFile, motifLength):
    path = os.path.abspath(sequencesFile)
    sitesFile = open(path[0:(len(path) - 12)] + "predictedsites.txt", 'w')
    motifFile = open(path[0:(len(path) - 12)] + "predictedmotif.txt", 'w')
    __writePredictedSites(sitesFile, output[0])
    __writePredictedMotif(motifFile, output[1], motifLength)
    sitesFile.close()
    motifFile.close()
    print "files written for " + path[-31:-13]
    return

def __writePredictedSites(file, positions):
    for x in positions:
        file.write(str(x) + "\n")
    return

def __writePredictedMotif(file, profileMatrix, motifLength):
    file.write(">MOTIF" +'\t' + str(motifLength))
    for x in range(1, globals.motifLength + 1):
        file.write('\t')
        for y in range(0, 4):
            file.write(str(profileMatrix[y][x]) + '\t')
    return
