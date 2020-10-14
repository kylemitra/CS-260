from compsci260lib import *
# Note that the '$' character will be used to designate the end of a
# given string.

def forward_bwt(seq):
    """forward_bwt(seq) takes as input a string containing the EOF character to
    which the BWT must be applied. The method should then return the result of
    the BWT on the input string.

    For example:
        forward_bwt('GATTACA$') --> 'ACTGA$TA'

    Args:
        seq (str): input string with an EOF character
    Returns:
        (str): the transformed string
    """

    # YOUR CODE GOES HERE
    """Apply Burrows-Wheeler transform to input string."""
    sortedString = sorted([seq[i:] + seq[:i] for i in range(len(seq))])
    newBWT = ''.join([row[-1] for row in sortedString])
    print(newBWT)
    return newBWT


def reverse_bwt(seq):
    """reverse_bwt(seq) takes as input a string containing the EOF character to
    which the reverse of the BWT must be applied. The method should then return
    the result of the reversal on the input string.

    For example:
        reverse_bwt('ACTGA$TA') --> 'GATTACA$'

    Args:
        seq (str): input string with an EOF character

    Returns:
        (str): the transformed string
    """
    table = [""] * len(seq)
    for i in range(len(seq)):
        table = sorted(seq[i] + table[i] for i in range(len(seq)))
    s = [row for row in table if row.endswith("$")][0]
    print (s)
    return s


def solve_bwt():

    # example sequences for forward_bwt() and reverse_bwt()
    # you may change them to different sequences to test your code.
    """
    seq1 = 'GATTACA$'
    seq2 = 'ACTGA$TA'
    forward_bwt(seq1)
    reverse_bwt(seq2)
    """

    # Load the mystery.txt and decode its contents using the reverse BWT
    # transformation. Report its contents.

    # Your code here
    mysteryText = open('mystery.txt', 'r')
    mysteryText = mysteryText.read()
    reverse_bwt(mysteryText)

if __name__ == '__main__':
    # forward_bwt('GATTACA$')
    # forward_bwt('AGT$TACGA')
    # reverse_bwt('ACTGA$TA')
    # reverse_bwt('AGT$TACGA')
    forward_bwt('CGGACTAACGGACTAACGGACTAACGGACTAA$')
    solve_bwt()

