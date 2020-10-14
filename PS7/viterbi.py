
import sys
from pprint import *
from math import log
from compsci260lib import *


def viterbi_decoding(input_file, hmm_file):
    """Calculate the viterbi decoding of an input sequence

    Arguments:
        input_file (str): path to input fasta file
        hmm_file (str): path to HMM file

    Returns:
        A list of dictionaries of segments in each state. An example output may
        look like:

        [
            {‘startPosition’: 0, ‘end’: 12, ‘state’: ‘state2’},
            {‘startPosition’: 13, ‘end’: 20, ‘state’: ‘state1’},
            ...
        ]
    """

    # open hmm file
    try:
        f_hmm_file = open(hmm_file, 'r')
    except IOError:
        print(("IOError: Unable to open HMM file: %s." % hmm_file))
        print("Exiting.")
        sys.exit(1)

    # read the state names and number
    states = f_hmm_file.readline().split()
    # print('states', states)
    K = len(states)

    # read the initial probabilities
    probs = f_hmm_file.readline().split()
    initial_probs = [float(prob) for prob in probs]
    # print('initial probs', initial_probs)

    # read the transition matrix
    transitions = [None for _ in range(K)]
    for i in range(K):
        matrix_row_arry = f_hmm_file.readline().split()
        matrix_row = [float(trans_prob) for trans_prob in matrix_row_arry]
        transitions[i] = matrix_row
    # print('transitions', transitions)

    # read the emitted symbols
    emitted_symbols = f_hmm_file.readline().split()

    # read the emission probability matrix
    emit_probs = [None for _ in range(K)]
    for i in range(K):
        matrix_row_arry = f_hmm_file.readline().split()
        matrix_row = [float(emit_prob) for emit_prob in matrix_row_arry]
        emit_probs[i] = matrix_row
    # print('emit', emit_probs)

    f_hmm_file.close()

    seq_dict = get_fasta_dict(input_file)
    emit_str = list(seq_dict.values())[0]  # there's only 1
    print(emit_str)
    print("Done reading sequence of length ", len(emit_str))

    # Create BLANK Viterbi table and traceback table
    viterbi = [[0 for _ in range(len(emit_str))] for _ in range(K)]
    pointers = [[0 for _ in range(len(emit_str))] for _ in range(K)]

    # Initialize the first column of the matrix
    for i in range(K):
        in_index = get_emit_index(emit_str[0].upper(), emitted_symbols)
        viterbi[i][0] = log(emit_probs[i][in_index]) + log(initial_probs[i])

    #Fill matrix with neg inf
    for j in range(1, len(emit_str)):
        for i in range(K):
            viterbi[i][j] = float("-inf")

    # Build the matrix column by column
    for j in range(1, len(emit_str)):
        in_index = get_emit_index(emit_str[j].upper(), emitted_symbols)
        for i in range(K):
            # Compute the entries viterbi[i][j] and pointers[i][j]
            # Tip: Use float('-inf') for the value of negative infinity
            for k in range(K):
                probEmit = emit_probs[i][in_index]
                prob = viterbi[k][j-1] + log(probEmit) + log(transitions[k][i])
                if prob > viterbi[i][j]:
                    viterbi[i][j] = prob
                    pointers[i][j] = k
    # print(viterbi)
    # print(pointers)

    # Traceback, stored as a list segment lengths in each state as dictionaries
    traceback = ""
    initialState = [i[-1] for i in viterbi].index(max([i[-1] for i in viterbi]))
    currentState = initialState
    for i in range(0, len(emit_str)):
        traceback += str(currentState)
        currentState = pointers[currentState][len(emit_str) - 1 - i]
    traceback = traceback[::-1]
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
        newDict['state'] = str('state') + str(int(currentState) + 1)
        segmentList.append(newDict)
        startPosition = positionCounter
        currentState = traceback[indexCounter]

    # pprint(segmentList)
    return segmentList


def count_segments(vit_ret):
    """Calculate the number of segments appearing in each state of
    the viterbi path

    Arguments:
        vit_ret (list of dicts): dictionary of lengths in each state.
            see: return value of viterbi_decoding

    Returns:
        a dictionary of states to number of occurrences in the state. e.g.
        {'state0': 10, 'state1': 2}
    """

    """YOUR CODE HERE"""
    ###
    ### Says it may be useful to report statistics about the length distribution of the segments
    ### For each state
    ###
    stateList = []

    for i in range(0, len(vit_ret)):
        if vit_ret[i]['state'] not in stateList:
            stateList.append(vit_ret[i]['state'])
    stateList = sorted(stateList)

    countsList = []
    for i in range(0,len(stateList)):
        countsList.append(0)

    for i in range (0, len(vit_ret)):
        for j in range(0, len(stateList)):
            if vit_ret[i]['state'] == stateList[j]:
                countsList[j] += 1

    stateCounts = {}
    for i in range (0, len(stateList)):
        stateCounts[str(stateList[i])] = countsList[i]

    print('Output of count_segments', stateCounts)
    return stateCounts

def get_emit_index(input_val, alphabet):
    """Get the index of the emission value in the alphabet

    Note: This will be a useful function for indexing the emission
    probabilities"""
    return alphabet.index(input_val)


def main():
    hmm_file = 'HMM.methanococcus.txt'
    # input_file = 'artificial.genome.fasta'
    input_file = "bacterial.genome.fasta"
    vit_ret = viterbi_decoding(input_file, hmm_file)

    # report the number of segments that exist in each state.
    counts = count_segments(vit_ret)
    keyList = list(dict.keys(counts))

    for i in range(0, len(keyList)):
        print('There are %d segments in ' % counts[keyList[i]] + keyList[i])

    print('\nFirst Ten Segments:')
    for i in range(0, 10):
        print(vit_ret[i])

    print('\nLast Ten Segments:')
    for i in range(len(vit_ret)-10, len(vit_ret)):
        print(vit_ret[i])



if __name__ == '__main__':
    """Call main(), do not modify."""
    main()
