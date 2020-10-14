'''
@author:
@date:

@note:

'''


from compsci260lib import *   # this will also import the sys and re modules


def solve_plasmid():

    # Load the plasmid reads from fasta ensuring they are
    # in the expected order to be assembled
    #
    # Your code here
    #
    reads = []

    # Assemble the reads into a single-stranded linearized version of the
    # plasmid:
    plasmid_dna = simple_assembler(reads)

    # Report the length of the assembled plasmid
    #
    # Your code here
    #

    # Search for ORFs in the reconstructed plasmid DNA
    #
    # Your code here
    #


def simple_assembler(reads):
    """Given a list of reads, as described in the problem, return an assembled
    DNA sequence, as a string. For consistency, use the first entry in the
    fragment reads list as the starting position of the returned sequence.

    For example, if we were to take in a list of three reads, 31 nucleotides
    long each. The last 15 nucleotides of each read would overlap with one
    other read, and the assembled sequence would be 48 nucleotides long with
    the sequence starting with the beginning of the first read.

    Args:
        reads (list): list of sequence strings as reads

    Returns:
         str: an assembled genomic sequence as a string starting with the first
              read in `reads`
    """

    #
    # Your code here
    #

    return ""


if __name__ == '__main__':
    solve_plasmid()
