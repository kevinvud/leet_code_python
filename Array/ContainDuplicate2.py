"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""

def containDuplicate2(inputArray, k):

    dict_count = {}
    diff = 0
    for index, value in enumerate(inputArray):
        if value not in dict_count:
            dict_count[value] = index
        else:
            if abs(index - k) == dict_count[value]:
                return True
            else:
                if abs(index - k) >= k:
                    dict_count[value] = index
    return False


input = [[1,2,3,1], [1,0,1,1], [1,2,3,1,2,3]]

inputK = [3, 3, 2]

for index in range(len(input)):
    print("Result using dictionary: {}".format(containDuplicate2(inputArray=input[index], k=inputK[index])))