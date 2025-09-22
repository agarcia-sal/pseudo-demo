t = int(input())
primeCount = 0

for currentNumber in range(1, t + 1):
    divisorCount = 0
    tempNumber = currentNumber

    for divisor in range(2, currentNumber):
        if tempNumber % divisor == 0:
            divisorCount += 1
            while tempNumber % divisor == 0:
                tempNumber //= divisor

    if divisorCount == 2:
        primeCount += 1

print(primeCount)
