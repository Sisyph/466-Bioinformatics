def readFastaFile(fileName):
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

def readMotifLengthFile(fileName):
    handle = open(fileName)
    line = handle.readline()
    return line
    
    
