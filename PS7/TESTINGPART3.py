from compsci260lib import *
from pprint import *

def assembly_tester():
    
    d = get_fasta_dict('paired.reads.fasta')
    Contig0 = get_fasta_dict('contig0.fasta')['contig0']
    Contig1 = get_fasta_dict('contig1.fasta')['contig1']
    SuperContig = get_fasta_dict('supercontig.fasta')['super_contig0']
    # pprint(SuperContig)
    bridgedGap = '<---bridged gap---> '
    # print(len('<---bridged gap---> '))
    
    FakeGap = 21

    MatedPairs = {}
    
    for k,v in d.items():
        sequence = k[:-1]
        letter = k[-1]
        if sequence not in MatedPairs:
            MatedPairs[sequence] = ["",""]
        if letter == "a":
            MatedPairs[sequence][0] = v
        else:
            MatedPairs[sequence][1] = v
          
    Error1 = []       
    Error2 = []
    Error3 = []
    
    SeperateContigs = []

    for k,v in MatedPairs.items():
        a = v[0]
        b = v[1]
        A = []
        B = []

        if a in Contig0:
            A.append(0)
            A.append(Contig0.find(a))
        elif a in Contig1:
            A.append(1)
            A.append(Contig1.find(a))
        else:
            A.append(-1)

        if b in Contig0:
            B.append(0)
            B.append(Contig0.find(b))
        elif b in Contig1:
            B.append(1)
            B.append(Contig1.find(b))
        else:
            B.append(-1)

        if A[0] == -1 or B[0] == -1:
            Error1.append(k)

        elif A[0] == B[0]:
            if A[1] < B[1] and ((B[1] + len(b)) - A[1] < 1980 or (B[1] + len(b)) - A[1] > 2020):
                    Error2.append(k)
            elif B[1] < A[1] and ((A[1] + len(a)) - B[1] < 1980 or (A[1] + len(a)) - B[1] > 2020):
                    Error2.append(k)
        else:
            A = SuperContig.find(a)
            B = SuperContig.find(b)
            if A < B:
                gap = B + len(b) - A - FakeGap
                SeperateContigs.append(gap)
            else:
                gap = A + len(a) - B - FakeGap
                SeperateContigs.append(gap)
                Error3.append(k)

    if len(Error2) == 0 and len(Error3) == 0 and len(Error1) == 0:
        print ("The Assembly is correct!")
    else:
        if len(Error1) > 0:
            print ("ERROR! There is a Miscellaneous Sequence Pair, the sequence is:", Error1[0])
        if len(Error2) > 0:
            print ("ERROR! The following mated pair sequences are of the wrong length:", Error2)
        if  len(Error3) > 0:
            print ("ERROR! The following mated pair sequences are ordered incorrectly:", Error3)

    print ('''\nWhen the bridge gap is of length 0, the distance between the beginning of the first sequence
to the end of the last sequence in a mated pair are as follows:''')
    print (SeperateContigs)

if __name__ == '__main__':
    assembly_tester()
