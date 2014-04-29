import os
import random



def genRandBase():
	bases = ['A','T','G','C']
	return random.choice(bases)


#check filename 
def create_dir(filename):
	d = os.path.dirname(filename)
	try:
   		os.stat(d)
	except:
  		os.mkdir(d) 


if __name__ == "__main__":
	print "hello generator"





	
#create a directory /data/
#create 10 subidrectories of /data/ for each param list wiht format /data/set_$ML_$NM_$SC/_$run 	(example: /data/set_8_1_10/_3 ) 
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







