"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

def containDuplicate(inputArray):


    dict_count = {}
    for index in inputArray:
        if index not in dict_count:
            dict_count[index] = 1
        else:
            dict_count[index] += 1

    for key, value in dict_count.items():
        if value > 1:
            return True

    return False

def containDuplicateUsingSet(inputArray):

    inputToSet = set(inputArray)

    return len(inputToSet) != len(inputArray)



input =[[1,1,1,3,3,4,3,2,4,2], [1,2,3,1], [1,2,3,4]]

for index in input:
    print("Result using dictionary: {}".format(containDuplicate(index)))
    print("Result using set: {}".format(containDuplicateUsingSet(index)))



