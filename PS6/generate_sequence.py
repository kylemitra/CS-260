from compsci260lib import *
from generate_HMM import generate_HMM


def summarize_sequence(state_sequence):
    """
    Given a state sequence, report the average length in each state

    Arguments:
        state_sequence (list of strings): generated sequence of states
    """

    # YOUR CODE GOES HERE
    stateOneCounter = 0
    stateOneAvg = 0
    stateTwoCounter = 0
    stateTwoAvg = 0

    for i in range(0, len(state_sequence)):
        if state_sequence[i] == '1':
            stateOneCounter += 1
        if state_sequence[i] == '2':
            stateTwoCounter += 1

    stateOneAvg = (stateOneCounter / len(state_sequence)) * 100
    stateTwoAvg = (stateTwoCounter / len(state_sequence)) * 100
    print('Percent of time in state1', stateOneAvg)
    print('Percent of time in state2', stateTwoAvg)

def ntide_sequence(state_sequence, observed_sequence, seq_length):

    ntideDict = {'A': {'1':0, '2':0}, 'C': {'1':0, '2':0},
                 'G': {'1':0, '2':0}, 'T': {'1':0, '2':0}}

    for i in range(0, seq_length-1):
        ntideDict[str(observed_sequence[i])][str(state_sequence[i])] += 1
    print(ntideDict)




def main():
    """Load the sequence HMM file, then report the average length in each
    state"""
    seq_length = 1000
    state_sequence, observation_sequence = generate_HMM("HMM.sequence.txt",
                                                     seq_length)
    summarize_sequence(state_sequence)
    ntide_sequence(state_sequence, observation_sequence, seq_length)


if __name__ == '__main__':
    """Main method call, do not modify"""
    main()
