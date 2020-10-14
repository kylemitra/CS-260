from compsci260lib import *
import textwrap
import random


def solve_language(file_name, order, num_outtext):
    """Create a Markov model for a given text file and output artificially
    generated text from the model.

    Args:
        file_name (str): path of the text to process
        order (int): order of the Markov model
        num_outtext (int): number of output texts to generate
    """

    # Read the contents of the file
    f = open(file_name, 'r')

    if f is None:
        print("Can't open " + file_name)
    else:
        contents = f.read()
        f.close()
        contents = contents.replace("\n", "")
        contents = contents.replace("\r", "")

    # This dictionary will store all the data needed to estimate the Markov
    # model:
    txt_dict = {}

    # Step 1: Count up occurrences of the various k-tuples in the training text
    print("Building dict of k-tuples and their counts...")
    build_dict(contents, order, txt_dict)

    # Step 2: Collect the counts necessary to estimate transition probabilities
    txt_dict = {}
    print("Collecting counts to estimate transition probabilities...")
    collect_counts(contents, order, txt_dict)
    display_dict(txt_dict)

    # Step 3: Generate artificial text from the trained model
    for _ in range(num_outtext):
        seed = contents[0:order]
        M = 1000
        next_character = ""
        text = seed

        print("\nOne version of the story is:")

        # Display my story
        for _ in range(M):
            next_character = generate_next_character(seed, txt_dict)
            text += next_character
            seed = seed[1:] + next_character

        text_list = textwrap.wrap(text, 72)
        text = "\n".join(text_list)
        print(text)


def display_dict(txt_dict):
    """Print the text dictionary as a table.

    This will need to be modified to handle the dictionary formatting described
    in collect_counts
    """
    #ORIGINAL
    # print("key\tcount ")
    # for key in txt_dict:
    #     print("%s\t%d " % (key, txt_dict[key]))

    #MODIFIED
    print("key\tcount\tfollowers ")
    for key in txt_dict:
        print("%s\t%d\t%s" % (key, txt_dict[key]['count'], txt_dict[key]['followers']))


def build_dict(contents, k, txt_dict):
    """Builds a dictionary of k-character (k-tuple) substring counts. Store the
    dictionary into the mutable argument txt_dict as a mapping from the k-tuple
    to an integer count. txt_dict's contents at the end of the function with
    k=2 will look something like this:

        { 'ac': 1, 'cg': 2, ... }

    Args:
        contents (str): the string contents of to count
        k (int): number of characters in the substring
        txt_dict (dict): mutable dictionary to store the k-character counts
    """

    '''YOUR CODE HERE...'''
    for i in range (0,len(contents)-k):
        dictKey = ''
        for j in range (0,k):
            dictKey += str(contents[i+j])
        if dictKey in txt_dict:
            txt_dict[dictKey] += 1
        else:
            txt_dict[dictKey] = 1

def collect_counts(contents, k, txt_dict):
    """Modify k-tuple dictionary to a mapping from k-tuple to a dictionary of
    of counts and dictionary of follower counts. txt_dict's contents at the
    end of the function will look something like this:
        {
            'ac': {
                'count': 1,
                'followers': { 'g': 1, 'c': 2}
            },
            ...
        }

    Args:
        contents (str): the string contents of to count
        k (int): number of characters in the substring
        txt_dict (dict): mutable dictionary to store the k-character counts
    """

    '''YOUR CODE HERE...'''
    for i in range (0,len(contents)-k):
        dictKey = ''
        for j in range (0,k):
            dictKey += str(contents[i+j])
        if dictKey in txt_dict:
            txt_dict[dictKey]['count'] += 1
            if contents[i+k] in txt_dict[dictKey]['followers']:
                txt_dict[dictKey]['followers'][contents[i+k]] += 1
            else:
                txt_dict[dictKey]['followers'].update({contents[i + k]: 1})
        else:
            txt_dict[dictKey] = {}
            txt_dict[dictKey].update({'count': 0, 'followers': {}})
            txt_dict[dictKey].update({'count': 1})
            txt_dict[dictKey]['followers'].update({contents[i+k]: 1})



def generate_next_character(seed, txt_dict):
    """Randomly select the next character of a k-tuple using the follower
    counts to determine the probability.

    Args:
        seed (str): k-tuple to follow from
        txt_dict (dict): k-tuple count follower dictionary

    Returns:
        (str) of the next character
    """

    '''YOUR CODE HERE...'''
    seedList = list(seed)
    newDict = txt_dict[seed]['followers']
    keyList = list(newDict.keys())
    charList = []

    for i in range(0, len(keyList)):
        counter = newDict[keyList[i]]
        while counter != 0:
            charList.append(keyList[i])
            counter = counter - 1

    randomChar = random.choice(charList)
    # nextChar = str(seedList[len(seedList)-1]) + str(randomChar)
    # print(nextChar)
    return randomChar



def main():
    """Call `solve_language` with the provided parameters."""
    file_name = "tidy.paradise.lost.txt"
    order = 4
    num_outtext = 1
    solve_language(file_name, order, num_outtext)


if __name__ == '__main__':
    """Main method call, do not modify."""
    main()
