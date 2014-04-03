"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Answer: 232792560

logic, numbers 1-10 are multiples of 11-20, so only need to test 11-20
increment by 20, test if each number mod it = 0, if so return, if not go on

"""
import time

def lcm(start, end):
    start_time = time.time()
    lst = [x for x in range(start, end + 1)]
    modTest = 0
    multiple = 1
    lcm = 0
    size = len(lst)
    test = lst[size-1]
    while modTest == 0:
        for i in range(size):
            modTest = modTest + ((test*multiple) % lst[i])
        if modTest == 0:
            lcm = test * multiple
            break
        elif multiple == 40000000:
            print time.time() - start_time, "seconds"
            return "Error, ran 40,000,000 times and no multiple"
        else:
            multiple = multiple + 1
            modTest = 0

    print time.time() - start_time, "seconds"
    return lcm
    

        
