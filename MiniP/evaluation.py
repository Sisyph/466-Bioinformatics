import directory
import reader
import math

#returns array of ints which is the sites in a given site file
def fileToSites( siteFile):
	out = []
	fo = open(siteFile)
	done = False
	while (not done):
		line = fo.readline()
		if (line == ""):
			done = True
		else:
			out.append(int(line))
	fo.close()
	return out

#doesnt work unless there are same num of site and predicted site files
def siteOverlap(sitesFiles, predSitesFiles):
#	if (len(sitesFiles) != len(predSitesFiles)):
#		print "site/pred sites length mismatch"
#		return -1
	output = []
	for y in range(0,7):
		count = 0	
		for x in range(0,10 ):
			try:
				preds = fileToSites(predSitesFiles[y*10 + x])	#array of ints
				sites = fileToSites(sitesFiles[y*10 + x])	
				for itr in preds:
					if (itr in sites):
						count += 1

			except IndexError:
				count += 0
		output.append((sitesFiles[y*10],count/10))
	return output

#
def computeEntropy(motifFiles, predMotifFiles):
	output = []
	for y in range(0,7):	
		for x in range(0,10 ):
			try:
				predPWM = reader.readPWM(predMotifFiles[y*10 + x])	#array of floats
				motifPWM = motifToPWM(motifFiles[y*10 + x])	
				output.append((motifFiles[y*10 + x], relEntropy(predPWM , motifPWM)))
			except IndexError:
				output.append(("Bad Input", -1.0))
				output.append(("Bad Input", -1.0))
	return output

#input file containing motif ie: "ACG*C*G", output array of rows of pwm
#incorporates laplace correction to k-l div
def motifToPWM(motifFile):
	output = []
	handle = open(motifFile)
	line = handle.readline()
	for x in list(line):
		if (x == 'A'):
			output.append( (.9970,0.000996,.000996,.000996) )
		elif (x == 'T'):
			output.append( (.000996,.99700,.000996,.000996) )
		elif (x == 'G'):
			output.append( (.000996,.000996,.9970,.000996) )
		elif (x == 'C'):
			output.append( (.000996,0.000996,.000996,.9970) )
		elif (x == '*'):
			output.append( (0.250,0.250,0.250,0.250) )
	return output

#takes 2 arays of arrays of floats representing pwms
#returns float
def relEntropy(motif1, motif2):
	output = 0.0 
	try:
		for i in range(0, len(motif1)):
			for j in range(0,4):
				try:
					output = output + motif1[i][j] * math.log(motif1[i][j] / motif2[i][j])
				except ZeroDivisionError:
					output += 0
	except IndexError:
		output = -100.54	
	return output

if __name__ == "__main__":
	print "hello evaluation"
	predMotifFiles = directory.getFiles('predictedmotif.txt')	#array of file names
        motifFiles = directory.getFiles('motif.txt')
	entropy_result = computeEntropy(motifFiles, predMotifFiles)

	fo = open('entropy_output.txt','w')
	for x in entropy_result:
		fo.write("" +x[0]+','+str(x[1]) +"\n")
	fo.close()

	sitesFiles = directory.getFiles('sites.txt') 
	predSitesFiles = directory.getFiles('predictedsites.txt')
	site_result = siteOverlap(sitesFiles,predSitesFiles)

	fo = open('site_output.txt','w')
	for x in site_result:
		fo.write("" +x[0]+','+str(x[1]) +"\n")
	fo.close()

	print "evaluation finished"

#for each of the 70 subdirectories
#compute the metrics
#perhaps generate graphs, though this could be done externally if the metrics are output to csv or similar
