
"""Floyd’s Triangle is a triangular array of numbers named after Robert Floyd. In this pattern, consecutive numbers
are printed in a right-angled triangular shape. It starts with 1 in the first row and increments by 1 in each
subsequent row"""
"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""

def floyd_triagnle_two(number_of_rows=3):
    start_num = 1
    counter = 0
    for n in range(1, number_of_rows + 1):
        for m in range(1, n + 1):
            print(m, end=" ")
        print()



def floyd_triangle(number_of_rows=1):
    start_num = 1
    start_index = 0
    while start_index < number_of_rows:
        for i in range(0, start_num):
            print(start_num, end=" ")
            start_num += 1
        print()
        start_index += 1

floyd_triagnle_two(number_of_rows=5)