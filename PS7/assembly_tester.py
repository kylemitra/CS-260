from compsci260lib import *
from pprint import *


def assembly_tester(reads_file, contig0_file, contig1_file):
    """
    Read in the contig files, verify the reads in each contig, and estimate
    the gap length between the contigs
    """

    # load the fasta files
    reads = get_fasta_dict(reads_file)
    contig0 = get_fasta_dict(contig0_file)['contig0']
    contig1 = get_fasta_dict(contig1_file)['contig1']

    # make sure the contigs pass the criteria in part d
    matedPairsDict = {}
    for i, j in reads.items():
        readName = i[:-1]
        char = i[-1]
        if readName not in matedPairsDict:
            matedPairsDict[readName] = ["",""]
        if char == "a":
            matedPairsDict[readName][0] = j
        elif char == "b":
            matedPairsDict[readName][1] = j
    # pprint(matedPairsDict)

    superContig = get_fasta_dict('supercontig.fasta')['super_contig0']
    bridgedGap = '<---bridged gap---> '
    bridgedGapLength = len(bridgedGap)
    # pprint(superContig)

    errorsPresent = 0

    for i, j in matedPairsDict.items():
        aSeq = j[0]
        bSeq = j[1]

        if ((aSeq not in contig0) and (aSeq not in contig1)) or ((bSeq not in contig0) and (bSeq not in contig1)):
            print('ERROR: This read is not anywhere in the set of contigs:', i)
            errorsPresent += 1
        elif ((aSeq in contig0) and (bSeq in contig0)) or ((aSeq in contig1) and (bSeq in contig1)):
            aSeq0 = contig0.find(aSeq)
            bSeq0 = contig0.find(bSeq)
            aSeq1 = contig1.find(aSeq)
            bSeq1 = contig1.find(bSeq)
            if (aSeq in contig0) and (bSeq in contig0):
                if aSeq0 < bSeq0 and (bSeq0 + len(bSeq)) - aSeq0 < 1980 or (bSeq0 + len(bSeq)) - aSeq0 > 2020:
                    print('ERROR: The distance of this mated pair is not 2000 +/- 10:', i)
                    errorsPresent += 1
                elif aSeq0 > bSeq0 and (aSeq0 + len(aSeq)) - bSeq0 < 1980 or (aSeq0 + len(aSeq)) - bSeq0 > 2020:
                    print('ERROR: The distance of this mated pair is not 2000 +/- 10:', i)
                    errorsPresent += 1
            if (aSeq in contig1) and (bSeq in contig1):
                if aSeq1 < bSeq1 and (bSeq1 + len(bSeq)) - aSeq1 < 1980 or (bSeq1 + len(bSeq)) - aSeq1 > 2020:
                    print('ERROR: The distance of this mated pair is not 2000 +/- 10:', i)
                    errorsPresent += 1
                elif aSeq1 > bSeq1 and (aSeq1 + len(aSeq)) - bSeq1 < 1980 or (aSeq1 + len(aSeq)) - bSeq1 > 2020:
                    print('ERROR: The distance of this mated pair is not 2000 +/- 10:', i)
                    errorsPresent += 1
        else:
            superA = superContig.find(aSeq)
            superB = superContig.find(bSeq)
            if superA >= superB:
                print('ERROR: The first read in the pair does not appear after the second read for the mated pair:', i)
                errorsPresent += 1

    if errorsPresent == 0:
        print('Assembly is consistent with the reads')
    # determine how the reads map to the contigs
    contig_reads = find_contig_reads(reads, contig0, contig1)

    # report the reads whose ends map to both contig0 and contig1
    # and their estimated gap lengths
    numDiffMates = 0
    readList = []
    gapLengthList = []

    for i in contig_reads:
        if contig_reads[i]['contig_a'] != contig_reads[i]['contig_b']:
            numDiffMates += 1
            readList.append(i)
            aSeq = matedPairsDict[i][0]
            bSeq = matedPairsDict[i][1]
            aLocation = superContig.find(aSeq)
            bLocation = superContig.find(bSeq)
            if aLocation > bLocation:
                gapLength = aLocation - (bLocation + len(bSeq)) - bridgedGapLength
            if aLocation < bLocation:
                gapLength = bLocation - (aLocation + len(aSeq)) - bridgedGapLength
            gapLengthList.append(gapLength)
    print('There are %d reads where one mate maps to contig0 and the other maps to contig1' % numDiffMates)
    estimateGapLength = sum(gapLengthList) / len(gapLengthList)
    print('The estimates gap length is', round(estimateGapLength))



def find_contig_reads(reads, contig0, contig1):
    """
    Determine whether the sequencing reads map to contig0/contig1/both/neither
    and where in the contig it matches. `reads` will contain both ends 'a' and
    'b', but you will return a dictionary using the read name as a whole
    (without 'a' and 'b').

    It should return a dictionary mapping the name of the mated pair of reads to:
        - 'contig_a' (str): the contig in which read 'a' was found in as `contig0',
          `contig1', or None.
        - start_a (int): the start position (1-indexed) read end 'a' mapped to
          for its respective contig (None if not found in any contig)
        - end_a (int): the end position (1-indexed) read end 'a' mapped to
          for its respective contig (None if not found in any contig)
        - 'contig_b' (str): the contig in which read 'b' was found in as `contig0',
          `contig1', or None.
        - start_b (int): the start position (1-indexed) read end 'b' mapped to
          for its respective contig (None if not found in any contig)
        - end_b (int): the end position (1-indexed) read end 'b' mapped to
          for its respective contig (None if not found in any contig)

    The returned dictionary should look something like:
    {
        'seq1': {
            'contig_a': 'contig1',
            'start_a': 1,
            'end_a': 100,
            'contig_b': None
            'start_b': None,
            'end_b': None,
        },
        'seq2': {
            'contig_a': 'contig0',
            'start_a': 101,
            'end_a': 200,
            'contig_b': 'contig1'
            'start_b': 201,
            'end_b': 300,
        },
        'seq3' : {
            'contig_a': None,
            'start_a': None,
            'end_a': None,
            'contig_b': None
            'start_b': None,
            'end_b': None,
        },
        ...
    }

    Arguments:
        reads (dict str to str): dictionary of sequencing reads
        contig0 (dict str to str): dictionary of reads in contig0
        contig1 (dict str to str): dictionary of reads in contig1

        see: get_fasta_dict

    Returns:
        Dictionary mapping reads to information of their mapping contig.
    """

    """YOUR CODE HERE"""

    matedPairsDict = {}
    for i, j in reads.items():
        readName = i[:-1]
        char = i[-1]
        if readName not in matedPairsDict:
            matedPairsDict[readName] = ["",""]
        if char == "a":
            matedPairsDict[readName][0] = j
        elif char == "b":
            matedPairsDict[readName][1] = j

    contigReadsDict = {}

    for i, j in matedPairsDict.items():
        contigReadsDict[i] = {}

        if j[0] in contig0:
            contigReadsDict[i]['contig_a'] = 'contig0'
            contigReadsDict[i]['start_a'] = contig0.find(j[0]) + 1
            contigReadsDict[i]['end_a'] = contig0.find(j[0]) + len(j[0])
        elif j[0] in contig1:
            contigReadsDict[i]['contig_a'] = 'contig1'
            contigReadsDict[i]['start_a'] = contig1.find(j[0]) + 1
            contigReadsDict[i]['end_a'] = contig1.find(j[0]) + len(j[0])
        else:
            contigReadsDict[i]['contig_a'] = 'None'
            contigReadsDict[i]['start_a'] = 'None'
            contigReadsDict[i]['end_a'] = 'None'

        if j[1] in contig0:
            contigReadsDict[i]['contig_b'] = 'contig0'
            contigReadsDict[i]['start_b'] = contig0.find(j[1]) + 1
            contigReadsDict[i]['end_b'] = contig0.find(j[1]) + len(j[1])
        elif j[1] in contig1:
            contigReadsDict[i]['contig_b'] = 'contig1'
            contigReadsDict[i]['start_b'] = contig1.find(j[1]) + 1
            contigReadsDict[i]['end_b'] = contig1.find(j[1]) + len(j[0])
        else:
            contigReadsDict[i]['contig_b'] = 'None'
            contigReadsDict[i]['start_b'] = 'None'
            contigReadsDict[i]['end_b'] = 'None'


    # pprint(contigReadsDict)
    return contigReadsDict


def main():
    """Call assembly tester with provided fasta files"""
    reads_file = 'paired.reads.fasta'
    contig0_file = 'contig0.fasta'
    contig1_file = 'contig1.fasta'
    assembly_tester(reads_file, contig0_file, contig1_file)

    peptides = open("peptides.fasta", "w")
    peptides.write('MKKIEDSNTLVITVDVKAKKHQIKQAVKKLCDINVAKFQVPSAALRRGVFALWALPRLLLQVCSPTAAFPVLRDHRPPGALCL')
    peptides.write('\nMSGRGKQGGKARAKAKSRSSRAGLQFPVGRVHRLLRKGNYSERVGAGAPVYLAAVLEYLTAEILELAGNAARDNKKTRIIPRHLQLAIRNDEELNKLLGRVTIAQGGVLPNIQAVLLPKKTESHHKAKGK')
    peptides.write('\nMPDPSKSAPAPKKGSKKAVTKAQKKDGKKRKRGRKESYSIYVYKVLKQVHPDTGISSKAMGIMNSFVNDIFERIASEASRLAHYNKRSTITSREVQTAVRLLLPGELAKHAVSEGTKAVTKYTSSK')
    peptides.write('\nMARTKQTARKSTGGKAPRKQLATKVARKSAPATGGVKKPHRYRPGTVALREIRRYQKSTELLIRKLPFQRLMREIAQDFKTDLRFQSSAVMALQEACESYLVGLFEDTNLCVIHAKR')
    peptides.close()


if __name__ == '__main__':
    """Call main(). Do not modify this block."""
    main()
