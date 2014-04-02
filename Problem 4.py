# -*- coding: cp1252 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609

I'm going to try the brute force approach. Enumerate a 900x900 matrix, fill it
with products, then iterate through to find the palindromic numbers


"""

#fills a matrix with products of i x j
def fillMatrix():
    size = 900
    matrix = [[] for x in range(size)]
    i = 0
    j = 0
    for i in range(size):
        for j in range(size):
            matrix[i].append((i+100)*(j+100))
    return matrix

#tests to see if it is a palindromic number
def testPalin(n):
    num = str(n)
    x = len(num)
    if (x % 2) == 0:
        y = x / 2
        for i in range(y):
            if (num[i] != num[y*2 - 1 - i]):
                return False
    else:
        y = (x - 1) / 2
        for i in range(y):
            if (num[i] != num[y*2 - i]):
                return False
    return True

        

#finds largest palindromic number
def findPalin():
    maxPalin = 0
    matrix = fillMatrix()
    size = 900
    i = 0
    j = 0
    for i in range(size):
        for j in range(size):
            temp = matrix[i][j]
            if testPalin(temp):
                if temp > maxPalin:
                    maxPalin = temp
    return maxPalin
    

