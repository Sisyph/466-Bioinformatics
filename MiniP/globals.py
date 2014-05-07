def initialize(_sequences, _motifLength):
    global sequences
    global motifLength
    global lengthOfSequences
    global numberOfSequences
    global unchosenSequences
    global possibleMotifPositions
    global initialSequence
    sequences = _sequences
    motifLength = _motifLength
    lengthOfSequences = len(_sequences[0])
    numberOfSequences = len(_sequences)
    possibleMotifPositions = lengthOfSequences - motifLength + 1
    initialSequence = sequences[0] 
    return
