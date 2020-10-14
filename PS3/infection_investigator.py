from bwt import *
from read_aligner import *
from compsci260lib import *

def reverse_complement(seq):
    """Returns the reverse complement of the input string."""
    comp_bases = {'A': 'T',
                  'C': 'G',
                  'G': 'C',
                  'T': 'A'}
    rev_seq = list(seq)
    rev_seq = rev_seq[::-1]
    rev_seq = [comp_bases[base] for base in rev_seq]
    return ''.join(rev_seq)

###NEED TO FIX FILE IMPORTS
patient1Sequence = get_fasta_dict('patient1.fasta')
patient2Sequence = get_fasta_dict('patient2.fasta')
patient3Sequence = get_fasta_dict('patient3.fasta')

bOvatusSequence = get_fasta_dict('bacteroides_ovatus.fasta')
bOvatusSequence = bOvatusSequence['Bacteroides ovatus']

bOvatusInfo = make_all(bOvatusSequence)
bThetaSequence = get_fasta_dict('bacteroides_thetaiotaomicron.fasta')
bThetaSequence = bThetaSequence['Bacteroides thetaiotaomicron']
bThetaSequence = reverse_complement(bThetaSequence)
bThetaInfo = make_all(bThetaSequence)
bLongumSequence = get_fasta_dict('bifidobacterium_longum.fasta')
bLongumSequence = bLongumSequence['Bifidobacterium longum']
bLongumSequence = reverse_complement(bLongumSequence)
bLongumInfo = make_all(bLongumSequence)
eRectaleSequence = get_fasta_dict('eubacterium_rectale.fasta')
eRectaleSequence = eRectaleSequence['Eubacterium rectale']
eRectaleSequence = reverse_complement(eRectaleSequence)
eRectaleInfo = make_all(eRectaleSequence)
lAcidSequence = get_fasta_dict('lactobacillus_acidophilus.fasta')
lAcidSequence = lAcidSequence['Lactobacillus acidophilus']
lAcidSequence = reverse_complement(lAcidSequence)
lAcidInfo = make_all(lAcidSequence)
pTimoSequence = get_fasta_dict('peptoniphilus_timonensis.fasta')
pTimoSequence = pTimoSequence['Peptoniphilus timonensis']
pTimoSequence = reverse_complement(pTimoSequence)
pTimoInfo = make_all(pTimoSequence)
pCopriSequence = get_fasta_dict('prevotella_copri.fasta')
pCopriSequence = pCopriSequence['Prevotella copri']
pCopriSequence = reverse_complement(pCopriSequence)
pCopriInfo = make_all(pCopriSequence)
rIntestSequence = get_fasta_dict('roseburia_intestinalis.fasta')
rIntestSequence = rIntestSequence['Roseburia intestinalis']
rIntestSequence = reverse_complement(rIntestSequence)
rIntestInfo = make_all(rIntestSequence)
rBromiiSequence = get_fasta_dict('ruminococcus_bromii.fasta')
rBromiiSequence = rBromiiSequence['Ruminococcus bromii']
rBromiiSequence = reverse_complement(rBromiiSequence)
rBromiiInfo = make_all(rBromiiSequence)
vCholeraeSequence = get_fasta_dict('vibrio_cholerae.fasta')
vCholeraeSequence = vCholeraeSequence['Vibrio cholerae']
vCholeraeSequence = reverse_complement(vCholeraeSequence)
vCholeraeInfo = make_all(vCholeraeSequence)

def read_mapper(patient, bacteria):
    """For a given patient and bacterial species, return a vector which counts
    the number of the patient's reads which map to each of the locations in the
    reference genome for the bacterial species.

    Args:
        patient (str): The patient name. Can be either "patient1", "patient2",
                       or "patient3". This will be useful for loading your
                       patient prevalence files from disk as described in
                       part c.

        bacteria (str): of the bacteria name as named in the reference_genomes
                        folder. e.g. "Bacteroides_ovatus", "Vibrio_cholerae",
                        etc. This will be useful for loading the appropriate
                        reference genome fasta file from disk.

    Returns:
        (list of ints): vector of aligned read counts to the genome.
        i.e. [c_1, c_2, ..., c_i, ..., c_n], where n=length of the genome
        and c_i = the count of aligned reads for the patient at genome
        position i.
    """
    # Your code here

    return []


def longest_zeros(count_vector):
    """Given a count vector, return the start and stop position of the longest
    string of zeros in the vector.

    Args:
        count_vector (list of ints): vector of aligned read counts to the
        genome. see: the return value for `read_mapper()`

    Returns:
        (tuple of (int, int)): the start and stop position of the longest
        string of zeros in the count_vector.
    """
    # Your code here

    return (-1, -1)


def align_patient_reads(patientSequence, bacteriaSequence):
    """YOUR CODE GOES HERE..."""
    condensedPatientSequence = []
    totalFinds = []
    patientNum = 0
    if patientSequence == patient1Sequence:
        patientNum = 2
    if patientSequence == patient2Sequence:
        patientNum = 1
    if patientSequence == patient3Sequence:
        patientNum = 3

    for i in range(1,100):
        addRead = patientSequence['P%d|%d' % (patientNum, i)]
        condensedPatientSequence.append(addRead)

    for j in range(0, len(condensedPatientSequence) - 1):
        finds = find(condensedPatientSequence[j], bacteriaSequence)
        totalFinds.append(finds)
    return(totalFinds)

def microbe_prevalence(patientSequence):
    bOvatusReads = align_patient_reads(patientSequence, bOvatusInfo)
    numbOvatusReads = len(bOvatusReads)
    bThetaReads = align_patient_reads(patientSequence, bThetaInfo)
    numbThetaReads = len(bThetaReads)
    bLongumReads = align_patient_reads(patientSequence,bLongumInfo)
    numbLongumReads = len(bLongumReads)
    eRectaleReads = align_patient_reads(patientSequence, eRectaleInfo)
    numeRectaleReads = len(eRectaleReads)
    lAcidReads = align_patient_reads(patientSequence, lAcidInfo)
    numlAcidReads = len(lAcidReads)
    pTimoReads = align_patient_reads(patientSequence,pTimoInfo)
    numpTimoReads = len(pTimoReads)
    pCopriReads = align_patient_reads(patientSequence, pCopriInfo)
    numpCopriReads = len(pCopriReads)
    rIntestReads = align_patient_reads(patientSequence, rIntestInfo)
    numrIntestReads = len(rIntestReads)
    rBromiiReads = align_patient_reads(patientSequence, rBromiiInfo)
    numrBromiiReads = len(rBromiiReads)
    vCholeraeReads = align_patient_reads(patientSequence, vCholeraeInfo)
    numvCholeraeReads = len(vCholeraeReads)

    totalNumReads = numbOvatusReads + numbThetaReads + numbLongumReads + numeRectaleReads + numlAcidReads + numpTimoReads + numpCopriReads + numrIntestReads + numrBromiiReads + numvCholeraeReads

    bOvatusPrev = numbOvatusReads / totalNumReads
    print('Prevalence of bOvatus is', bOvatusPrev)
    bThetaPrev = numbThetaReads / totalNumReads
    print('Prevalence of bTheta is', bThetaPrev)
    bLongumPrev = numbLongumReads / totalNumReads
    print('Prevalence of bLongum is', bLongumPrev)
    eRectalePrev = numeRectaleReads / totalNumReads
    print('Prevalence of eRectale is', eRectalePrev)
    lAcidPrev = numlAcidReads /totalNumReads
    print('Prevalence of lAcid is', lAcidPrev)
    pTimoPrev = numpTimoReads / totalNumReads
    print('Prevalence of pTimo is', pTimoPrev)
    pCopriPrev = numpCopriReads / totalNumReads
    print('Prevalence of pCopri is', pCopriPrev)
    rBromiiPrev = numrBromiiReads / totalNumReads
    print('Prevalence of rBromii is', rBromiiPrev)
    vCholeraePrev = numvCholeraeReads / totalNumReads
    print('Prevalence of vCholerae is', vCholeraePrev)

if __name__ == '__main__':
    microbe_prevalence(patient3Sequence)