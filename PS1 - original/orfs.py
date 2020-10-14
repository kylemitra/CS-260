'''
@author:
@date:

@note:

'''


from compsci260lib import *   # this will also import the sys and re modules


def solve_orfs():
    """Your code goes here..."""


def summarize_orfs(orfs):
    """Summarize ORFs identified from the find_orfs procedure as a count of the
    number of found orfs and the average length of the found ORFs (in amino
    acids)

    Args:
        orfs (list): a list of dictionaries of found ORFs

    Returns:
         tuple: (The number of ORFs found (int), Average ORF length (float))
    """

    #
    # Your code here
    #

    return (None, None)  # replace with the tuple described above


def find_orfs(seq, min_length_aa=0, is_double_stranded=False,
              is_circular=False):
    """This is a function for finding sufficiently long ORFs in all reading
    frames in a sequence of DNA or RNA.  By default, the sequence is assumed
    to be single-stranded, but if you call this function with
    is_double_stranded = True, it will look for ORFs on both strands.

    The function takes as input parameters: a string representing a genomic
    sequence, the minimum length (in amino acids) for an ORF before it will be
    returned (which defaults to 0), whether the sequence should be considered
    double-stranded, and whether the sequence is circular (like a plasmid).

    The last two parameters default to False; so if default values are used,
    the function will assume a single-stranded linear sequence.

    Args:
        seq (str): a genomic sequence
        min_length_aa (int): minimum length of found ORFs in amino acids
        is_double_stranded (bool): whether the sequence should be considered
                                   double-stranded
        is_circular (bool): whether the sequence is circular (like a plasmid)

    Returns:
        list: of dictionaries with information on each ORF found.

    Where each ORF found is represented by a dictionary with
    the following keys:
        frame (int): The nucleotide offset in which the ORF was found. (Must be
        0, 1, or 2)
        stop (int): the nucleotide position of the end of the ORF
        start (int): the nucleotide position of the start of the ORF
        stopcodon (str): the nucleotide triplet of the stop codon
        nlength (int): the length (in nucleotides) of the ORF

    A valid return list may look something like this:
    [
        {
            'frame': 0,
            'stop': 13413,
            'aalength': 4382,
            'start': 265,
            'stopcodon': 'UAA',
            'nlength': 13149
        },
        {
            'frame': 0,
            'stop': 27063,
            'aalength': 221,
            'start': 26398,
            'stopcodon': 'UAA',
            'nlength': 666
        }
    ]
    """

    #
    # Your code here
    #

    return []


if __name__ == '__main__':
    solve_orfs()
