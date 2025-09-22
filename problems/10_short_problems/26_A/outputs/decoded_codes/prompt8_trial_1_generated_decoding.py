def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(limit):
    semiprimeCount = 0

    for currentNumber in range(1, limit + 1):
        primeFactorCount = 0
        tempNumber = currentNumber

        for potentialFactor in range(2, currentNumber):
            if tempNumber % potentialFactor == 0 and is_prime(potentialFactor):
                primeFactorCount += 1
                while tempNumber % potentialFactor == 0:
                    tempNumber //= potentialFactor
        
        if primeFactorCount == 2:
            semiprimeCount += 1

    return semiprimeCount

limit = int(input())
result = count_semiprimes(limit)
print(result)
