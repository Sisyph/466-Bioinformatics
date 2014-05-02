def readFastaFile(fileName):
    handle = open(fileName)
    line = handle.readline()
    lines = []
    while True:
        line = handle.readline()
        while True:
            if not line:
                break
            if line[0] == ">":
                break
            lines.append(line.rstrip())
            line = handle.readline()
        if not line:
            return lines

def readMotifLengthFile(fileName):
    handle = open(fileName)
    line = int(handle.readline())
    return line
    
    
