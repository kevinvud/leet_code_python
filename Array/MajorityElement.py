"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2


"""

def majorityElement(input):

    count = 0
    candidate = 0

    for index in input:
        if count == 0:
            candidate = index
        count += 1 if candidate == index else -1

    return candidate


def majorityElemenMoreSpace(input):

    temp_dict = {}

    for index in input:
        if index not in temp_dict:
            temp_dict[index] = 1
        else:
            temp_dict[index] += 1

    maxCount = None
    keyCount = None

    for key, val in temp_dict.items():
        if maxCount == None and keyCount == None:
            maxCount = val
            keyCount = key
        else:
            if val > maxCount:
                maxCount = val
                keyCount = key
    return keyCount


arrayInput = [3,1,2,4,3,3,2,4]
print(majorityElement(input=arrayInput))
print(majorityElemenMoreSpace(input=arrayInput))



