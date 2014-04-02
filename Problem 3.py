"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Answer: 6857


"""

def primefactor(n):
    i = 2
    prime = 0

    while(i <= n):
        if (n % i) == 0:
            n = n / i
            prime = i
            i = i + 1
        else:
            i = i + 1

    if prime == 0:
        return n
    else:
        return prime
        
    

        
    
