"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

"""


def removeDuplicateFromSortedArray(inputArray):

    output = []
    temp_holder = None
    counter = 0
    for num in inputArray:
        if temp_holder == None:
            temp_holder = num
            counter += 1
            output.append(num)
        else:
            if temp_holder != num:
                output.append(num)
                temp_holder = num

    return output


def removeDuplicateFromSortedArrayConstantSpace(inputArray):

    if len(inputArray) == 0 or len(inputArray) == 1:
        return len(inputArray)

    counter = 0

    for i in range(0, len(inputArray) - 1):
        if inputArray[i] != inputArray[i + 1]:
            inputArray[counter] = inputArray[i]
            counter += 1

    inputArray[counter] = inputArray[len(inputArray) - 1]

    return inputArray[:counter + 1]



input = [[1,1,2], [0,0,0,1,1,1,2,2,3,3,4,4]]

for index in input:
    print(removeDuplicateFromSortedArrayConstantSpace(index))