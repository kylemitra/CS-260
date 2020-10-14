COMPSCI 260 - Problem Set 7, Problem 3
Due: Fri 6 Dec 2019, 5pm

Name: Kyle Mitra
NetID: km423

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): None

My solutions and comments for this problem are below.
-----------------------------------------------------
a)
Number of Reads: 244 Mated Pairs of Reads (488 Reads Total)
Average Length: 2000 +/- 10 (1995, 2002)
Random Fragments sequenced an average of 500 BPs from both ends of the DNA sequencer
Coverage is 7
	- Coverage = RL/ G
	- 7 = (488)(2000) / G
	- G = 13942.857

Estimation of the length of the original cloned chromosomal region that is about to be assembled: ~13943

Estimation of the number of gaps that are expected to remain after assembly: 
The expected number of unsequenced nucleotides that remain after assembly is Ge^-C.
In this case, since G is about 13943 and C is 7, we get that the estimated number of gaps is about 12.714 or about 13 gaps.

b)
It is possible to estimate the length of a gap by using mated pairs of reads. Since gaps are bridged by mated pairs of reads, we can use mated pairs which reside on both contigs to estimate the length of the gap, since we know that only one gap exists between the two given contigs. We use the distance between the two contigs to get the estimate of the gap distance. 

c) SEE CODE

d) This read is not anywhere in the set of contigs: seq244.
seq244 is the read which doesn't not belong in the assembly.

e) 

There are 11 reads where one mate maps to contig0 and the other maps to contig1.
The possible length of the gap between the two contigs is between 918-922. 

f)
Based on the previous problem, the size of the gap length that exists between the two contigs is approximately the average of these lengths. 
Average = Sum of the length list / size of the length list.
This gave a value of 920.27 so the size is about 920 nucleotides. 

g) The GENSCAN HMM is not constrained to start in the state corresponding to the background nucleotide distribution (state N) but can start in any state (i.e. the initial probability of every state is nonzero). This fact is relevant for the specific assembled sequence since in a circular genome, there is no identified start location, so it is important that the results will be the same no matter where in the assembly you start. 

h)
SEE genscan.contig0.txt and genscan1.txt.

i) 
The GENSCAN output indicates the predicted locations of different genes and exons. 

j) 
K, the total number of protein-coding genes predicted by GENSCAN is 5 unique ones and 11 total ones (including repeats).
There are a total 11 total exons predicted, one for each of the k predicted genes.


SEE peptides.fasta

k) The predicted number of exons is typical of genes in the human genome since they are equal to the number of protein-coding genes.

l) 
For contig0:
The fist peptide is 60S ribosomal protein L23a
The second is Histone H2A type 3
The third is Histone H2B type 3-B

For contig1:
The peptide is Histone H3.1t

Given what we know these genes are from the human genome, these results are believable.
The peptide sequences which represent full-length proteins are the contig1 peptide sequence (Histone H3.1t), the third contig0 peptide (Histone H2B type 3-B), and the second contig0 peptide (Histone H2A type 3). The first contig0 peptide (60S ribosomal protein L23a) represents a fragment. The fragmented peptide means that part of the sequence lies in the gap between the two contains while the complete peptides reside solely on a single contig.

m) All of the three matching proteins are histones. Histones are a family of basic proteins that associate with DNA in the nucleus and help condense it into chromatin.


