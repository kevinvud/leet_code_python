# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# #
# # You may assume that each input would have exactly one solution, and you may not use the same element twice.
# #
# # Example:
# #
# # Given nums = [2, 7, 11, 15], target = 9,
# #
# # Because nums[0] + nums[1] = 2 + 7 = 9,
# # return [0, 1].


def fizzBuzz(nums = [2, 3, 11, 7], target = 19):

    if not nums or not target:
        return

    dict = {}
    for index, val in enumerate(nums):
        if not dict:
            dict.update({val: index})
        number_to_look = target - val
        if number_to_look in dict:
            return [dict[number_to_look], index]
        else:
            dict.update({val: index})
    return []

print(fizzBuzz())