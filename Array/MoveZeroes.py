"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

def moveZeroes(input):

    # O(1) space complexity

    if not input:
        return []
    counter = 0
    for index in input:
        if index != 0:
            input[counter] = index
            counter += 1

    while counter < len(input):
        input[counter] = 0
        counter += 1

    return input


def moveZeroesMoreSpace(input):

    # O(n) space complexity

    output = []
    counter = 0
    for index in input:
        if index != 0:
            output.append(index)
            counter += 1

    while counter < len(input):
        output.append(0)
        counter += 1
    return output

input = [0,1,0,3,12,10,0,1]
print(moveZeroes(input=input))
print(moveZeroesMoreSpace(input=input))