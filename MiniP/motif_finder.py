# python packages
import random

# original packages
import directory
import reader
#import writer
import profile_matrix
import probability_matrix


def findMotif(sequences, motifLength):
        lengthOfSequences = len(sequences[0])
        numberOfSequences = len(sequences)

        # choose a sequence for sampling
        initialSequence = sequences[0]
        
        # choose a random motif position for each unchosen sequence
        initialPositions = chooseMotifPositions(lengthOfSequences, numberOfSequences, motifLength)

        # count residue occurences for each position for all unchosen sequences
        profileMatrix = profile_matrix.createProfileMatrix(sequences[1:(numberOfSequences - 1)], motifLength, initialPositions)

        # determine frequency and background frequency for each of the residue occurences
        probabilityMatrix = probability_matrix.createProbabilityMtarix()

        

        profileMatrix = profile_matrix.calculateProfileMatrix(motifLength, sequences, initialPositions)

def chooseMotifPositions(lengthOfSequences, numberOfSequences, motifLength):
        positions = []
        for x in range(1, numberOfSequences): 
                positions.append(random.randint(0, lengthOfSequences - motifLength))
        return positions
                
        
        

        
        
if __name__ == "__main__":
	print "running motif_finder.py..."

        # create array of motif length text files
        motifLengthFiles = directory.getFiles('*.txt')
        sequencesFiles = directory.getFiles('*.fa')
        chooseMotifPositions(5, 6)

        # iterate over arrays 
        for motifLengthFile in motifLengthFiles:
                motifLength = reader.readMotifLengthFile(motifLengthFile)
                for sequencesFile in sequencesFiles:
                        sequences = reader.readSequencesFile(sequenceFile)
                        findMotif(sequences, motifLength)

                
        

#for each of the 70 subdirectories does the following
#reads in motiflength.txt and sequences.fa
#performs motif finding algorith on input to generate pwm, and find binding site in each sequence
#
#writes predicted location of binding site in each sequence to "predictedsites.txt" (format tbd, same as sites.txt)
#writes pwm to "predictedmotif.txt" refer to instruction doc


