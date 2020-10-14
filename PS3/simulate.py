import math
import sys
import random
from compsci260lib import *
from math import exp

def simulate():
    """YOUR CODE GOES HERE..."""
    """Have to Set values equal to those in part e"""
    valG = 3 * 10**6 #length of DNA segment in number of bases
    G = [0] * valG #List of zeroes for each nucleotide in genome
    R = 4 * 10**4 #number of sequence reads
    L = 450 #number of nucleotides in a read (the length)

    C = (R*L)//valG
    probNotCovered = math.exp(-1*C)

    numUnseqeuncedNtides = valG*probNotCovered
    # print('Expected Ntides', numUnseqeuncedNtides)
    numContigs = R*probNotCovered
    # print('Expected Contigs', numContigs)
    lengthContigs = (valG*(1-probNotCovered))/(numContigs)
    # print('Expected Contig Length',lengthContigs)

    for i in range(0, R): # iterate through R different reads
        for j in range(1):
            starting_point = random.randint(1,valG - L + 1)
        for k in range(0,L-1):
            G[starting_point+k] += 1

    zeroCounter = 0
    contigCounter = 0
    contigLength = 0
    contigLengthList = []

    for x in range(0,valG):
        if G[x] == 0:
            zeroCounter += 1

    for y in range(0,valG-1):
        if G[y] > 0 and G[y+1] == 0:
            contigCounter += 1
        if G[valG-1] > 0:
            contigCounter += 1
        if G[y] > 0:
            contigLength += 1
        if G[y] == 0 and contigLength > 0:
            contigLengthList.append(contigLength)
            contigLength = 0
    averageContigLength = sum(contigLengthList) / len(contigLengthList)

    empiricalCoverage = sum(G) / len(G)
    print('The emperical coverage is', empiricalCoverage)
    print('The number of nucleotides not covered by any read is', zeroCounter)
    print('The number of contigs is', contigCounter)
    print('The average length of contigs is', averageContigLength)


if __name__ == '__main__':
    simulate()
