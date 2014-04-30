import sys
#import reader
#import writer
from os import listdir
from os.path import isfile, join

if __name__ == "__main__":
	print "hello motif"
        directoryPath = "./data/"
        dataFiles = [ files for file in listdir(directoryPath) if isfile(join (mypath, f)) ]
        print dataFiles
        #fastaFile = readers.readFastaFile(fastaFileName)
        #motifLength = readers.readMotifLengthFile(motifLengthFileName)
        #motifs = findMotifs(fastaFile, motifLength)
        

#for each of the 70 subdirectories does the following
#reads in motiflength.txt and sequences.fa
#performs motif finding algorith on input to generate pwm, and find binding site in each sequence
#
#writes predicted location of binding site in each sequence to "predictedsites.txt" (format tbd, same as sites.txt)
#writes pwm to "predictedmotif.txt" refer to instruction doc


