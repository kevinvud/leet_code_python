"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:

Input: "USA"
Output: True

Example 2:

Input: "FlaG"
Output: False


Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

"""

def detectCapital(input):

    if len(input) < 0:
        return False
    if input.islower():
        return True
    elif input.isupper():
        return True
    else:
        inputLen = len(input) - 1
        if input[inputLen].isupper():
            return False
        elif input[0].lower() or input[0].isupper():
            for index in range(1, len(input)):
                if input[index].isupper():
                    return False
        return True


input = ["USA", "FlaG", "Alex", "NaM", "TiNh"]
for index in input:
    print(detectCapital(index))
