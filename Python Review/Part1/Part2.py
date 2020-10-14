'''
@author: YM, JZ, AJH
@date: originally 4-23-13, with subsequent edits

@note: Learning Python list manipulations
'''


def play_with_list():
    """In this tutorial, you will learn some of the basic features of a Python list"""

baby_words = ["goo", "mama", "wa", "dada", "cookie monster"]
mommy_words = ["hello", "dear", "love", "honey", "darling"]
    # try to do the following exercises as Pythonically as possible...
    # all these exercises will help you later in your problem sets

    # 1. check if "zzz" exists in baby_words
print ('zzz' in baby_words)
    # 2. use the sorted() function to sort baby_words and assign the result to another variable
baby_words2 = sorted(baby_words)
print (baby_words2)
    # 3. use the sort() method to sort baby_words (e.g. baby_words.sort()) and try to assign the result to another variable
baby_words3 = baby_words.sort()
#.sort function does not have an output
print (baby_words3)
    # 4. create a list named combined_words
combined_words = []
print (combined_words)
    # 5. iterate and use the append() function to add each baby word into combined_words
for item in baby_words:
    combined_words.append(item)
print (combined_words)
    # 6. use extend() function to add all mommy_words
combined_words.extend(mommy_words)
print (combined_words)
    # 7. delete the combined_words list using keyword del
del (combined_words)
    # 8. reassign combined_words to an empty list
combined_words = []
print (combined_words)
    # 9. use + operator to assign all the items in both lists to combined_words
combined_words = baby_words + mommy_words
print (combined_words)
    # 10. remove the first element of combined_words and save the element
element = combined_words[0]
print (element)
del combined_words[0]
print (combined_words)
    # 11. insert the saved element at the first position of combined_words
combined_words.insert(0,element)
print (combined_words)
    # 13. get sublist starting from the 3rd element to the end

    # 14. check if combined_words contains "dada"
print('dada' in combined_words)
    # 15. use list comprehension to add the string " baby" to each item in mommy_words
print(mommy_words + 'baby' for mommy_words in mommy_words)

if __name__ == '__main__':
    play_with_list()
