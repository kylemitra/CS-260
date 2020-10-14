'''
@author: Kyle Mitra
@date: 9/6/19

@note:

'''


from compsci260lib import *   # this will also import the sys and re modules


def solve_cloning():
    """Function demonstrating the procedure of extracting a gene and inserting
    into a plasmid using restriction enzymes."""

    aim2_fasta_path = 'aim2_plus_minus_1kb.fasta'
    pRS304_fasta_path = 'pRS304.fasta'

    # Read in the aim2 genomic sequence from the fasta file along with its
    # upstream and downstream regions.
    aim2_genomic = get_fasta_dict(aim2_fasta_path)
    print(aim2_genomic)
    # Store the beginning and the end of the Aim2 gene as Python indices.
    aim2_beg = None
    print(aim2_beg.start())
    # Your code goes here
    aim2_end = None  # Your code goes here

    # Define regular expression terms for each restriction enzyme
    r_enzymes = get_restriction_enzymes_regex()

    # Store coordinates of restriction sites found upstream, downstream, and
    # within the aim2 gene
    r_enzyme_sites = find_aim2_restriction_enzymes(
        aim2_beg, aim2_end, aim2_genomic)

    # Report the found restriction enzyme sites
    #
    # Your code goes here
    #

    # Input the pRS304 plasmid selecting the MCS
    # Store the MCS in a new variable.
    #
    # Your code goes here
    #
    mcs_start = None
    mcs_end = None
    prs304_mcs = None

    # Find and report the restriction enzymes in the MCS
    p_enzyme_sites = find_pRS304_MCS_restriction_sites(prs304_mcs, mcs_start)
    #
    # Your code goes here
    #

    # Extract aim2 gene and insert into the plasmid, report the length
    #
    # Your code goes here
    #


def get_restriction_enzymes_regex():
    """Returns a dictionary of restriction enzyme regular expressions for
    searching in genomic sequences.

    This function should be used for find_aim2_restriction_enzymes and
    find_pRS304_MCS_restriction_sites.
    """

    r_enzymes = {
        "BamHI": "<regular expression to identify BamHI site>",
        #
        # ...
        #
    }
    return r_enzymes


def find_aim2_restriction_enzymes(aim2_beg, aim2_end, aim2_genomic):
    """Finds the restriction enzyme sites in the aim2 genomic sequence. Stored
    as a dictionary of lists. Each restriction enzyme key corresponds to a list
    of dictionaries containing relevant information for a found site.

    Each found site will have defined keys:
        sequence (str): the nucleotide sequence matched in the genome
        start (int): the start nucleotide position in the genome
        end (int): the ending position
        location (str): the position of the site relative the aim2 gene.
            (must be "upstream", "downstream", or "within")

    A valid returned dictionary may look like this:
    {
        'BamHI' : [
            {
                'start': 10,
                'end': 15,
                'sequence': 'GGATCC',
                'location': 'upstream'
            },
            {
                'start': 100,
                'end': 105,
                'sequence': 'GGATCC',
                'location': 'downstream'
            }
        ],
        'BstYI' : [
            {
                'start': 30,
                'end': 35,
                'sequence': 'AGATCC',
                'location': 'within'
            }
        ]
    }
    """

    # load restriction enzyme regular expressions
    r_enzymes = get_restriction_enzymes_regex()

    r_enzyme_sites = {"BamHI": [], "BstYI": [], "SpeI": [],
                      "SphI": [], "StyI": [], "SalI": []}

    # Your code goes here
    for

    return r_enzyme_sites


def find_pRS304_MCS_restriction_sites(prs304_mcs, mcs_start):
    """Finds the restriction sites for for the MCS of pRS304. Stored as a
    dictionary of lists. Each restriction enzyme key corresponds to a list of
    dictionaries containing relevant information for a found site in the MCS.

    Each found site will have defined keys:
        sequence (str): the nucleotide sequence matched in the MCS
        start (int): the start nucleotide position in the MCS
        end (int): the ending position in the MCS

    A valid returned dictionary may look like this:
    {
        'BamHI' : [
            {
                'start': 10,
                'end': 15,
                'sequence': 'GGATCC'
            },
            {
                'start': 100,
                'end': 105,
                'sequence': 'GGATCC'
            }
        ],
        'BstYI' : [
            {
                'start': 30,
                'end': 35,
                'sequence': 'AGATCC'
            }
        ]
    }
    """

    # load restriction enzyme regular expressions
    r_enzymes = get_restriction_enzymes_regex()

    p_enzyme_sites = {"BamHI": [], "BstYI": [], "SpeI": [],
                      "SphI": [], "StyI": [], "SalI": []}
    #
    # Your code goes here
    #

    return p_enzyme_sites


if __name__ == '__main__':
    solve_cloning()
