t = int(input())
resultCount = 0

for currentNumber in range(1, t + 1):
    distinctPrimeFactorsCount = 0
    tempNumber = currentNumber

    for potentialFactor in range(2, currentNumber):
        if tempNumber % potentialFactor == 0:
            distinctPrimeFactorsCount += 1
            while tempNumber % potentialFactor == 0:
                tempNumber //= potentialFactor

    if distinctPrimeFactorsCount == 2:
        resultCount += 1

print(resultCount)


t = int(input())
requiredDistinctCount = 2  # This can be changed for different requirements
resultCount = 0

for currentNumber in range(2, t + 1):  # Start from 2 since 1 has no prime factors
    distinctPrimeFactorsCount = 0
    tempNumber = currentNumber

    for potentialFactor in range(2, int(currentNumber**0.5) + 1):
        if tempNumber % potentialFactor == 0:
            distinctPrimeFactorsCount += 1
            while tempNumber % potentialFactor == 0:
                tempNumber //= potentialFactor

        if distinctPrimeFactorsCount > requiredDistinctCount:  # Early exit if count exceeds needed
            break

    if tempNumber > 1:  # If tempNumber is still greater than 1, it is a prime itself
        distinctPrimeFactorsCount += 1

    if distinctPrimeFactorsCount == requiredDistinctCount:
        resultCount += 1

print(resultCount)
