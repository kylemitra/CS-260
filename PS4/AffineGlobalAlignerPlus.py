from compsci260lib import *
from GlobalAligner import *
from pprint import *

atpaHs = get_fasta_dict('atpa_Hs.fasta')
atpaHs = list(atpaHs.values())
atpaHs = ' '.join(atpaHs)
atpaEc = get_fasta_dict('atpa_Ec.fasta')
atpaEc = list(atpaEc.values())
atpaEc = ' '.join(atpaEc)

def solve_ag_aligner_plus(seq1, seq2, subst_dict, gap_penalty,
                          affine_penalty):
    """The overall procedure for collecting the inputs, running the aligner,
    and displaying the table and final value.

    Args:
        seq1 (str): first sequence to match
        seq2 (str): second sequence to match
        subst_dict (dictionary string -> int): dictionary representation
            of the substitution matrix
        gap_penalty (int): gap penalty (penalty per gap character); this
            value should be positive because we will subtract it
        affine_penalty (int): affine penalty; as a positive integer

    Reports:
        the optimal alignment score
        the up-most alignment achieving this score
        the down-most alignment achieving this score
    """

    """YOUR CODE GOES HERE..."""
    traceback_table = [[0] * (len(seq2)+1) for _ in range(len(seq1)+1)]
    for x in range(len(seq1)+1):
        for y in range(len(seq2)+1):
            traceback_table[x][y] = set()

    dp_table = [[0] * (len(seq2)+1) for _ in range(len(seq1)+1)]

    # the dp table has len(seq1) + 1 rows and len(seq2) + 1 columns
    I = len(dp_table)  # so I is 1 more than m
    J = len(dp_table[0])  # so J is 1 more than n

    # Initialize the dp table with solutions to base cases using linear gap
    #
    dp_table[0][0] = 0
    dp_table[1][0] = - gap_penalty - affine_penalty
    traceback_table[1][0].add("U")
    dp_table[0][1] = - gap_penalty - affine_penalty
    traceback_table[0][1].add("L")

    for i in range(2,I):
        dp_table[i][0] = dp_table[i-1][0] - gap_penalty
        traceback_table[i][0].add("U")

    for j in range(2,J):
        dp_table[0][j] = dp_table[0][j-1] - gap_penalty
        traceback_table[0][j].add("L")

    gapPresent = 1

    for i in range(1, I):
        for j in range(1, J):
            diagVal = dp_table[i - 1][j - 1] + subst_dict.get(seq1[i - 1] + seq2[j - 1])
            if gapPresent == 0:
                topVal = dp_table[i - 1][j] - gap_penalty - affine_penalty
                leftVal = dp_table[i][j - 1] - gap_penalty - affine_penalty
            else:
                topVal = dp_table[i - 1][j] - gap_penalty
                leftVal = dp_table[i][j - 1] - gap_penalty
            dp_table[i][j] = max(diagVal, topVal, leftVal)

            if dp_table[i][j] == diagVal:
                traceback_table[i][j].add("D")
                gapPresent = 0
            if dp_table[i][j] == topVal:
                traceback_table[i][j].add("U")
                if gapPresent == 0:
                    gapPresent = gapPresent + 1
            if dp_table[i][j] == leftVal:
                traceback_table[i][j].add("L")
                if gapPresent == 0:
                    gapPresent = gapPresent + 1

    display_dp_table(seq1,seq2,dp_table)
    print("\n\nThe score of an optimal global alignment is", dp_table[I - 1][J - 1])

    ####
    # Upmost Alignment
    ##
    topSolutionSequence = []
    topGivenSequence = []
    stringMatcherLocation = min(len(seq1), len(seq2)) - 1
    stringMatcherLocation2 = max(len(seq1), len(seq2)) - 1

    while (j != 0 or i != 0):
        if 'U' in traceback_table[i][j]:
            topGivenSequence.insert(0, "-")
            topSolutionSequence.insert(0, "-")
            i = i - 1
            stringMatcherLocation = stringMatcherLocation - 1
        if 'D' in traceback_table[i][j]:
            topGivenSequence.insert(0, seq2[stringMatcherLocation2])
            topSolutionSequence.insert(0, seq1[stringMatcherLocation])
            i = i - 1
            j = j - 1
            stringMatcherLocation = stringMatcherLocation - 1
            stringMatcherLocation2 = stringMatcherLocation2 - 1
        elif 'L' in traceback_table[i][j]:
            topGivenSequence.insert(0, seq2[stringMatcherLocation2])
            topSolutionSequence.insert(0, "-")
            j = j - 1
            stringMatcherLocation2 = stringMatcherLocation2 - 1
    topGivenSequence = "".join(topGivenSequence)
    topSolutionSequence = "".join(topSolutionSequence)
    print('\nUpmost alignment achieving this score is\n', topGivenSequence, '\n', topSolutionSequence)

    ####
    # Down-most solution
    ####
    i = len(dp_table) - 1
    j = len(dp_table[0]) - 1
    bottomGivenSequence = []
    bottomSolutionSequence = []
    stringMatcherLocation = min(len(seq1), len(seq2)) - 1
    stringMatcherLocation2 = max(len(seq1), len(seq2)) - 1

    while (j != 0 or i != 0):
        if 'L' in traceback_table[i][j]:
            bottomGivenSequence.insert(0, seq2[stringMatcherLocation2])
            bottomSolutionSequence.insert(0, "-")
            j = j - 1
            stringMatcherLocation2 = stringMatcherLocation2 - 1
        elif 'D' in traceback_table[i][j]:
            bottomGivenSequence.insert(0, seq2[stringMatcherLocation2])
            bottomSolutionSequence.insert(0, seq1[stringMatcherLocation])
            i = i - 1
            j = j - 1
            stringMatcherLocation = stringMatcherLocation - 1
            stringMatcherLocation2 = stringMatcherLocation2 - 1
        elif 'U' in traceback_table[i][j]:
            bottomGivenSequence.insert(0, "-")
            bottomSolutionSequence.insert(0, "-")
            i = i - 1
            stringMatcherLocation = stringMatcherLocation - 1
    bottomGivenSequence = "".join(bottomGivenSequence)
    bottomSolutionSequence = "".join(bottomSolutionSequence)
    print('Downmost alignment achieving this score is\n', bottomGivenSequence, '\n', bottomSolutionSequence)

if __name__ == '__main__':
    seq1 = 'GA'
    seq2 = 'GATTACA'
    match = 1
    mismatch = -1
    gap_penalty = 1
    affine_penalty = 3
    seq_type = validate_sequences(seq1, seq2)
    if seq_type == 1:
        # Both the sequences are DNA sequences so use the scores for match and
        # mismatch
        subst_matrix = create_subst_matrix_dna(match, mismatch)
    elif seq_type == 2:
        # Both the sequences are protein sequences so read in the BLOSUM62
        # substitution matrix
        subst_matrix = create_subst_matrix_aa("BLOSUM62.txt")
    else:
        sys.exit('Input sequences are of different types')

    # Obtain a dictionary of scores for aligning a pair of characters
    subst_dict = create_subst_matrix_dict(subst_matrix)

    solve_ag_aligner_plus(seq1, seq2, subst_dict,
                          gap_penalty, affine_penalty)