import os
import random

def genRandBase():
	bases = ['A','T','G','C']
	return random.choice(bases)


#check filename, then make directory if it doesnt exist 
def create_dir(newpath):
	if not os.path.exists(newpath): os.makedirs(newpath)

#makes k dirs with the given parameters
def dir_params(ML,NM,SC,k):
	for run in range(0,k):
		create_dir("data/set_"+str(ML)+"_"+str(NM)+"_"+str(SC)+"/_"+str(run)) 

#specifies the different data directories for each of the paramter sets
def make_subdirs():
	create_dir("data")
	dir_params(8,1,10,10)
	dir_params(8,0,10,10)
	dir_params(8,2,10,10)
	dir_params(6,1,10,10)
	dir_params(7,1,10,10)
	dir_params(8,1,5,10)
	dir_params(8,1,20,10)
	
#makes SC sequences of length SL by repeatedly generating a uniform random base
def make_seqs(SL, SC):
	output = []	
	for x in range(0,SC):
		this_seq = ""
		for j in range(0,SL):
			this_seq += genRandBase()	
		output.append(this_seq)

	return output

#determines variable positions then makes a motif with uniform bases except * at the variables ones
def gen_motif(ML,NM):
	output = ""
	inputs = range(ML)
	stars = []
	count = 0
	while (count< NM):
		tempStar = random.choice(inputs)
		stars.append(tempStar)
		inputs.remove(tempStar)		
		count+=1

	for x in range(0,ML):
		if (x in stars):
			output+= '*'
			
		else:
			output += genRandBase()
	return output

#places motif at a random postion in a sequence
def gen_bind_sites(motif,SC):
	output = []
	for x in range(0,SC):
		temp = ""
		for pos in list(motif):
			if (pos == '*'):
				temp +=genRandBase()
			else: 
				temp += pos
		output.append(temp)
	return output	

#choses bind sites in same order as seqs
#output is (sequence with implant, start location of implant) tuple array
def genBoundSeqs(seqs, bind_sites, ML, SL):
	output = []
	for x in range(len(seqs)):
		pos = random.randint(0,SL-ML)
		output.append((seqs[x][0:pos] + bind_sites[x] + seqs[x][pos+ML:],pos))
	return output

#pass in params to generate all the sequences and files for those params
def generator(ML,NM,SL,SC):
	pDir = "data/set_"+str(ML)+"_"+str(NM)+"_"+str(SC)
	for run in range(0,10):
		subDir = pDir + "/_"+str(run) + "/" 
		seqs = make_seqs(SL,SC)		#array of strings
		motif = gen_motif(ML,NM)	#string
		bind_sites = gen_bind_sites(motif,SC)	#array of strings
		boundSeqs = genBoundSeqs(seqs, bind_sites, ML, SL)	#array of (string, int) tuples
		
		fo = open(subDir + "motiflength.txt",'w')
		fo.write(str(ML))
		fo.close()

		fo = open(subDir + "motif.txt",'w')
		fo.write("MOTIF1	" + str(ML) +   "	"+ motif)
		fo.close()

		fo = open(subDir + "sites.txt",'w')
		for x in boundSeqs:
			fo.write(str(x[1])+"\n")
		fo.close()

		fo = open(subDir + "sequences.fa",'w')
		for x in boundSeqs:
			fo.write(">Sequence1\n")
			fo.write(x[0] + "\n")
		fo.close()

if __name__ == "__main__":
	print "hello generator"
	make_subdirs()
	generator(8,1,500,10)
	generator(6,1,500,10)
	generator(7,1,500,10)
	generator(8,0,500,10)
	generator(8,2,500,10)
	generator(8,1,500,5)
	generator(8,1,500,20)
	print "done generating"









