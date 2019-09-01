"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""


def firstUniqueChar(input="leetcode"):

    letter_count_dict = {}

    for letter in input:
        if letter in letter_count_dict:
            letter_count_dict[letter] += 1
        else:
            letter_count_dict[letter] = 1

    for key, value in letter_count_dict.items():
        if value == 1:
            return input.index(key)

print(firstUniqueChar(input="loveleetcode"))
print(firstUniqueChar())

