from compsci260lib import *
from math import sqrt


def solve_k_nearest(input_patients, new_patients):
    """
    Read in the input patients as training data to use to determine and report
    the prognosis of the 10 new patients.

    Args:
        input_patients (list of dicts): dictionaries of training patient
            data. see: `read_training_data`

        new_patients (list of dicts): dictionaries of test patient data.
            see: `read_test_data`
    """
    """YOUR CODE GOES HERE..."""
    valTracker = []
    locationTracker = []
    newCalcDist = 0
    indexToBeReplaced = 0
    nCounter = 0
    rCounter = 0

    # for j in range(0, 1):
    for j in range(0, len(new_patients)):
        for i in range(0, len(input_patients)):
            newCalcDist = compute_dist(input_patients[i]['expression'], new_patients[j]['expression'])
            if len(valTracker) < 5:
                valTracker.append(newCalcDist)
                locationTracker.append(i)
            if len(valTracker) == 5:
                if newCalcDist < max(valTracker):
                    indexToBeReplaced = valTracker.index(max(valTracker))
                    valTracker[indexToBeReplaced] = newCalcDist
                    locationTracker[indexToBeReplaced] = i

        for x in range(0, len(valTracker)):
            if input_patients[locationTracker[x]]['class'] == 'N':
                nCounter += 1
            if input_patients[locationTracker[x]]['class'] == 'R':
                rCounter += 1

        if nCounter > rCounter:
            new_patients[j]['class'] = 'N'
        if rCounter > nCounter:
            new_patients[j]['class'] = 'R'

        nCounter = 0
        rCounter = 0
        valTracker = []
        locationTracker = []
        newCalcDist = 0
        indexToBeReplaced = 0

    print(new_patients)


def read_training_data(file_name):
    """Read the training gene expression data from a text file. Note: the
    patients in the training data are classified as "R" (responsive to
    treatment) or "N" (non-responsive to treatment).  For example,
    input_patients[0]["class"] = the class of the first patient (R or N)
    input_patients[0]["expression"][0] = the expression of the first
    gene for the first patient.

    Returns:
        (list of dicts): list of patients as a class and expression data. The
        dictionary of each patient will be in the form of:
            'class' -> string with values strictly 'N' or 'R' for
            non-responsive or responsive to the treatment
            'expression' -> list of floats of gene expression values

        and look something like:
            {'class': 'N', 'expression': [9.049, 8.313, ..., 6.428700888]}
    """
    '''Training Data is database of gene expression values for all 10 biomarker genes
     for 1000 patients who responded to treatment (class R) and 1000 patients who were 
     non-responsive (class N).'''

    f = open(file_name, "r")
    if f is None:
        sys.stderr("File " + file_name + " does not exist")
    else:
        input_patients = []
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            # check if you are splitting on "\t" which is what you
            # want to split on
            data = line.split()
            class_name = data.pop(0)
            float_data = [float(datum) for datum in data]  # convert to float
            patient = {"class": class_name, "expression": float_data}
            input_patients.append(patient)
        f.close()
        # print('Patient input', input_patients)
        return input_patients


def read_test_data(file_name):
    """Read the test gene expression data from a text file. Note: the
    patients in the test data are not classified.

   Returns:
    (list of dicts): list of patients as a class and expression data. The
    dictionary of each patient will be in the form of:
        'class' -> string with only 'unknown' as its value
        'expression' -> list of floats of gene expression values

    and look something like:
        {'class': 'unknown', 'expression': [9.049, 8.313, ..., 6.428700888]}
    """
    '''Expression levels of the ten biomarker genes for each of the 10 patients'''

    f = open(file_name, "r")
    if f is None:
        sys.stderr("File " + file_name + " does not exist")
    else:
        test_patients = []
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            # check if you are splitting on "\t" which is what you want
            # to split on
            data = line.split()
            float_data = [float(datum) for datum in data]
            patient = {"class": "unknown", "expression": float_data}
            test_patients.append(patient)
        f.close()
        # print('Test Patient input', test_patients)
        return test_patients


def compute_dist(tuple_1, tuple_2):
    """Return the Euclidean distance between two points in any number of
    dimensions."""

    if len(tuple_1) != len(tuple_2):
        sys.stderr("Cannot compute Euclidean distance between tuples of "
                   "different sizes!")
    dist = 0
    for i in range(len(tuple_1)):
        dist += (tuple_1[i] - tuple_2[i]) * (tuple_1[i] - tuple_2[i])
    return sqrt(dist)


if __name__ == '__main__':
    input_patients = read_training_data("gene_expression_training_set.txt")
    new_patients = read_test_data("gene_expression_test_set.txt")
    solve_k_nearest(input_patients, new_patients)
