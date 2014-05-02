# python packages
import random

# original packages
import globals
import directory
import reader
import profile_matrix
import probability_matrix

def findMotif(sequences, motifLength):
        # declare and set the following global variables:
        #   - sequences
        #   - motifLength
        #   - lengthOfSequences
        #   - numberOfSequences
        #   - unchosenSequences 
        #   - possibleMotifPositions
        #   - initialSequence variables
        globals.initialize(sequences, motifLength)

        # choose a random motif position for each unchosen sequence
        initialPositions = chooseMotifPositions()

        # count residue occurences for each position for all unchosen sequences
        profileMatrix = profile_matrix.createProfileMatrix(sequences[1:(globals.numberOfSequences - 1)], initialPositions)

        # determine frequency and background frequency for each of the residue occurences
        probabilityMatrix = probability_matrix.createProbabilityMatrix(profileMatrix)

        # calculate weight for each possible motif position in the chosen sequence
        positionWeights = probability_matrix.calculatePositionWeights(probabilityMatrix)

        # normalize position weights
        # randomly choose position based on normalized probabilities

        # ???

        # write to predictedmotif.txt

        return

def chooseMotifPositions():
        positions = []
        for x in range(1, globals.numberOfSequences + 1): 
                positions.append(random.randint(0, globals.lengthOfSequences - globals.motifLength))
        return positions

        
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
                        break
                break

                
        

#for each of the 70 subdirectories does the following
#reads in motiflength.txt and sequences.fa
#performs motif finding algorith on input to generate pwm, and find binding site in each sequence
#
#writes predicted location of binding site in each sequence to "predictedsites.txt" (format tbd, same as sites.txt)
#writes pwm to "predictedmotif.txt" refer to instruction doc


