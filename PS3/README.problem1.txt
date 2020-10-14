COMPSCI 260 - Problem Set 3, Problem 1
Due: Fri 11 Oct 2019, 5pm

Name: Kyle Mitra
NetID: km423

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): Office Hours / StackOverflow

My solutions and comments for this problem are below.
-----------------------------------------------------
a) C = (RL)/G

b) The probability of not a specific location in the genome not being covered is
	[1 - (C/R)]^R 	which simplifies to 	e^(-C)
From this probability, the expected number of unsequenced nucleotides is G * e^(-C)

c) The expected number of contigs is R * e^(-C).
The expected length of each contain is (G[1-e^(-C)])/(R*e^(-C))