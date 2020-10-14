
def make_survey_response_dict(course, python, editor):
    """
    Returns a response dictionary for the PS0 survey.

    Args:
        course (int): highest computer science class taken at Duke, as an integer
        python (int): confidence in your Python programming abilities, as an integer
                 (must be 0, 1, 2, or 3)
        editor (string): The Python editor you will be using, as a string
                 (e.g., PyCharm, Sublime Text, Atom, vim, etc.)

    Returns:
        dict: A dictionary with the pre-specified keys, and the answers
        to the survey questions as the values. The returned dictionary will
        look something like this:
        {
            'course': 101,
            'python': 1,
            'editor': "PyCharm"
        }
    """

    # Your code here

    return {}


def run_survey_response():
    """Constructs and reports the PS0 survey.

    Returns:
        The student's filled survey response dictionary
    """

    # Call the make_survey_response_dict procedure with your provided answers
    survey_response = make_survey_response_dict(None, None, None)

    # Report survey response as human-readable text to the console output
    #
    # Your code here
    #

    return survey_response  # Return your survey response (for autograding)


if __name__ == '__main__':
    run_survey_response()
