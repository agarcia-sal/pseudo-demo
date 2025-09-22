# Start
timePeriod = int(input())
resultCount = 0

for currentNumber in range(1, timePeriod + 1):
    divisorCount = 0
    tempNumber = currentNumber
    
    for potentialDivisor in range(2, currentNumber):
        if tempNumber % potentialDivisor == 0:
            divisorCount += 1
            while tempNumber % potentialDivisor == 0:
                tempNumber //= potentialDivisor
    
    if divisorCount == 2:
        resultCount += 1

print(resultCount)
# End


import math

def count_unique_prime_factors(n):
    if n < 2:
        return 0
    
    divisorCount = 0
    tempNumber = n
    
    # Check for potential divisors up to square root of n
    for potentialDivisor in range(2, int(math.sqrt(n)) + 1):
        if tempNumber % potentialDivisor == 0:
            divisorCount += 1
            while tempNumber % potentialDivisor == 0:
                tempNumber //= potentialDivisor
    
    # Check if the remaining tempNumber is a prime factor greater than sqrt(n)
    if tempNumber > 1:
        divisorCount += 1
    
    return divisorCount

timePeriod = int(input())
resultCount = 0

for currentNumber in range(1, timePeriod + 1):
    if count_unique_prime_factors(currentNumber) == 2:
        resultCount += 1

print(resultCount)
