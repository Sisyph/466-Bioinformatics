# python packages
import random

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
        profileMatrix = []
        probabilityMatrix = []
        positionWeights = []
        normalizedPositionWeights = []
        iterations = 1000

        for iteration in range(0, iterations):
                for unchosenSequence in range(0, len(sequences)):
                        # count residue occurences for each position for all unchosen sequences
                        profileMatrix = profile_matrix.createProfileMatrix(positions, unchosenSequence)

                        # determine frequency and background frequency for each of the residue occurences
                        probabilityMatrix = probability_matrix.createProbabilityMatrix(profileMatrix)

                        # calculate weight for each possible motif position in the chosen sequence
                        positionWeights = position_weights.calculatePositionWeights(probabilityMatrix)

                        # normalize position weights
                        normalizedPositionWeights = position_weights.normalizePositionWeights(positionWeights)
                        
                        # randomly choose position based on normalized probabilities
                        positions[unchosenSequence] = position_weights.choosePosition(normalizedPositionWeights)
        
                        if unchosenSequence < (len(sequences) - 1):
                                globals.initialSequence = sequences[unchosenSequence + 1]
                reset()
        
        return [positions, profileMatrix]

def chooseMotifPositions():
        positions = []
        for x in range(0, globals.numberOfSequences): 
                positions.append(random.randint(0, globals.lengthOfSequences - globals.motifLength))
        return positions

def reset():
    globals.initialSequence = globals.sequences[0]
    return

        
if __name__ == "__main__":
	print "running motif finder..."

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
                print "files written for " + str(sequencesFile)

        print "motif finder complete"


                
        

#for each of the 70 subdirectories does the following
#reads in motiflength.txt and sequences.fa
#performs motif finding algorith on input to generate pwm, and find binding site in each sequence
#
#writes predicted location of binding site in each sequence to "predictedsites.txt" (format tbd, same as sites.txt)
#writes pwm to "predictedmotif.txt" refer to instruction doc


