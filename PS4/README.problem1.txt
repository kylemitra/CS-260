COMPSCI 260 - Problem Set 4, Problem 1
Due: Fri 25 Oct 2019, 5pm

Name: Kyle Mitra
NetID: km423

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): None

My solutions and comments for this problem are below.
-----------------------------------------------------
a) See attached

b) The score of an optimal alignment is -2. 
There are 5 different alignments that achieve this score.
The set of optimal alignments is as follows:
[
_ _ _ T A G T A, 
T _ A _ _ G T A,
T A _ _ _ G T A,
_ T A _ _ G T A,
T A G T _ _ _ A
]

c) If an affine gap score was used instead of a linear gap score, the 2nd alignment listed (T _ A _ _ G T A) would no longer be optimal because it opens 2 different gaps compared to the other optimal alignments which only open one continuous gap. Since you have to pay a gap opening penalty in an affine gap score, you want to minimize the number of different gaps present so, the 2nd solution would no longer be optimal. 