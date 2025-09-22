def countSemiPrimes(inputNumber):
    resultCounter = 0
    
    for currentNumber in range(1, inputNumber + 1):
        divisorCount = 0
        tempNumber = currentNumber
        
        for potentialDivisor in range(2, currentNumber):
            if tempNumber % potentialDivisor == 0:
                divisorCount += 1
                
                while tempNumber % potentialDivisor == 0:
                    tempNumber //= potentialDivisor
        
        if divisorCount == 2:
            resultCounter += 1
            
    return resultCounter

# Example usage
t = int(input())
print(countSemiPrimes(t))
