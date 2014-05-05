import csv

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
    
#returns array of pwm rows which are arrays of floats
#incorporates laplace correction to k-l div
def readPWM(fileName): 
	rows = []
	with open(fileName,'r') as f:
		next(f)
		reader=csv.reader(f,delimiter='\t')
		for row in reader:
			tot = 0
			temp = []
			if ('<' in row):
				break
			for element in row[:-1]:
				tot = tot + float(element) + 1
			rows.append([(float(element)+1)/tot for element in row[:-1]] )
	return rows
