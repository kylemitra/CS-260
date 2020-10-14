COMPSCI 260 - Problem Set 7, Problem 2
Due: Fri 6 Dec 2019, 5pm

Name: Kyle Mitra
NetID: km423

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): None

My solutions and comments for this problem are below.
-----------------------------------------------------
a) See Code

b) First Ten Segments:
{'start': 1, 'end': 13558, 'state': 'state1'}
{'start': 13559, 'end': 13667, 'state': 'state2'}
{'start': 13668, 'end': 31086, 'state': 'state1'}
{'start': 31087, 'end': 31120, 'state': 'state2'}
{'start': 31121, 'end': 33377, 'state': 'state1'}
{'start': 33378, 'end': 33409, 'state': 'state2'}
{'start': 33410, 'end': 33653, 'state': 'state1'}
{'start': 33654, 'end': 33682, 'state': 'state2'}
{'start': 33683, 'end': 37430, 'state': 'state1'}
{'start': 37431, 'end': 37466, 'state': 'state2'}

Last Ten Segments:
{'start': 1622883, 'end': 1622975, 'state': 'state2'}
{'start': 1622976, 'end': 1626993, 'state': 'state1'}
{'start': 1626994, 'end': 1627036, 'state': 'state2'}
{'start': 1627037, 'end': 1627041, 'state': 'state1'}
{'start': 1627042, 'end': 1627043, 'state': 'state2'}
{'start': 1627044, 'end': 1637000, 'state': 'state1'}
{'start': 1637001, 'end': 1637053, 'state': 'state2'}
{'start': 1637054, 'end': 1659452, 'state': 'state1'}
{'start': 1659453, 'end': 1659521, 'state': 'state2'}
{'start': 1659522, 'end': 1664970, 'state': 'state1'}

c) Using the posterior code, there appears to be 183 structural RNA regions now. These regions appear to be smaller in length and more precise. Compared to the positions of the transfer RNA genes, the start and end positions of the 'state2' regions of these genomes are still not exact but remain relatively close to the positions of the tRNAs listed in the .txt file.

d) The posterior decoder picked up nearly 3x more structural RNA regions than the Viterbi decoder did. The regions of the posterior decoder were shorter in length and more precise, sometimes picking up 2 separate 'state2' regions in areas where the Viterbi coder only detected a single 'state2' region. Compared to the tRNA locations in the .txt file, the corresponding 'state2' locations were more accurate in the posterior decoder than the Viterbi decoder. This observations indicate that the posterior decoder seems to work better overall. It is able to pick up small regions of states and identify more state changes. The start and end locations of these regions are more precise. When trying to complete a task such as identify the location of tRNAs (if not given the locations in a .txt file), the posterior decoder would be more useful and provide more accurate results than the Viterbi decoder. 



