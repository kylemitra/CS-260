'''
@author: Kyle Mitra
@date: 9/26/19

@note:

'''

from compsci260lib import *

from pprint import *

def solve_pebble(grid_file):
    """Code for the "Pebble Beach" problem. This problem involves implementing
    an O(n) dynamic programming algorithm for computing the maximum value of
    the placement of pebbles under the constraint that no pebbles can be
    vertically or horizontally adjacent.

    Args: grid_file (str): a string with the name of the file that contains
          the grid of values. Each line of that file should contain a row
          of four integers, separated by tabs

    Returns: the maximal score for the optimal pebble placements
    """

    """Your code goes here..."""

    #  Return the maximum value of the placement of pebbles
    gridInfo = open(grid_file, "r")
    gridInfo = gridInfo.readlines()
    i = 0
    newGridInfo = []
    for i in range (0,len(gridInfo)):
        newGridInfo.append(gridInfo[i].strip().split())
    for i in range (0,len(gridInfo)):
        newGridInfo[i][0] = int(newGridInfo[i][0])
        newGridInfo[i][1] = int(newGridInfo[i][1])
        newGridInfo[i][2] = int(newGridInfo[i][2])
        newGridInfo[i][3] = int(newGridInfo[i][3])
    numRows = len(open(grid_file).readlines())
    numCols = int(len(open(grid_file).read().split()) / numRows)
    numPebbles = numRows * 2

    combo1 = []
    combo2 = []
    combo3 = []
    combo4 = []
    combo5 = []
    combo6 = []
    combo7 = []
    combo8 = []

    for i in range (0,numRows):
        combo1.append(calcsum(newGridInfo,i,1))
        combo2.append(calcsum(newGridInfo,i,2))
        combo3.append(calcsum(newGridInfo,i,3))
        combo4.append(calcsum(newGridInfo,i,4))
        combo5.append(calcsum(newGridInfo,i,5))
        combo6.append(calcsum(newGridInfo,i,6))
        combo7.append(calcsum(newGridInfo,i,7))
        combo8.append(calcsum(newGridInfo,i,8))

    maxVal = []
    maxVal.append(max(combo1[0], combo2[0], combo3[0], combo4[0], combo5[0], combo6[0], combo7[0], combo8[0]))
    for i in range (0, (numRows-1)):
        if maxVal[i] == combo5[i]:
            maxVal.append(max(combo2[(i+1)], combo4[(i+1)], combo6[(i+1)], combo8[(i+1)]))
        elif maxVal[i] == combo6[i]:
            maxVal.append(max(combo1[(i+1)], combo3[(i+1)], combo5[(i+1)], combo8[(i+1)]))
        elif maxVal[i] == combo7[i]:
            maxVal.append(max(combo2[(i+1)], combo3[(i+1)], combo8[(i+1)]))
        elif maxVal[i] == combo1[i]:
            maxVal.append(max(combo2[(i+1)], combo3[(i+1)], combo4[(i+1)], combo6[(i+1)], combo8[(i+1)]))
        elif maxVal[i] == combo2[i]:
            maxVal.append(max(combo1[(i+1)], combo3[(i+1)], combo4[(i+1)], combo5[(i+1)], combo7[(i+1)], combo8[(i+1)]))
        elif maxVal[i] == combo3[i]:
            maxVal.append(max(combo1[(i+1)], combo2[(i+1)], combo4[(i+1)], combo6[(i+1)], combo7[(i+1)], combo8[(i+1)]))
        elif maxVal[i] == combo4[i]:
            maxVal.append(max(combo1[(i+1)], combo2[(i+1)], combo3[(i+1)], combo5[(i+1)], combo8[(i+1)]))
        elif maxVal[i] == combo8[i]:
            maxVal.append(max(combo1[(i+1)], combo2[(i+1)], combo3[(i+1)], combo4[(i+1)], combo5[(i+1)], combo6[(i+1)], combo7[(i+1)], combo8[(i+1)]))
    print(maxVal)

    bestScore = 0
    for j in range (0, (len(maxVal)-1)):
        bestScore = bestScore + maxVal[j]
    print(bestScore)
    return bestScore

def calcsum(A,i,b):
    #A is the input data
    #i is number of rows
    if b == 1:
        return A[i][0]
    elif b == 2:
        return A[i][1]
    elif b == 3:
        return A[i][2]
    elif b == 4:
        return A[i][3]
    elif b == 5:
        return A[i][0] + A[i][2]
    elif b == 6:
        return A[i][1] + A[i][3]
    elif b == 7:
        return A[i][0] + A[i][3]
    elif b == 8:
        return 0


if __name__ == '__main__':
    max_score = solve_pebble('grid.txt')
    print("The max score for this grid is %d" % max_score)
