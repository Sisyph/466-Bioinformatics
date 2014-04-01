def SimpleFastaParser(fileName):
    handle = open(fileName)
    line = handle.readline()
    while True:
        title = line[1:].rstrip()
        lines = []
        line = handle.readline()
        while True:
            if not line:
                break
            if line[0] == ">":
                break
            lines.append(line.rstrip())
            line = handle.readline()
            print line
        if not line:
            return

def main(argv):
    parsedFastaFile = SimpleFastaParser(fastaFileName)
    print parsedFastaFile
    return
