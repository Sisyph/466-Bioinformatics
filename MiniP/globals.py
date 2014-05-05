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
    unchosenSequences = sequences[1:len(sequences)]
    possibleMotifPositions = lengthOfSequences - motifLength + 1
    initialSequence = sequences[0] 
    return

def initializePositions(_positions):
    global unchosenPositions
    unchosenPositions = _positions[1:len(sequences)]
    return
