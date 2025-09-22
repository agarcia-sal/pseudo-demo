def count_semi_primes():
    t = int(input())
    totalSemiPrimes = 0

    for currentNumber in range(1, t + 1):
        divisorCount = 0
        tempNumber = currentNumber

        for potentialDivisor in range(2, currentNumber):
            if tempNumber % potentialDivisor == 0:
                divisorCount += 1
                
                while tempNumber % potentialDivisor == 0:
                    tempNumber //= potentialDivisor

        if divisorCount == 2:
            totalSemiPrimes += 1
    
    print(totalSemiPrimes)

# Call the function to execute
count_semi_primes()
