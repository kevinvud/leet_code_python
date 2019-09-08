"""
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

"""

def sortArrayByParity(input):

    even_array = []
    odd_array = []

    for index in input:
        if index % 2 == 0:
            even_array.append(index)
        else:
            odd_array.append(index)
    return even_array + odd_array

arrayInput = [3,1,2,4]
print(sortArrayByParity(input=arrayInput))



