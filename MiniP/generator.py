import os
import random



def genRandBase():
	bases = ['A','T','G','C']
	return random.choice(bases)


#check filename 
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
	
#
def make_seqs(SL, SC):
	output = []	
	for x in range(0,SC):
		this_seq = ""
		for j in range(0,SL):
			this_seq += genRandBase()	
		output.append(this_seq)

	return output

#is biased to place stars near beginning of motif
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

#
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

#choses bind sites in same order as seqs, maybe want to randomize
def genBoundSeqs(seqs, bind_sites, ML, SL):
	output = []
	for x in range(len(seqs)):
		pos = random.randint(0,SL-ML)
		output.append(seqs[x][0:pos] + bind_sites[x] + seqs[x][pos+ML:])
	return output

#pass in params to generate all the sequences and files for those params
def generator(ML,NM,SL,SC):
	pDir = "data/set_"+str(ML)+"_"+str(NM)+"_"+str(SC)
	for run in range(0,10):
		subDir = pDir + "/_"+str(run) 
		seqs = make_seqs(SL,SC)		#array of strings
		motif = gen_motif(ML,NM)	#string
		bind_sites = gen_bind_sites(motif,SC)	#array of strings
		boundSeqs = genBoundSeqs(seqs, bind_sites, ML, SL)	#array of strings


if __name__ == "__main__":
	print "hello generator"
	make_subdirs()
	generator(8,1,50,10)

	#7 calls to generator

	
#create a directory /data/
#create 10 subidrectories of /data/ for each param list wiht 
#format /data/set_$ML_$NM_$SC/_$run 	(example: /data/set_8_1_10/_3 ) 
#do the following for each set of parameter values 10 times and put the output in appropriate folders there are 70 lowest lvl sub directories which will contain 4 files each

#generate an array SC long of sequences(strings) of length SL
#generate a motif that looks like this A*C*GGT	 , where length is ML and number of stars is NM
#generate an array SC long of binding sites(strings) that match the motif except have * replaced with random nucleotides
#loop over the sequence array, for each sequence pop a random binding site from the binding site array and overite a random location in the sequence with the binding site
#	record the location of the binding site in each sequence (format tbd)
#write out the sequence array to a fasta called "sequences.fa"
#write the location of the binding site in each sequence (format tbd) in a file called "sites.txt"
#write the motif in format "MOTIF1	 7	 A*C*GGT" to "motif.txt" see project instructions doc
#write the motif length (int) to file "motiflength.txt"
#
#
#
#
#
#







