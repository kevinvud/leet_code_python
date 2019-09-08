"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

"""



def validPalindrome2(input):
    return validPalindrome(input, 0, len(input) - 1)


def validPalindrome(input, initialIndex, inputLen, alreadyRemoved = False):

    inputLen = inputLen
    initialIndex = initialIndex

    while initialIndex < inputLen:
        if input[initialIndex] != input[inputLen]:
            if alreadyRemoved:
                return False
            else:
                return validPalindrome(input, initialIndex + 1, inputLen, alreadyRemoved=True) or validPalindrome(input, initialIndex, inputLen - 1, alreadyRemoved=True)
        else:
            initialIndex += 1
            inputLen -= 1
    return True

input = "abca"

print(validPalindrome2(input=input))




