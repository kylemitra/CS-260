import sys
from math import log, exp
from compsci260lib import get_fasta_dict
from pprint import *
# from viterbi import count_segments


def posterior_decoding(input_file, hmm_file):
    """
    Calculate the posterior decoding and return the decoded segments.

    input_file (str): path to input fasta file
    hmm_file (str): path to HMM file

    Returns:
        A list of dictionaries of segments in each state. An example output may
        look like:

        [
            {‘start’: 0, ‘end’: 12, ‘state’: ‘state2’},
            {‘start’: 13, ‘end’: 20, ‘state’: ‘state1’},
            ...
        ]
    """

    # Read in the input files
    f_in_file = open(input_file)
    f_hmm_file = open(hmm_file)
    if f_in_file is None: sys.exit("Can't open HMM file: " + hmm_file)
    if f_hmm_file is None: sys.exit("Can't open file: " + input_file)

    # read the state names and number
    states = f_hmm_file.readline().split()
    K = len(states)

    # read the initial probabilities
    probs = f_hmm_file.readline().split()
    initial_probs = [float(prob) for prob in probs]

    # read the transition matrix
    transitions = [None for _ in range(K)]
    for i in range(K):
        matrix_row_arry = f_hmm_file.readline().split()
        matrix_row = [float(trans_prob) for trans_prob in matrix_row_arry]
        transitions[i] = matrix_row

    # read the emission symbols
    emission_symbols = f_hmm_file.readline().split()

    # read the emission probability matrix
    emit_probs = [None for _ in range(K)]
    for i in range(K):
        matrix_row_arry = f_hmm_file.readline().split()
        matrix_row = [float(emit_prob) for emit_prob in matrix_row_arry]
        emit_probs[i] = matrix_row

    f_hmm_file.close()

    seq_dict = get_fasta_dict(input_file)
    emit_str = list(seq_dict.values())[0]  # there's only 1

    print(("Done reading sequence of length ", len(emit_str)))

    # Run the forward algorithm
    forward = run_forward(states, initial_probs, transitions,
                          emission_symbols, emit_probs, emit_str)

    # Run the backward algorithm
    backward = run_backward(states, initial_probs,
                            transitions, emission_symbols, emit_probs,
                            emit_str)

    # Calculate the posterior probabilities
    # Initializing the posterior 2D matrices
    posterior = [[float(0) for _ in range(K)] for _ in range(len(emit_str))]
    for i in range(len(emit_str)):
        # Did not normalize the probabilities (i.e., did not divide by P(X)),
        # because we will only use these probabilities to compare
        # posterior[i][0] versus posterior[i][1]
        for k in range(K):
            posterior[i][k] = forward[i][k] + backward[i][k]
    # print(posterior)

    # Create the list of decoded segments to return
    traceback = ""
    for i in posterior:
        maxState = i.index(max(i)) + 1
        traceback += str(maxState)
    # print(traceback)

    positionCounter = 1
    indexCounter = 0
    startPosition = 0
    currentState = traceback[0]
    segmentList = []

    while positionCounter < len(traceback):
        while traceback[indexCounter] == currentState and positionCounter < len(traceback):
            positionCounter += 1
            indexCounter += 1
        newDict = {}
        newDict['start'] = startPosition + 1
        newDict['end'] = positionCounter
        newDict['state'] = str('state') + str(int(currentState))
        segmentList.append(newDict)
        startPosition = positionCounter
        currentState = traceback[indexCounter]

    # pprint(segmentList)
    return segmentList


def run_forward(states, initial_probs, transitions,
                emission_symbols, emit_probs, emit_str):
    """Calculates the forward probability matrix.

    Arguments:
        states (list of str): list of states as strings
        initial_probs (list of float): list of initial probabilities for each
            state
        transitions (list of list of float): matrix of transition probabilities
        emission_symbols (list of str): list of emission symbols
        emit_probs (list of list of float): matrix of emission probabilities
            for each state and emission symbol
        emit_str (str):

    Returns:
        (list of list of floats): matrix of forward probabilities
    """
    K = len(states)
    L = len(emit_str)
    forward = [[float(0) for _ in range(K)] for _ in range(L)]

    # Initialize
    emit_index = get_emit_index(emit_str[0], emission_symbols)
    for k in range(K):
        forward[0][k] = log(initial_probs[k]) + log(emit_probs[k][emit_index])

    #Fill matrix with neg inf
    for i in range(1, L):
        for j in range(0, K):
            forward[i][j] = float("-inf")

    # Iterate
    for i in range(1, L):
        emit_index = get_emit_index(emit_str[i].upper(), emission_symbols)
        # Compute the forward probabilities for the states
        for j in range(0, K):
            fkList = []
            probEmit = log(emit_probs[j][emit_index])
            for k in range(0, K):
                fk = forward[i-1][k] + log(transitions[k][j])
                fkList.append(fk)
            if fkList[0] == max(fkList):
                p = fkList[0]
                q = fkList[1]
            else:
                p = fkList[1]
                q = fkList[0]
            r = p + log(1+exp(q-p))
            if (probEmit + r) > forward[i][j]:
                forward[i][j] = probEmit + r
    return forward


def run_backward(states, initial_probs, transitions,
                 emission_symbols, emit_probs, emit_str):
    """Calculates the forward probability matrix.

        Arguments:
            states (list of str): list of states as strings
            initial_probs (list of float): list of initial probabilities for each
                state
            transitions (list of list of float): matrix of transition probabilities
            emission_symbols (list of str): list of emission symbols
            emit_probs (list of list of float): matrix of emission probabilities
                for each state and emission symbol
            emit_str (str):

        Returns:
            (list of list of floats): matrix of backwards probabilities
    """
    K = len(states)
    L = len(emit_str)
    backward = [[float(0) for _ in range(K)] for _ in range(L)]

    # Initialize
    for k in range(K):
        backward[L-1][k] = log(1)  # which is zero, but just to be explicit...

    #Fill matrix with neg inf
    for i in range(L-2, -1, -1):
        for j in range(0, K):
            backward[i][j] = float("-inf")

    # Iterate
    for i in range(L-2, -1, -1):
        emit_index = get_emit_index(emit_str[i+1].upper(), emission_symbols)
        # Compute the backward probabilities for the states
        for j in range(0, K):
            bkList = []
            for k in range(0, K):
                bk = backward[i+1][k] + log(transitions[j][k]) + log(emit_probs[k][emit_index])
                bkList.append(bk)
            if bkList[0] == max(bkList):
                p = bkList[0]
                q = bkList[1]
            else:
                p = bkList[1]
                q = bkList[0]
            r = p + log(1+exp(q-p))
            if r > backward[i][j]:
                backward[i][j] = r
    return backward


def get_emit_index(input_val, alphabet):
    """Get the index of the emission value in the alphabet

    Note: This will be a useful function for indexing the emission
    probabilities"""
    return alphabet.index(input_val)


def main():
    # input_file = "artificial.genome.fasta"
    input_file = "bacterial.genome.fasta"
    hmm_file = "HMM.methanococcus.txt"
    posteriorList = posterior_decoding(input_file, hmm_file)

    #Report the first and last ten segments in your decoding
    print('\nFirst Ten Segments:')
    for i in range(0, 10):
        print(posteriorList[i])

    print('\nLast Ten Segments:')
    for i in range(len(posteriorList)-10, len(posteriorList)):
        print(posteriorList[i])

    # segments = count_segments(posteriorList)

if __name__ == '__main__':
    """Call main(), do not modify"""
    main()
