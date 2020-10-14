COMPSCI 260 - Problem Set 2, Problem 3
Due: Fri 27 Sep 2019, 5pm

Name: Kyle Mitra
NetID: km423

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): TA Office Hours / Piazza / Google

My solutions and comments for this problem are below.
-----------------------------------------------------
a) There are 8 different patterns which pebbles can be placed in. There can be no pebbles in a row (1 total pattern). There can be one pebble in a square, for all four squares. (1 + 4 = 5 total patterns). There can be one pebble in the first square and one in the third square (6 total patterns). There can be one pebble in the first square and one in the last square (7 total patterns).

b) A dynamic programming algorithm for this problem would begin at the last row of the grid and calculate the maximum value. For the pattern which returns this maximum value, there are only a few patterns which can be used in the next row and be a valid solution. For these possible patterns, we want to return the maximum value of the patterns which work. This process will repeat itself until working its way up to the top row of the grid until the entire grid has been completed. Then all the squares with pebbles on them can be used to calculate the maximum value of the whole grid.

c) See code

d) The maximum value of the sample grid is 10275. 

e) In the diagram attached, it would be optimal solution would require you to leave the second row empty. The only possible combinations for the second row are to put a pebble in the first box or the third box but doing so will prevent you from pebbling these boxes in the next row. In this case, to yield the optimal solution, you would have to leave the second row empty.
