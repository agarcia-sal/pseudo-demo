totalNumbers = int(input())
primeCount = 0

for currentNumber in range(1, totalNumbers + 1):
    divisorCount = 0
    numerator = currentNumber
    
    for potentialDivisor in range(2, currentNumber):
        if numerator % potentialDivisor == 0:
            divisorCount += 1
            while numerator % potentialDivisor == 0:
                numerator //= potentialDivisor

    if divisorCount == 2:
        primeCount += 1

print(primeCount)
