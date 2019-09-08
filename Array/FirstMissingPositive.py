"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

"""


def firstMissingPositive(input):
    if not input:
        return 1

    # remove all negative
    for neg in input:
        minN = min(input)
        if minN <= 0:
            input.pop(input.index(minN))
        else:
            break
    if not input:
        return 1

    sorted_input = sorted(input)

    for i in sorted_input:
        if 1 not in input:
            return 1
        elif i - 1 > 0 and i - 1 not in input:
            return i - 1
        elif i + 1 not in input:
            return i + 1


inputArray = [[7,8,9,11,12], [3,4,-1,1], [1,2,9,0,3]]
# inputArray = [[-3, -4, -1, 1, 2]]

for input in inputArray:
    print(firstMissingPositive(input=input))



