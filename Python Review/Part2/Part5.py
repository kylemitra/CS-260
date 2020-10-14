'''
@author: YM
@date: originally 4-23-13, with subsequent edits

@note: Learning regular expressions with Python
'''

import re


def play_with_regex():
    """In this tutorial, you will learn some of the basic features of a Python regex library"""

    DNA_string = "ATTTGTATGTTCGGCTAACTTCTACCCATCCCCCGAAGTTTAGCAGGTCGTGAGGTGTCATGGAGGCTCTCGTTCATCCCGTGGGACATCAAGCTTCGCCTTGATAAAGCACCCCGCTCGGGTGTAGCAGAGAAGACGCCTACTGAATTGTGCGATCCCTCCACCTCAGCTAAGGTAGCTACCAATATTTAGTTTTTTAGCCTTGCGACAGACCTCCTACTTAGATTGCCACGCATTGAGCTAGCGAGTCAGCGATAAGCATGACGCGCTTTCAAGCGTCGCGAGTATGTGAACCAAGGCTCCGGACAGGACTATATACTTGGGTTTGATCTCGCCCCGACAACTGCAAACCTCAACATTTATAGATTATAAGGTTAGCCGAAATTGCACGTGGTGGCGCCCGCCGACTGCTCCCCGAGTGTGGCTCTTTGATCTGACAACGCGCGACCTCCATCGCGGCCGATTGTTTCTGCGGACCATGTCGTCCTCATAGTTTGGGCATGTTTCCGTTGTAGGAGTGAAGCCACTTAGCTTTGCGCCGTAGTCCCAATGAAAAACCTATGGACTTTGTTTTGGGTAGCATCAGGAATCTGAACCCTGTGAATGTGGGGGTCGCGCGCATAGACCTTTATCTCCGGTTCAAGTTAGGCATGAGGCTGCATGCTACGTTGTCACACCTACACTGCTCGAAGTAAATATGGGAAGCGCGCGGCCTGGCCCGAGGCGTTCCGCGCCGCCACGTGTTCGTTAACTGTTGATTGGTGGCACATAAGCAATACCGTAGTCCCTCAAATTCAGCTCTGTTATCTCGAGCGTTATGTGTCAAATGGCGTAGAACGGGATTGACTGTTTGACACTAGCTGGTGTTCGGTTCGGTAACGGAGAATCTGTGGGGCTATGTCACTAATACTTTCGAAACGCCCCGTACCGATGCTGAACAAGTCGATGCAGGCTCCCGTCTTTGAATAGGGGTAAACATACAAGTCGATAGAAGATGGGT"

    # 1. check if DNA_string starts with "ATTTGTATG" (say with re.search() or re.findall())

    # 2. use re.findall() to determine if there are instances of 5 or more consecutive C's in DNA_string

    # 3. find instances of the motif GGXY in the DNA sequence where X={A,C,G,T} and Y={C,T}
    # you may find re.finditer() to be more useful than re.findall()


if __name__ == '__main__':
    play_with_regex()