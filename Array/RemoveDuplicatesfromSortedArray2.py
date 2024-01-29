"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.

"""

def removeDuplicateFromSortedArray2(inputArray):

    if len(inputArray) == 0 or len(inputArray) == 1:
        return len(inputArray)

    counter = 1

    for i in range(2, len(inputArray)):
        if inputArray[counter] != inputArray[i] or inputArray[counter] != inputArray[counter - 1]:
            counter += 1
            inputArray[counter] = inputArray[i]

    return inputArray

input = [[1,1,2], [1,1,1,2,3], [0,1,1,1,1,2,3,3], [0,0,0,1,1,1,2,2,3,3,4,4]]

for index in input:
    print(removeDuplicateFromSortedArray2(index))
      