# -*- coding: utf-8 -*-
"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Answer: 

logic, brute force

"""
import time

def diffSumSquares(start, end):
    start_time = time.time()
    sumSquared = 0
    squaresSummed = 0
    difference = 0

    for x in range(start, end + 1):
        squaresSummed = squaresSummed + x*x
        sumSquared = sumSquared + x
    sumSquared = sumSquared * sumSquared

    difference = sumSquared - squaresSummed
    print time.time() - start_time, "seconds"
    return difference
    

        
