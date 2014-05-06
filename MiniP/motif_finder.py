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
        #   - sequences
        #   - motifLength
        #   - lengthOfSequences
        #   - numberOfSequences
        #   - unchosenSequences 
        #   - unchosenPositions
        #   - possibleMotifPositions
        #   - initialSequence
        globals.initialize(sequences, motifLength)

        # choose a random motif position for each unchosen sequence
        positions = chooseMotifPositions()

        # initialize global position variable
        #   - unchosenPositions
        globals.initializePositions(positions)

        # initialize iteration variables
        profileMatrix = []
        probabilityMatrix = []
        positionWeights = []
        normalizedPositionWeights = []
        iterations = 5

        for iteration in range(0, iterations):
                for x in range(0, len(sequences)):
                        # count residue occurences for each position for all unchosen sequences
                        profileMatrix = profile_matrix.createProfileMatrix()

                        # determine frequency and background frequency for each of the residue occurences
                        probabilityMatrix = probability_matrix.createProbabilityMatrix(profileMatrix)

                        # calculate weight for each possible motif position in the chosen sequence
                        positionWeights = position_weights.calculatePositionWeights(probabilityMatrix)

                        # normalize position weights
                        normalizedPositionWeights = position_weights.normalizePositionWeights(positionWeights)
                        
                        # randomly choose position based on normalized probabilities
                        positions[x] = position_weights.choosePosition(normalizedPositionWeights)
        
                        nextIteration(positions, x + 1)
                reset()
        return [positions, profileMatrix]

def chooseMotifPositions():
        positions = []
        for x in range(0, globals.numberOfSequences): 
                positions.append(random.randint(0, globals.lengthOfSequences - globals.motifLength))
        return positions

def nextIteration(positions, x):
    if x < len(globals.sequences):
        globals.initialSequence = globals.sequences[x]
        sequencesCopy = list(globals.sequences)
        del sequencesCopy[x]
        globals.unchosenSequences = sequencesCopy
        globals.unchosenPositions = list(positions)
        del globals.unchosenPositions[x]
    return

def reset():
    globals.unchosenSequences = globals.sequences[1:len(globals.sequences)]
    globals.initialSequence = globals.sequences[0]
    return

        
if __name__ == "__main__":
	print "running motif finder..."

        # create array of motif length text files
        motifLengthFiles = directory.getFiles('motiflength.txt')
        sequencesFiles = directory.getFiles('sequences.fa')

        # iterate over arrays 
        for x in range(0, len(motifLengthFiles)):
                sequencesFile = sequencesFiles[x]
                motifLengthFile = motifLengthFiles[x]
                sequences = reader.readFastaFile(sequencesFile)
                motifLength = reader.readMotifLengthFile(motifLengthFile)
                output = findMotif(sequences, motifLength)
                writer.writePredictions(output, sequencesFile, motifLength)

        print "motif finder complete"


                
        

#for each of the 70 subdirectories does the following
#reads in motiflength.txt and sequences.fa
#performs motif finding algorith on input to generate pwm, and find binding site in each sequence
#
#writes predicted location of binding site in each sequence to "predictedsites.txt" (format tbd, same as sites.txt)
#writes pwm to "predictedmotif.txt" refer to instruction doc


