COMPSCI 260 - Problem Set 2, Problem 1
Due: Fri 27 Sep 2019, 5pm

Name: Kyle Mitra
NetID: km423

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): TA Office Hours / Piazza / Google

My solutions and comments for this problem are below.
-----------------------------------------------------
a) genome size n combinations = (4)^n
   Sequence combinations = (4)^m
   [(4^n)/(4^m)] = total number of expected occurrences.

b) A brute force algorithm to map a read to a reference genome would begin by first identifying the complement nucleotide sequence of the read. A read is matched to a reference genome by aligning itself with the respective nucleotide complement for each base pair in the read sequence. The optimal solution would be to simply identify this complement sequence on the reference genome but there lies a possibility for mismatches. Therefore, you want to identify the best possible match for the read even if there is no perfect one. A brute force algorithm would run through every possible sequence from a single base pair match to an entire sequence match. It would start at matching one base pair, then see if there is somewhere where there are two base pairs which match, then three, and so on. At a certain point, the algorithm will not be able to determine a better match in the sequence so it will return the best match it found. There are also the possibility of gaps between base pair matches (for example, the first four bases and another 8 bases in the middle may match) and therefore, you need to check every single possible matching combination. This brute force algorithm will take at worst O(n*m) time is m is the length of the read sequence and n is the length of the of the genome. 


c) When the number of reads (k) times the length of the reads (m) exceeds the length of the genome (n) then it would be worth it to adopt the pre-process approach to the genome. However, a tradeoff of using this pre-processing approach does not let you identify the best pairing possibility as it is only querying the genome for an exact match of the complement sequence. The brute force method is able to identify the best match possible even when a perfect match does not exist. This can be useful due to the potential of mistakes in reading in the genome. For a lengthly read, if there is a potential match that is off by only one base pair, you can possibly identify an issue with the genome you read in, if you are expecting there to be a match. However, a pre-processing approach would not be able to provide you any information about this potential match.

