'''
@author: YM, JZ, AJH
@date: originally 4-9-13, with subsequent edits

@note: Learning Python dictionary manipulations
'''


def play_with_dictionary():
    """In this tutorial, you will learn some of the basic features of a Python dictionary"""

    # baby_words_freq is a dictionary of baby words to frequency
baby_words_freq = {"goo": 5, "mama": 20,
                       "wa": 3, "dada": 4, "cookie monster": 3}

    # 1. check if "zzz" exists in dictionary keys
print('zzz' in baby_words_freq)
    # 2. find the most commonly used baby word

    # 3. return a list of keys unordered
print(list(baby_words_freq.keys()))
    # 4. return a list of values unordered
print(list(baby_words_freq.values()))
    # 5. return a list of keys sorted by ascending values
print(baby_words_freq, key=baby_words_freq.get)
    # 6. return a list of keys sorted by descending values

    # 7. add the key "chuchu" with value 1
baby_words_freq["chuchu"] = 1
print  (baby_words_freq)
    # 8. delete the key "wa" from the dictionary
del baby_words_freq["wa"]
    # 9. duplicate the dictionary
dict2 = baby_words_freq
print (dict2)
    # 10. increment the value of "goo" by 1
baby_words_freq["goo"] = 6
print (baby_words_freq)
    # 11. print the dictionary key-value pairs
print(baby_words_freq)

if __name__ == '__main__':
    play_with_dictionary()
