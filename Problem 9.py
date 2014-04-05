"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Answer: 31875000 

logic: set, a and c, test for b

"""
import time

def pythaTriplet():
    start_time = time.time()
    for c in range(1, 1001):
        for a in range(1, 1001):
            b = 1000 - c - a
            if ((a*a + b*b) == c*c) and b > 0:
                print time.time() - start_time, "seconds"
                return a*b*c
    print time.time() - start_time, "seconds"
    return "Error, no answer"



#simplified formula:
"""
a + b + c = 1000            Take the square of both sides
a^2 + b^2 + c^2 + 2(ab + bc + ac) = 10^6 

Write c^2 as a^2 + b^2
a^2 + b^2 + ab + bc + ac = 5E5    add ab to both sides
(a + b)^2 + c(a + b) = 5E5 + ab
(a + b + c)(a + b) = 5E5 + ab We know that a + b + c = 1000
1000a + 1000b - ab = 5E5
a(1000 - b) + 1000b = 5E5
"""

def revisedPytha():
    start_time = time.time()
    for b in range(1, 1001):
        a =(500000 - 1000*b)/(1000-b)
        if isinstance(a, int):
            c = 1000 - a - b
            if (a*a + b*b) == (c*c):
                print time.time() - start_time, "seconds"
                print a, b, c
                return a*b*c
    print time.time() - start_time, "seconds"
    return "Error, ran through loop, found no solution"
    

        
