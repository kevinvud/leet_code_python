"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

"""

def fizzBuzz(nRun = 15):

    output = []

    for index in range(1, nRun + 1):
        if index % 15 == 0:
            output.append('FizzBuzz')
        elif index % 3 == 0:
            output.append('Fizz')
        elif index % 5 == 0:
            output.append('Buzz')

        else:
            output.append('{}'.format(index))
    return output

print(fizzBuzz(nRun=15))
