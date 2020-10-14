import sys
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
            {‘start’: 0, ‘end’: 12, ‘state’: ‘state2’},
            {‘start’: 13, ‘end’: 20, ‘state’: ‘state1’},
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
    print('states', states)
    K = len(states)

    # read the initial probabilities
    probs = f_hmm_file.readline().split()
    initial_probs = [float(prob) for prob in probs]
    print('initial probs', initial_probs)

    # read the transition matrix
    transitions = [None for _ in range(K)]
    for i in range(K):
        matrix_row_arry = f_hmm_file.readline().split()
        matrix_row = [float(trans_prob) for trans_prob in matrix_row_arry]
        transitions[i] = matrix_row
    print('transitions', transitions)

    # read the emitted symbols
    emitted_symbols = f_hmm_file.readline().split()

    # read the emission probability matrix
    emit_probs = [None for _ in range(K)]
    for i in range(K):
        matrix_row_arry = f_hmm_file.readline().split()
        matrix_row = [float(emit_prob) for emit_prob in matrix_row_arry]
        emit_probs[i] = matrix_row
    print('emit', emit_probs)

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
        
    # Build the matrix column by column
    for j in range(1, len(emit_str)):
        in_index = get_emit_index(emit_str[j].upper(), emitted_symbols)
        
        for i in range(K):
            # Compute the entries viterbi[i][j] and pointers[i][j]
            # NEG_INF is float('-inf')
            emition_prob = emit_probs[i][in_index]
            viterbi[i][j] = float("-inf")           
            for k in range(K):
                prob = viterbi[k][j-1] + log(emition_prob) + log(transitions[k][i])
                if prob > viterbi[i][j]:
                    viterbi[i][j] = prob
                    pointers[i][j] = k
    print(viterbi)
    print(pointers)
       
    # Traceback code goes here:
    last_column = [i[-1] for i in viterbi]
    max_start = max(last_column)
    start_state = last_column.index(max_start)
    cur_state = start_state
    traceback = ""    
    for i in range(len(emit_str)-1,-1,-1):
        traceback += str(cur_state)
        cur_state = pointers[cur_state][i]
    
    traceback = traceback[::-1]
     
    i = 1
    start_i = 0
    start_state = traceback[0]
     
    print ("start\tstop\tstate")
    while i<len(traceback)-1:
        while traceback[i] == start_state and i<len(traceback)-1:
            i += 1
        print (str(start_i+1)+"\t"+str(i)+"\t"+"state ", str(int(start_state)+1))
        start_i = i
        start_state = traceback[i]


def get_emit_index(input_val, alphabet):
    for i in range(len(alphabet)):
        if alphabet[i] == input_val:
            return i
    
    sys.stderr("Could not find character " + input_val)


if __name__ == '__main__':
    hmm_file = "HMM.methanococcus.txt"
    input_file = "artificial.genome.fasta"
    # input_file = "bacterial.genome.fasta"
    vit_ret = viterbi_decoding(input_file, hmm_file)
    
    f_in_file = open(input_file)
    f_hmm_file = open(hmm_file)
    
    if f_in_file is None:
        sys.exit("Can't open HMM file: " + hmm_file)
    if f_hmm_file is None:
        sys.exit("Can't open file: " + input_file)
    
    viterbi_decoding(f_in_file, f_hmm_file)
