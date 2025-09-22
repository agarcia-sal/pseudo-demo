def countSemiprimes(limit):
    semiprimeCount = 0
    for i in range(1, limit + 1):
        divisorCount = 0
        currentNumber = i
        for potentialDivisor in range(2, i):
            if currentNumber % potentialDivisor == 0:
                divisorCount += 1
                while currentNumber % potentialDivisor == 0:
                    currentNumber //= potentialDivisor
            if divisorCount > 2:  # Early exit if we already have more than 2 divisors
                break
        if divisorCount == 2:
            semiprimeCount += 1
    return semiprimeCount

inputLimit = int(input())
output = countSemiprimes(inputLimit)
print(output)
