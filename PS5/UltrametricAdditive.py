from compsci260lib import *

def solve_ultrametric_additive():
    """
    Given distance metrics, determine if they are ultrametric and/or additive.
    """

    # Distance metrics for table 1 and table 2
    dist_1 = {"1,2": 0.3, "1,3": 0.7, "1,4": 0.9,
              "2,3": 0.6, "2,4": 0.8,
              "3,4": 0.6}  # fill in table 1 here

    dist_2 = {"1,2": 0.8, "1,3": 0.4, "1,4": 0.6, "1,5": 0.8,
              "2,3": 0.8, "2,4": 0.8, "2,5": 0.4,
              "3,4": 0.6, "3,5": 0.8,
              "4,5": 0.8}

    # Check if dist_1 and dist_2 are ultrametric and additive by
    # calling is_ultrametric and is_additive with the default
    # threshold value (1e-4).
    #
    # Your code here
    print('dist_1 is ultrametric:', is_ultrametric(dist_1,threshold=1e-4))
    print('dist_2 is ultrametric:', is_ultrametric(dist_2,threshold=1e-4))
    print('dist_1 is additive:', is_additive(dist_1, threshold=1e-4))
    print('dist_2 is additive:', is_additive(dist_2, threshold=1e-4))

    # Construct the ATPA synthase distance metric table
    atpa_table = {"HUMAN,ECOLI": 0.5, "HUMAN,BACCE": 0.5, "HUMAN,MOUSE": 0.1, "HUMAN,YEAST": 0.4, "HUMAN,SCHPO": 0.4,
                  "ECOLI,BACCE": 0.3, "ECOLI,MOUSE": 0.5, "ECOLI,YEAST": 0.5, "ECOLI,SCHPO": 0.5,
                  "BACCE,MOUSE": 0.5, "BACCE,YEAST": 0.5, "BACCE,SCHPO": 0.5,
                  "MOUSE,YEAST": 0.4, "MOUSE,SCHPO": 0.4,
                  "YEAST,SCHPO": 0.3} #  fill in ATPA synthase distance metric table

    # Determine if the ATPA synthase distance metrics
    # are ultrametric and additive
    #
    # Your code here
    print('atpa_table is ultrametric:', is_ultrametric(atpa_table))
    print('atpa_table is additive:', is_additive(atpa_table))


def is_ultrametric(dist, threshold=1e-4):
    """Check that a set of pairs of point distances are ultrametric.

    Note: When making comparisons between distances, use `is_almost_equal` with
    the input parameterized threshold. This will be useful for subsequent
    problems where `is_ultrametric` is called.

    Args:
        dist (dict): exhaustive dict of pairs of points mapped to distances. 
        e.g.
            {"1,2" : 0.5, "1,3" : 0.1, "2,3" : 0.6}
        threshold (float): maximium difference in which numeric values are 
            considered equal
    Returns:
        (bool) True if the given distance metric is an ultrametric,
    False otherwise."""

    """YOUR CODE GOES HERE..."""
    keys = list(dist.keys())
    keys = (str(keys)[1:-1])
    keys = keys.replace("'", '')
    keys = keys.replace(", ",",")
    keys = keys.split(",")
    keys = list(dict.fromkeys(keys))
    maxIndice = len(keys)
    distanceList = []

    for i in range (0, maxIndice):
        for j in range (0, maxIndice):
            for k in range (0, maxIndice):
                if ((i != j) and (i != k) and (j != k)) and (i < j < k):
                    dist1 = dist['%s,%s' %(keys[i],keys[j])]
                    dist2 = dist['%s,%s' %(keys[i],keys[k])]
                    dist3 = dist['%s,%s' %(keys[j],keys[k])]
                    distanceList.append(dist1)
                    distanceList.append(dist2)
                    distanceList.append(dist3)
                    maxDist = max(distanceList)
                    maxDistIndex = distanceList.index(maxDist)
                    minDist = min(distanceList)
                    minDistIndex = distanceList.index(minDist)
                    if (minDistIndex == 0 and maxDistIndex == 1) or (minDistIndex  == 1 and maxDistIndex == 0):
                        midDist = distanceList[2]
                    elif (minDistIndex == 1 and maxDistIndex == 2) or (minDistIndex == 2 and maxDistIndex == 1):
                        midDist = distanceList[0]
                    elif (minDistIndex == 0 and maxDistIndex == 2) or (minDistIndex == 2 and maxDistIndex == 0):
                        midDist = distanceList[1]
                    distanceList = []

    # print(minDist <= max(midDist, maxDist) and is_almost_equal(midDist,maxDist))
    return minDist <= max(midDist, maxDist) and is_almost_equal(midDist,maxDist)



def is_additive(dist, threshold=1e-4):
    """Check that a set of pairs of point distances are additive.

    Note: When making comparisons between distances, use `is_almost_equal` with
    the input parameterized threshold. This will be useful for subsequent
    problems where `is_ultrametric` is called.

    Args:
        dist (dict): exhaustive dict of pairs of points mapped to distances. 
        e.g.
            {"1,2" : 0.5, "1,3" : 0.1, "2,3" : 0.6}
        threshold (float): maximium difference in which numeric values are 
            considered equal

    Returns:
        (bool) Return True if the given distance metric is additive, 
        False otherwise."""

    """YOUR CODE GOES HERE..."""
    '''Three ways to group [1-2|3-4] [1-3|2-4] [1-4|2-3]'''
    keys = list(dist.keys())
    keys = (str(keys)[1:-1])
    keys = keys.replace("'", '')
    keys = keys.replace(", ",",")
    keys = keys.split(",")
    keys = list(dict.fromkeys(keys))
    maxIndice = len(keys)
    sumList = []

    for i in range(0, maxIndice):
        for j in range(0, maxIndice):
            for k in range(0, maxIndice):
                for l in range(0, maxIndice):
                    if (i != j) and (i != k) and (i != l) and (j != k) and (j != l) and (k != l):
                        if (i < j) and (i < k) and (i < l) and (j < k) and (j < l) and (k < l):
                            sum1 = round((dist['%s,%s' % (keys[i], keys[j])] + dist['%s,%s' % (keys[k], keys[l])]),1)
                            sum2 = round((dist['%s,%s' % (keys[i], keys[k])] + dist['%s,%s' % (keys[j], keys[l])]),1)
                            sum3 = round((dist['%s,%s' % (keys[i], keys[l])] + dist['%s,%s' % (keys[j], keys[k])]),1)
                            sumList.append(sum1)
                            sumList.append(sum2)
                            sumList.append(sum3)
                            maxSum = max(sumList)
                            maxSumIndex = sumList.index(maxSum)
                            minSum = min(sumList)
                            minSumIndex = sumList.index(minSum)
                            if (minSumIndex == 0 and maxSumIndex == 1) or (minSumIndex == 1 and maxSumIndex == 0):
                                midSum = sumList[2]
                            elif (minSumIndex == 1 and maxSumIndex == 2) or (minSumIndex == 2 and maxSumIndex == 1):
                                midSum = sumList[0]
                            elif (minSumIndex == 0 and maxSumIndex == 2) or (minSumIndex == 2 and maxSumIndex == 0):
                                midSum = sumList[1]
                            sumList = []

    # print(minSum <= max(midSum, maxSum) and is_almost_equal(midSum, maxSum))
    return minSum <= max(midSum, maxSum) and is_almost_equal(midSum, maxSum)




def is_almost_equal(num_1, num_2, threshold=0):
    """Return true if the difference between the two parameters is negligible
    enough that the parameters can be considered equal.

    Args:
        num_1 (float/int): numeric value to compare
        num_2 (float/int): numeric value to compare
        threshold (float): maximium difference in which numeric values are 
            considered equal

    Returns:
        (bool): true if the numeric values are within the threshold
    """
    return abs(num_1 - num_2) <= threshold


if __name__ == '__main__':
    solve_ultrametric_additive()