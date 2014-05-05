# python packages
import random

# original packages
import globals
import directory
import reader
import profile_matrix
import probability_matrix
import position_weights

def findMotif(sequences, motifLength):
        # initialize sequence and motif variables
        # declare and set the following global variables:
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

        # initialze position variable
        # declare and set the following global variables:
        #   - unchosenPositions
        globals.initializePositions(positions)

        # initialize iteration variables
        profileMatrix = []
        probabilityMatrix = []
        positionWeights = []
        normalizedPositionWeights = []
        previousPositions = []

        while True:
                for x in range(0, len(sequences)):
                        # count residue occurences for each position for all unchosen sequences
                        profileMatrix = profile_matrix.createProfileMatrix(globals.unchosenSequences, globals.unchosenPositions)

                        # determine frequency and background frequency for each of the residue occurences
                        probabilityMatrix = probability_matrix.createProbabilityMatrix(profileMatrix)

                        # calculate weight for each possible motif position in the chosen sequence
                        positionWeights = position_weights.calculatePositionWeights(probabilityMatrix)

                        # normalize position weights
                        normalizedPositionWeights = position_weights.normalizePositionWeights(positionWeights)

                        # randomly choose position based on normalized probabilities
                        positions[x] = position_weights.choosePosition(normalizedPositionWeights)
        
                        nextIteration(positions, x + 1)
                if cmp(positions, previousPositions) == 0:
                        print "SUCCESS!"
                        break
                print positions
                previousPositions = list(positions)
                reset()

        print positions                        
        return positions

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
    unchosenSequences = globals.sequences[1:len(globals.sequences)]
    initialSequence = globals.sequences[0]
    return

        
if __name__ == "__main__":
	print "running motif_finder.py..."

        # create array of motif length text files
        motifLengthFiles = directory.getFiles('motiflength.txt')
        sequencesFiles = directory.getFiles('sequences.fa')

        # iterate over arrays 
        for motifLengthFile in motifLengthFiles:
                motifLength = reader.readMotifLengthFile(motifLengthFile)
                for sequencesFile in sequencesFiles:
                        sequences = reader.readFastaFile(sequencesFile)
                        findMotif(sequences, motifLength)

                
        

#for each of the 70 subdirectories does the following
#reads in motiflength.txt and sequences.fa
#performs motif finding algorith on input to generate pwm, and find binding site in each sequence
#
#writes predicted location of binding site in each sequence to "predictedsites.txt" (format tbd, same as sites.txt)
#writes pwm to "predictedmotif.txt" refer to instruction doc


