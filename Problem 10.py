"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer: 142913828922

logic, similar to problem seven. let's find the prime numbers through 2million by storing and testing.
sum along the way

sieve approach is faster, use it to test prime.

"""
import time
import math

def sumPrime(n):
    start_time = time.time()
    counter = 2
    i = 0
    flag = 0
    num = 3
    lst = [2, 3]
    primeSum = 5
    if n < 3:
        return "Need n larger than 3"
    
    while num < n:
        flag = 1
        #checks number against list of primes. if a prime is a factor, rules out number as prime
        #and moves to check the next number
        for x in range(counter):
            modTest = (num % lst[x])
            if modTest == 0:
                flag = 0
                break
        #no prime was factor of number, therefore, number is a prime. add to prime number list
        if flag == 1:
            lst.append(num)
            primeSum = primeSum + num
            counter = counter + 1
        i = i + 1
        #potential primes are odd numbers
        num = 3 + 2*i
       
    print time.time() - start_time, "seconds"
    return primeSum

def newSumPrime(n):
    start_time = time.time()
    i = 1
    flag = 0
    num = 5
    lst = [2, 3]
    primeSum = 5
    counter = 2
    
    if n < 5:
        return "Need n larger than 5"
    
    while num < n:
        flag = 1
        primeCeiling = math.floor(math.sqrt(num))
        #checks number against list of primes. if a prime is a factor, rules out number as prime
        #and moves to check the next number
        for x in range(counter):
            testPrime = lst[x]
            if testPrime > primeCeiling:
                flag = 1
                break
            modTest = (num % lst[x])
            if modTest == 0:
                flag = 0
                break
        #no prime was factor of number, therefore, number is a prime. add to prime number list
        if flag == 1:
            lst.append(num)
            primeSum = primeSum + num
            counter = counter + 1
        i = i + 1
        #potential primes are odd numbers
        num = 3 + 2*i
       
    print time.time() - start_time, "seconds"
    return primeSum


    

        
