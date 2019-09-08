"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

"""



def majorityElement2(input):

    num0 = None
    num1 = None
    count0 = 0
    count1 = 0
    output = []

    for num in input:
        if num0 != None and num0 == num:
            count0 += 1
        elif num1 != None and num1 == num:
            count1 += 1
        elif count0 == 0:
            num0 = num
            count0 = 1
        elif count1 == 0:
            num1 = num
            count1 = 1
        else:
            count0 -= 1
            count1 -= 1

    count0 = 0
    count1 = 0

    for num in input:
        if num == num0:
            count0 += 1
        if num == num1:
            count1 += 1

    if count0 > len(input) / 3:
        output.append(num0)
    if count1 > len(input) / 3:
        output.append(num1)

    if not output:
        return -1
    return output


arrayInput = [1,1,1,3,3,2,2,2,4,4,4,4]
print(majorityElement2(input=arrayInput))



