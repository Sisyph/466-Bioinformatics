def initialize(listOfStrings, integer):
    global sequences
    global motifLength
    global lengthOfSequences
    global numberOfSequences
    global unchosenSequences
    global possibleMotifPositions
    global initialSequence
    sequences = listOfStrings
    motifLength = integer
    lengthOfSequences = len(sequences[0])
    numberOfSequences = len(sequences)
    unchosenSequences = numberOfSequences - 1
    possibleMotifPositions = lengthOfSequences - motifLength + 1
    initialSequence = sequences[0] 
    return
