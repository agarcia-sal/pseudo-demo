def countSemiprimeNumbers():
    maximumNumber = int(input())
    semiprimeCount = 0

    for currentNumber in range(1, maximumNumber + 1):
        distinctPrimeCount = 0
        tempNumber = currentNumber
        
        for potentialFactor in range(2, currentNumber):
            if tempNumber % potentialFactor == 0:
                distinctPrimeCount += 1
                while tempNumber % potentialFactor == 0:
                    tempNumber //= potentialFactor  # Reduce tempNumber
                
        if distinctPrimeCount == 2:
            semiprimeCount += 1

    print(semiprimeCount)
