# python packages
import random
import datetime

# original packages
import globals
import directory
import reader
import writer
import profile_matrix
import probability_matrix
import position_weights

def findMotif(sequences, motifLength):
        # initialize global sequence and motif variables
        globals.initialize(sequences, motifLength)

        # choose a random motif position for each unchosen sequence
        positions = chooseMotifPositions()

        # initialize iteration variables
        iterations = 100
        currentInformationContent = 0.0
        bestInformationContent = 0.0
        profileMatrix = []
        probabilityMatrix = []
        positionWeights = []
        normalizedPositionWeights = []
        bestPositions = []
        bestProfileMatrix = []

        for iteration in range(0, iterations):
                for unchosenSequenceIndex in range(0, len(sequences)):
                        # count residue occurences for each position for all unchosen sequences
                        profileMatrix = profile_matrix.createProfileMatrix(positions, unchosenSequenceIndex)

                        # determine frequency and background frequency for each of the residue occurences
                        probabilityMatrix = probability_matrix.createProbabilityMatrix(profileMatrix)

                        # calculate weight for each possible motif position in the chosen sequence
                        positionWeights = position_weights.calculatePositionWeights(probabilityMatrix)

                        # normalize position weights
                        normalizedPositionWeights = position_weights.normalizePositionWeights(positionWeights)
                        
                        # randomly choose position based on normalized probabilities
                        positions[unchosenSequenceIndex] = position_weights.choosePosition(normalizedPositionWeights)
                        
                        # recalculate profile and probability matrix
                        profileMatrix = profile_matrix.createProfileMatrix(positions, -1)
                        probabilityMatrix = probability_matrix.createProbabilityMatrix(profileMatrix)

                        # calculate information content of sample
                        currentInformationContent = probability_matrix.calculateInformationContent(probabilityMatrix, positions)
                        
                        if currentInformationContent > bestInformationContent:
                                bestInformationContent = currentInformationContent
                                bestPositions = list(positions)
                                bestProfileMatrix = list(profileMatrix)
        
                        if unchosenSequenceIndex < (len(sequences) - 1):
                                globals.unchosenSequence = sequences[unchosenSequenceIndex + 1]
        
        print "information content = " + str(bestInformationContent)
        return [bestPositions, bestProfileMatrix]

def chooseMotifPositions():
        positions = []
        for x in range(0, globals.numberOfSequences): 
                positions.append(random.randint(0, globals.lengthOfSequences - globals.motifLength))
        return positions
        
if __name__ == "__main__":
        print "\nRunning motif finder..."
        print "-----------------------" + '\n'

        startTime = datetime.datetime.now()
        print "start time = " + str(startTime) + '\n'

        # create array of motif length text files
        motifLengthFiles = directory.getFiles('motiflength.txt')
        sequencesFiles = directory.getFiles('sequences.fa')
        numberOfFiles = len(motifLengthFiles)

        # iterate over arrays 
        for x in range(0, numberOfFiles):
                sequencesFile = sequencesFiles[x]
                motifLengthFile = motifLengthFiles[x]
                sequences = reader.readFastaFile(sequencesFile)
                motifLength = reader.readMotifLengthFile(motifLengthFile)
                output = findMotif(sequences, motifLength)
                writer.writePredictions(output, sequencesFile, motifLength)
                print "files written for " + str(sequencesFile) + '\n'

        endTime = datetime.datetime.now()
        print "\nend time = " + str(endTime)
        print "run time = " + str(endTime - startTime)

        print "\n---------------------"
        print "Motif finder complete" + '\n'


#for each of the 70 subdirectories does the following
#reads in motiflength.txt and sequences.fa
#performs motif finding algorith on input to generate pwm, and find binding site in each sequence
#
#writes predicted location of binding site in each sequence to "predictedsites.txt" (format tbd, same as sites.txt)
#writes pwm to "predictedmotif.txt" refer to instruction doc


