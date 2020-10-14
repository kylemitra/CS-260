from compsci260lib import *
import sys
import random
import os


def generate_HMM(hmm_file, seq_length):
    """ Load an HMM specification from file, and generate state and observed
        sequences through sampling of the HMM.

        The HMM will have states labeled as strings and observations as (string)
        characters which will be useful when we generate an HMM with nucleotide
        sequence observations:

        An example return sequence for an occasionally dishonest casino HMM
        with dice rolls may look like:
            (['F', 'L', 'L'], ['2', '6', '6'])

        Arguments:
            hmm_file (str): path to the HMM file
            seq_length (int): the length of the sequence we will generate

        Returns:
            a tuple of
            (the state sequence as strings,
             observed sequence as single character strings)
    """
    if not os.path.exists(hmm_file):
        raise ValueError("Can't open HMM parameter file: %s" % hmm_file)

    f = open(hmm_file, "r")

    # read the state names
    states = f.readline().strip().split()

    # read the initial probabilities
    initial_probs = f.readline().strip().split()
    initial_probs = [float(p) for p in initial_probs]

    # read and store the transition matrix
    # NOTE: this is stored as a dictionary of lists, so the rows of the
    #       matrix are "named" with the state name as a key, while the
    #       columns of the matrix correspond to indices into the list
    transitions = {}
    for i in range(0, len(states)):
        state = states[i]
        matrix_row = f.readline().strip().split()
        transitions[state] = [float(p) for p in matrix_row]

    # read in all the observable characters
    observable_chars = f.readline().strip().split()

    # read the emission matrix
    # NOTE: this is stored as a dictionary of lists, so the rows of the
    #       matrix are "named" with the state name as a key, while the
    #       columns of the matrix correspond to indices into the list
    emission = {}
    for i in range(0, len(states)):
        state = states[i]
        matrix_row = f.readline().strip().split()
        emission[state] = [float(p) for p in matrix_row]
        # normalize
        sum_emissions = sum(emission[state])
        emission[state] = [x / sum_emissions for x in emission[state]]
    f.close()

    # YOUR CODE GOES HERE....
    state_sequence = []
    observed_sequence = []
    print(transitions)
    print(emission)

    #Initialize Firs tState
    initalStatesList = list(transitions.keys())
    state_sequence.append(random.choice(initalStatesList)) #Random Generate first
    print('The first state picked was', state_sequence[0])

    stateChoiceList = []
    for i in range(0, len(initalStatesList)):
        stateChoiceList.append(initalStatesList[i])
    for i in range (0, len(initalStatesList)):
        transitions[initalStatesList[i]] = [x * 100 for x in transitions[initalStatesList[i]]]
        emission[initalStatesList[i]] = [x * 100 for x in emission[initalStatesList[i]]]

    for i in range(1,seq_length):
        outcomeProbList = []
        for j in range(0, len(observable_chars)):
            outcomeProbList.append(observable_chars[j])
        for k in range(0, len(emission[state_sequence[i-1]])):
            outcomeProbList[k] = outcomeProbList[k] * round(list(emission[state_sequence[i-1]])[k])
        outcomeProbList = list(''.join(outcomeProbList))
        observed_sequence.append(random.choice(outcomeProbList))

        stateChoiceList2 = []
        for x in range(0, len(initalStatesList)):
            if state_sequence[i-1] == initalStatesList[x]:
                for y in range(0, len(stateChoiceList)):
                    for z in range (0, round(transitions[initalStatesList[x]][y])):
                        stateChoiceList2.append(stateChoiceList[y])
        state_sequence.append(random.choice(stateChoiceList2))

    #Adds last roll unaccounted for
    outcomeProbList = []
    for j in range(0, len(emission[state_sequence[i - 1]])):
        outcomeProbList.append(str(j + 1))
    for k in range(0, len(emission[state_sequence[i - 1]])):
        outcomeProbList[k] = outcomeProbList[k] * round(list(emission[state_sequence[i - 1]])[k])
    outcomeProbList = list(''.join(outcomeProbList))
    observed_sequence.append(random.choice(outcomeProbList))

    state_sequence = [x.replace('state1', '1') for x in state_sequence]
    state_sequence = [x.replace('state2', '2') for x in state_sequence]
    state_sequence = ''.join(state_sequence)
    observed_sequence = ''.join(observed_sequence)

    print('state', state_sequence)
    print('observed', observed_sequence)
    return (state_sequence, observed_sequence)  # a tuple containing the state and observation sequences


def audit_casino(state_sequence, observed_sequence, subsequence):
    """Given state and observed sequences, report the state sequences and
    frequency of those state sequences that emitted the rolls represented
    in subsequence
    """

    # YOUR CODE GOES HERE
    matchCounter = 0
    locationList = []
    stateList = []
    countsDict = {}

    for i in range(0, len(observed_sequence)):
        for j in range(0, len(subsequence)):
            if ((i+j) < len(observed_sequence)):
                if (observed_sequence[i+j] == subsequence[j]):
                    matchCounter += 1
                    locationList.append(i+j)
                else:
                    matchCounter = 0
                    locationList = []
                if matchCounter == len(subsequence):
                    for k in range (0, len(locationList)):
                        stateList.append(state_sequence[locationList[k]])
                    stateList = ' '.join([str(x) for x in stateList])
                    if stateList in countsDict:
                        countsDict[stateList] += 1
                    else:
                        countsDict[stateList] = 1
                    stateList = []
    print('Dict of Counts', countsDict)



def main():
    """Generate state and observed sequences and report the frequency of state
    sequences emitting 1662"""
    seq_length = 1000
    state_sequence, observed_sequence = generate_HMM("HMM.sequence.txt",
                                                     seq_length)
    audit_casino(state_sequence, observed_sequence, ['1','6','6','2'])
    f = open("artificial_genome.txt", "w+")
    f.write(state_sequence)
    f.write(observed_sequence)
    f.close()


if __name__ == '__main__':
    """Main method call, do not modify"""
    main()

