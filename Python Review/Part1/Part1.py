'''
@author: YM, JZ, AJH
@date: originally 4-23-13, with subsequent edits

@note: Learning Python string manipulations
'''


def play_with_string():
    """In this tutorial, you will learn some of the basic features of a Python string"""

DNA_string = "ATTTGTATGTTCGGCTAACTTCTACCCATCCCCCGAAGTTTAGCAGGTCGTGAGGTGTCATGGAGGAGCTCTCGTTCATCCCGTGGGACATCAAGCTTCGCCTTGATAAAGCACCCCGCTCGGGTGTAGCAGAGAAGACGCCTACTGAATTGTGCGATCCCTCCACCTCAGCTAAGGTAGCTACCAATATTTAGTTTTTTAGCCTTGCGACAGACCTCCTACTTAGATTGCCACGCATTGAGCTAGCGAGTCAGCGATAAGCATGACGCGCTTTCAAGCGTCGCGAGTATGTGAACCAAGGCTCCGGACAGGACTATATACTTGGGTTTGATCTCGCCCCGACAACTGCAAACCTCAACATTTATAGATTATAAGGTTAGCCGAAATTGCACGTGGTGGCGCCCGCCGACTGCTCCCCGAGTGTGGCTCTTTGATCTGACAACGCGCGACCTCCATCGCGGCCGATTGTTTCTGCGGACCATGTCGTCCTCATAGTTTGGGCATGTTTCCGTTGTAGGAGTGAAGCCACTTAGCTTTGCGCCGTAGTCCCAATGAAAAACCTATGGACTTTGTTTTGGGTAGCATCAGGAATCTGAACCCTGTGAATGTGGGGGTCGCGCGCATAGACCTTTATCTCCGGTTCAAGTTAGGCATGAGGCTGCATGCTACGTTGTCACACCTACACTGCTCGAAGTAAATATGGGAAGCGCGCGGCCTGGCCCGAGGCGTTCCGCGCCGCCACGTGTTCGTTAACTGTTGATTGGTGGCACATAAGCAATACCGTAGTCCCTCAAATTCAGCTCTGTTATCTCGAGCGTTATGTGTCAAATGGCGTAGAACGGGATTGACTGTTTGACACTAGCTGGTGTTCGGTTCGGTAACGGAGAATCTGTGGGGCTATGTCACTAATACTTTCGAAACGCCCCGTACCGATGCTGAACAAGTCGATGCAGGCTCCCGTCTTTGAATAGGGGTAAACATACAAGTCGATAGAAGATGGGT"

    # try to do the following exercises as Pythonically as possible...
    # all these exercises will help you later in your problem sets

    # 1. get the 3rd character of the DNA_string
print (DNA_string[2])
    # 2. copy the string using str() function (notice how this is different from simple assignment)
sequence = str(DNA_string)
print (sequence)
    # 2. remove the 3rd character from DNA_string
print (DNA_string[0:2] + DNA_string[3:])
    # 3. add the 3rd character back into its original position in DNA_string
print (DNA_string[0:2] + DNA_string[2] + DNA_string[3:])
    # 4. get the last 5 characters of DNA_string
print (DNA_string[-5:])
    # 5. get the first 20 characters of DNA_string
print (DNA_string[0:19])
    # 6. iterate through DNA_string one character at time
for x in DNA_string:
    print(x)
    # 7. How many times does the motif "GGAG" occur in the DNA sequence?
print(DNA_string.count('GGAG'))
    # 8. Use a formatted string to print the following string "a is 100, b is 120, and c is 140"
a = 100
b = 120
c = 140
print('a is %s, b is %s, and c is %s' % (a,b,c))
print('a is ' + str(a) + ', b is ' + str(b) + ', and c is ' + str(c))
    # 9. check if "GCAGGTCGTGAGGTGTCATGG" is a substring of DNA_string
DNA_string.find('GCAGGTCGTGAGGTGTCATGG')
DNA_string.count('GCAGGTCGTGAGGTGTCATGG')
DNA_string.index('GCAGGTCGTGAGGTGTCATGG')
    # 10. reverse DNA_string
print (DNA_string[::-1])

if __name__ == '__main__':
    play_with_string()
