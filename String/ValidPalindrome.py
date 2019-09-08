"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

"""
import re

# def validPalindrome(input= "race a car"):
#
#     # regex pattern
#     pattern = re.compile('\W')
#
#     input = input.lower()
#     input = re.sub(pattern,'',input)
#     MIDDLE_INDEX = int(len(input) / 2)
#     inputLen = len(input)
#     initialIndex = 0
#
#     while initialIndex <= MIDDLE_INDEX and MIDDLE_INDEX < inputLen:
#         if input[initialIndex] != input[inputLen - 1]:
#             return False
#         initialIndex += 1
#         inputLen -= 1
#     return True


def validPalindrome(input= "race a car"):

    # regex pattern
    pattern = re.compile('\W')

    input = input.lower()
    input = re.sub(pattern,'',input)
    inputLen = len(input) - 1
    initialIndex = 0

    while initialIndex < inputLen:
        if input[initialIndex] != input[inputLen]:
            return False
        initialIndex += 1
        inputLen -= 1
    return True

inputString = "A man, a plan, a canal: Panama"
print(validPalindrome(input=inputString))




