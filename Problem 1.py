"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168
"""

def multiples(n):
	sum = 0
	i = 1
	j = 1
	m = 1
	while(i*3 < n):
		sum+= i*3
		i = i + 1
		
	while(j*5 < n):
		sum+= j*5
		j = j + 1
		
	while(m*15 < 1000):
		sum -= m*15
		m = m + 1
	
	return sum
	
