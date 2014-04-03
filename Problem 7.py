"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Answer: 104743

logic, similar to problem three. let's find the prime numbers with through storing and testing.

"""
import time

def nthPrime(n):
    start_time = time.time()
    counter = 2
    i = 0
    flag = 0
    num = 0
    lst = [2, 3]
    if n < 3:
        return "Need n larger than 3"
    
    while counter < n:
        flag = 1
        i = i + 1
        #potential primes are odd numbers
        num = 3 + 2*i
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
            counter = counter + 1
       
    print time.time() - start_time, "seconds"
    return num
    

        
