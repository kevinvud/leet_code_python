"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

"""

rowOne = "qwertyuiop"
rowTwo = "asdfghjkl"
rowThree = "zxcvbnm"

def keyboardRow(input):

    out_put = []
    for index in input:
        letter_counter = len(index)
        initial_counter = 0
        is_contain_letter_from_row_1 = False
        is_contain_letter_from_row_2 = False
        for letter in index:
            if letter.lower() in rowOne:
                initial_counter += 1
                is_contain_letter_from_row_1 = True
            elif letter.lower() in rowTwo and not is_contain_letter_from_row_1:
                is_contain_letter_from_row_2 = True
                initial_counter += 1
            elif letter.lower() in rowThree and not is_contain_letter_from_row_2 and not is_contain_letter_from_row_1:
                initial_counter += 1
        if initial_counter == letter_counter:
            out_put.append(index)
    return out_put


input_array = ["Yum","Hello", "Alaska", "Dad", "Peace"]

print(keyboardRow(input=input_array))




