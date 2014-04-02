import sys
import random

def SimpleFastaParser(fileName):
    handle = open(fileName)
    line = handle.readline()
    while True:
        title = line[1:].rstrip()
        lines = ""
        line = handle.readline()
        while True:
            if not line:
                break
            if line[0] == ">":
                break
            lines += line.rstrip()
            line = handle.readline()
        if not line:
            return lines

def countOccurences(sequence, word):
    count = sequence.count(word, 0, len(sequence))
    return count

def countOccurencesIn1000Permutations(sequence, word):
    # get count of each nucleotide in sequence
    aCount = sequence.count('A', 0, len(sequence))
    tCount = sequence.count('T', 0, len(sequence))
    cCount = sequence.count('C', 0, len(sequence))
    gCount = sequence.count('G', 0, len(sequence))
    
    # get first permutation of sequence
    permutation = getPermutation(aCount, tCount, cCount, gCount)

    # count occurences of word in permutations
    count = []
    numberOfPermutations = 0
    while numberOfPermutations < 1000:
        count.append(countOccurences(permutation, word))
        numberOfPermutations += 1
        permutation = getPermutation(aCount, tCount, cCount, gCount)

    # return list of occurences in each permutation
    return count

def getPermutation(aCount, tCount, cCount, gCount):
    permutation = ""
    while aCount > 0 or tCount > 0 or cCount > 0 or gCount > 0:
        randomNumber = random.randrange(1, 5)
        if aCount > 0 and randomNumber == 1:
            permutation += 'A'
            aCount += -1
        elif tCount > 0 and randomNumber == 2:
            permutation += 'T'
            tCount += -1
        elif cCount > 0 and randomNumber == 3:
            permutation += 'C'
            cCount += -1
        elif gCount > 0 and randomNumber == 4:
            permutation += 'G'
            gCount += -1
    return permutation

def calculatePValue(originalCount, permutationCountList):
    count = 0
    for permutationCount in permutationCountList:
        if permutationCount >= originalCount:
            count += 1
    pValue = count / 1000.0
    return pValue

if __name__ == "__main__":
    fastaFileName = sys.argv[1]
    word = sys.argv[2]

    sequence = SimpleFastaParser(fastaFileName)
    print "Length of sequence = " + str(len(sequence))

    originalCount = countOccurences(sequence, word)
    print "N = " + str(originalCount)

    permutationCountList = countOccurencesIn1000Permutations(sequence, word)
    pValue = calculatePValue(originalCount, permutationCountList)
    print "p-value = " + str(pValue)
