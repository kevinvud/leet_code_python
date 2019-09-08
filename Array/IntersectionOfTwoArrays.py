"""


Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

"""

def intersectionTwoArrays(nums1, nums2):

    output = []
    for index in nums1:
        if index in nums2 and index not in output:
            output.append(index)
    return output


# Use Set

def intersectionTwoArraysWithSet(nums1, nums2):

    set1 = set(nums1)
    set2 = set(nums2)

    return list(set1.intersection(set2))


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
print(intersectionTwoArrays(nums1, nums2))
print(intersectionTwoArrays(nums3, nums4))

print(intersectionTwoArraysWithSet(nums1, nums2))
print(intersectionTwoArraysWithSet(nums3, nums4))


