'''
@author: Kyle Mitra
@date: 9/20/19

@note:

'''

from compsci260lib import *
import timeit
import random


def brute_force(score_list):
    """Get the maximum similarity score using brute force.

    Args: score_list (list): list of integer similarity scores

    Returns: (int) of the maximal computed score
    """
    scores = 0;
    movingIndex = 0;
    allScores = []
    maxScores = []
    # print(score_list)
    maxIndex = len(score_list)-1
    while movingIndex < maxIndex:
        for i in range(movingIndex,maxIndex):
            scores = scores + score_list[i]
            allScores.append(scores)
            if len(allScores) == (maxIndex-movingIndex):
                maxScores.append(max(allScores))
                movingIndex = movingIndex + 1
                allScores = []
                scores = 0
    maxScore = max(maxScores)
    print (maxScore)
    return maxScore  # replace with the computed maximal score


def divide_conquer(score_list):
    """Get the maximum similarity score using divide and conquer.

    Args: score_list (list): list of integer similarity scores

    Returns: (int) of the maximal computed score
    """
    start = 0
    end = len(score_list) - 1
    if start == end:
        return score_list[start]

    middle = end // 2

    leftsum = float('-inf')
    sum = 0

    for i in range(middle,start,-1):
        sum = sum + score_list[i]
        if (sum > leftsum):
            leftsum = sum

    rightsum = float('-inf')
    sum2 = 0

    for i in range(middle+1,end+1,+1):
        sum2 = sum2+score_list[i]
        if (sum2>rightsum):
            rightsum = sum2

    fullSum = leftsum + rightsum

    leftMid = middle // 2
    leftsum2 = float('-inf')
    sum3 = 0

    for i in range(leftMid, start, -1):
        sum3 = sum3 + score_list[i]
        if (sum3 > leftsum2):
            leftsum2 = sum3

    rightsum2 = float('-inf')
    sum4 = 0

    for i in range(leftMid + 1, middle + 1, +1):
        sum4 = sum4 + score_list[i]
        if (sum4 > rightsum2):
            rightsum2 = sum4

    leftFullSum = leftsum2 + rightsum2

    rightMid = middle + (middle // 2)
    leftsum3 = float('-inf')
    sum5 = 0

    for i in range(rightMid, middle, -1):
        sum5 = sum5 + score_list[i]
        if (sum5 > leftsum3):
            leftsum3 = sum5

    rightsum3 = float('-inf')
    sum6 = 0

    for i in range(end + 1, rightMid + 1, +1):
        sum6 = sum6 + score_list[i]
        if (sum6 > rightsum3):
            rightsum3 = sum6

    rightFullSum = leftsum3 + rightsum3

    maxVal = max(fullSum, rightFullSum, leftFullSum)
    return maxVal  # replace with the computed maximal score

def linear(score_list):
    """Get the maximum similarity score in linear time.

    Args: score_list (list): list of integer similarity scores

    Returns: (int) of the maximal computed score
    """
    maxIncludingHere = maxSoFar = 0
    for i in score_list:
        maxSoFar = max(maxSoFar + i, 0)
        maxIncludingHere = max(maxIncludingHere, maxSoFar)
    # print(maxIncludingHere)

    return maxIncludingHere  # replace with the computed maximal score


if __name__ == '__main__':
    """You can use this to test the correctness of your code by using
    sample_list as an input to each function."""

    sample_list = [2, -3, -4, 4, 8, -2, -1, 1, 10, -5]

    brute_force(sample_list)
    divide_conquer(sample_list)
    linear(sample_list)

    """ This part below is used to test the runtime of your code, an example is
    given below for brute force algorithm with a random list of length 100.
    You will have to measure the runtime of each algorithm on every input size
    given in the problem set. """

    # allowed_scores = [i for i in range(-10,11)]
    # random_list = [random.choice(allowed_scores) for x in range(100000000)]
    # bruteforce_runtime = timeit.timeit('brute_force(random_list)',
    #     setup="from __main__ import brute_force, random_list", number=1)
    # print(bruteforce_runtime)
    # divide_runtime = timeit.timeit('divide_conquer(random_list)',
    #     setup="from __main__ import divide_conquer, random_list", number=1)
    # print(divide_runtime)
    # linear_runtime = timeit.timeit('linear(random_list)',
    #     setup="from __main__ import linear, random_list", number=1)
    # print(linear_runtime)