# python packages
import random
import datetime
import sys

# original packages
import globals
import directory
import reader
import writer
import profile_matrix
import probability_matrix
import position_weights

def findMotif(sequences, motifLength, iterations):
        # initialize global sequence and motif variables
        globals.initialize(sequences, motifLength)

        # choose a random motif position for each unchosen sequence
        positions = chooseMotifPositions()

        # initialize iteration variables
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
                        # count residue and background occurences for each position for all unchosen sequences
                        profileMatrix = profile_matrix.createProfileMatrix(positions, unchosenSequenceIndex)

                        # determine residue and background probabilities
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

                        # calculate information content of current sample
                        currentInformationContent = probability_matrix.calculateInformationContent(probabilityMatrix, positions)
                        
                        # update best sample if current has greater information content
                        if currentInformationContent > bestInformationContent:
                                bestInformationContent = currentInformationContent
                                bestPositions = list(positions)
                                bestProfileMatrix = list(profileMatrix)
        
                        # update unchosen sequence value for next iteration
                        if unchosenSequenceIndex < (len(sequences) - 1):
                                globals.unchosenSequence = sequences[unchosenSequenceIndex + 1]
        
        return [bestPositions, bestProfileMatrix, bestInformationContent]

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
        informationContent = 0
        for x in range(0, numberOfFiles):
                sequencesFile = sequencesFiles[x]
                motifLengthFile = motifLengthFiles[x]
                sequences = reader.readFastaFile(sequencesFile)
                motifLength = reader.readMotifLengthFile(motifLengthFile)
                output = findMotif(sequences, motifLength, int(sys.argv[1]))
                informationContent += output[2]
                writer.writePredictions(output, sequencesFile, motifLength)
                print "files written for " + str(sequencesFile)
                if (x + 1) % 10 == 0:
                        print "\naverage information content for this set: " + str(informationContent/10) + '\n'
                        informationContent = 0
                        

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


