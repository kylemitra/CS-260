import sys
from math import log, exp
from compsci260lib import get_fasta_dict
# from pandas.join import inner_join_indexer_float32

def posterior_decoding(input_file, f_hmm_file):
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
    seqList = list(seq_dict.values())
    emit_str = seqList[0]  # there's only 1
    
    print ("Done reading sequence of length ", len(emit_str))
    
    # Run the forward algorithm
    forward = run_forward(states, initial_probs, transitions, emission_symbols, emit_probs, emit_str)
    
    # Run the backward algorithm
    backward = run_backward(states, initial_probs, transitions, emission_symbols, emit_probs, emit_str)
    
    # Calculate the posterior probabilities
    # Initializing the posterior 2D matrices
    posterior = [[float(0) for _ in range(K)] for _ in range(len(emit_str))]
    for i in range(len(emit_str)):
        # Did not normalize the probabilities (i.e., did not divide by P(X)),
        # because we will only use these probabilities to compare
        # posterior[i][0] versus posterior[i][1]
        for k in range(K):
            posterior[i][k] = forward[i][k] + backward[i][k]
    
#     print forward
#     print backward
#     print posterior
    # Print out the decoded results
    traceback = ""
    for i in posterior:
        m = max(i)
        state = i.index(m)
        traceback += str(state)
    
#     print traceback
    
    i = 1
    start_i = 0
    start_state = traceback[0]
    count = 0
     
    print ("start\tstop\tstate")
    while i<len(traceback)-1:
        while traceback[i] == start_state and i<len(traceback)-1:
            i += 1
        print (str(start_i+1)+"\t"+str(i)+"\t"+"state ", str(int(start_state)+1))
        count += 1
        start_i = i
        start_state = traceback[i]
    
    print (count)


def run_forward(states, initial_probs, transitions, 
    emission_symbols, emit_probs, emit_str):
    """Calculates the forward probability matrix"""

    K = len(states)
    L = len(emit_str)

    forward = [[float(0) for _ in range(K)] for _ in range(L)]

    # Initialize
    emit_index = get_emit_index(emit_str[0], emission_symbols)
    for k in range(K):
        forward[0][k] = log(initial_probs[k]) + log(emit_probs[k][emit_index])
    
    # Iterate
    for i in range(1, L):
        emit_index = get_emit_index(emit_str[i].upper(), emission_symbols)
        # Compute the forward probabilities for the states
        p = 0
        q = 0
        for j in range(K):
            porq = []
            forward[i][j] = float("-inf")
            emition_prob = log(emit_probs[j][emit_index])
            for k in range(K):
                prob = forward[i-1][k] + log(transitions[k][j])
                porq.append(prob)
         
            if porq[0] > porq[1]:
                p = porq[0]
                q = porq[1]
            else:                                                
                q = porq[0]
                p = porq[1]
            r = p + log(1+exp(q-p))
            forward[i][j] = emition_prob + r
        
    return forward        
        

def run_backward(states, initial_probs, transitions, 
    emission_symbols, emit_probs, emit_str):
    """Calculates the backward probability matrix"""

    K = len(states)
    L = len(emit_str)

    backward = [[float(0) for _ in range(K)] for _ in range(L)]

    # Initialize
    for k in range(K):
        backward[L-1][k] = log(1)  # which is zero, but just to be explicit...
    
    # Iterate
    for i in range(L-2, -1, -1):
        emit_index = get_emit_index(emit_str[i+1].upper(), emission_symbols)
        
        # Compute the backward probabilities for the states
        p = 0
        q = 0
        for j in range(K):
            porq = []
            backward[i][j] = float("-inf")
        
            for k in range(K):
                prob = backward[i+1][k] + log(transitions[j][k]) + log(emit_probs[k][emit_index])
                porq.append(prob)
         
            if porq[0] > porq[1]:
                p = porq[0]
                q = porq[1]
            else:                                                
                q = porq[0]
                p = porq[1]
            r = p + log(1+exp(q-p))
            backward[i][j] = r
    


    return backward        
        

def get_emit_index(input_val, alphabet):
    """does a linear search to find the index of a character"""
    for i in range(len(alphabet)):
        if alphabet[i] == input_val:
            return i
    sys.exit("Could not find character " + input_val)


if __name__ == '__main__':
    hmm_file = "HMM.methanococcus.txt"
    input_file = "artificial.genome.fasta"
    posterior_decoding(input_file, hmm_file)
