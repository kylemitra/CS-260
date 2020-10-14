'''
@author: YM
@date: originally 4-23-13, with subsequent edits

@note: multidimensional arrays
'''

from pprint import *


def play_with_stuff():
    """In this tutorial, you will learn about multidimensional arrays in Python """

    # try to the following exercises as Pythonically as possible...
    # all these exercises will help you later in your problem sets

    # 1. create a 1D array with 10 elements, each with value 0

    # 2. create a 2D array of 10 x 10 elements, each with value 0

    # 3. create a 3D array of 10 x 10 x 10 elements, each with value of 0
    # NOTE: Python requires that you instantiate your list elements before you can use them

    # 4. import the pprint() function from the pprint module to print out the arrays you have just created

    # 5. alternatively, use str() function to print out all three arrays

    # 6. iterate backwards in the 1D array, setting each value in the array to the number of the step you
    #   are currently executing (i.e. the array should look like this [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    # 7. iterate forward every element (rows by cols) in the 2D array and set every value to pos infinity
    # NOTE: in Python, positvie infinity can be assigned with the value float("inf") or negative infinity with the value float("-inf")

    # 8. iterate backwards in the 3D array. set all odd indices ((x + y + z) %2 ==1) to neg inf and all even indices to pos inf


if __name__ == '__main__':
    play_with_stuff()
