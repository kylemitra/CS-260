COMPSCI 260 - Problem Set 7, Problem 1
Due: Fri 6 Dec 2019, 5pm

Name: Kyle Mitra
NetID: km423

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): None

My solutions and comments for this problem are below.
-----------------------------------------------------
a) See Code

b) Output of count_segments for artificial.genome:
{'state1': 11, 'state2': 11}
Output of count_segments for bacterial.genome:
{'state1': 68, 'state2': 67}

c) 
First Ten Segments:
{'start': 1, 'end': 13562, 'state': 'state1'}
{'start': 13563, 'end': 13667, 'state': 'state2'}
{'start': 13668, 'end': 31086, 'state': 'state1'}
{'start': 31087, 'end': 31120, 'state': 'state2'}
{'start': 31121, 'end': 33653, 'state': 'state1'}
{'start': 33654, 'end': 33682, 'state': 'state2'}
{'start': 33683, 'end': 97326, 'state': 'state1'}
{'start': 97327, 'end': 97542, 'state': 'state2'} *
{'start': 97543, 'end': 97627, 'state': 'state1'}
{'start': 97628, 'end': 97716, 'state': 'state2'} *

Last Ten Segments:
{'start': 1410405, 'end': 1410468, 'state': 'state2'}
{'start': 1410469, 'end': 1525012, 'state': 'state1'}
{'start': 1525013, 'end': 1525081, 'state': 'state2'}
{'start': 1525082, 'end': 1553925, 'state': 'state1'}
{'start': 1553926, 'end': 1553982, 'state': 'state2'}
{'start': 1553983, 'end': 1622881, 'state': 'state1'}
{'start': 1622882, 'end': 1622974, 'state': 'state2'}
{'start': 1622975, 'end': 1659453, 'state': 'state1'}
{'start': 1659454, 'end': 1659521, 'state': 'state2'}
{'start': 1659522, 'end': 1664970, 'state': 'state1'}

d) With the Viterbi decoder, there appears to be 67 structural RNA regions. After analyzing the transfer RNA gene locations in the tRNA.locations.txt file, I was able to identify that all the tRNA regions given in the .txt file were areas in the bacterial genome that corresponded to 'state2', as expected. However, the start and end positions learned by the Viterbi decoder were not as precise as the ones given in the .txt file as they often included additional nucleotides beyond the start and end locations given of the tRNAs in the .txt file.
